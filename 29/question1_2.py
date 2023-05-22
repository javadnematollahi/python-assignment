import cv2
import numpy as np

animal=cv2.imread("input/animal.jpg")
javad=cv2.imread("input/javad.jpg")
#  you can set i in range (0,1,2,3)  and you can set j in range (0,1,2) to
# choose your animal among animals in animal picture in input folder
i=1;j=1
h,w,_=animal.shape
print(w,h)
#396 * 340
animal_offset=250
my_animal=np.zeros((int((h-animal_offset)/4),int(w/3),3))

my_animal=animal[int(animal_offset+i*(h-animal_offset)/4):int(animal_offset+(i+1)*(h-animal_offset)/4),int(j*w/3):int((j+1)*w/3)]

javad=cv2.resize(javad,(int(w/3),int((h-animal_offset)/4)))

face_detector=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces= face_detector.detectMultiScale(javad,1.3)



for face in faces:
    x1,y1,w1,h1=face
    my_animal=cv2.resize(my_animal,(int(w1*1.4),int(h1*1.7)))
# print(x,y,w,h)
my_animal=my_animal.astype(np.float32)
javad=javad.astype(np.float32)
t=75
t1=70
for a in range(int(w1*1.4)):
    for b in range(int(h1*1.7)):
        if my_animal[b,a,0]<220 and my_animal[b,a,1]<220 and my_animal[b,a,2]<220:
            javad[y1-t1+b,x1-t+a]=javad[y1-t1+b,x1-t+a]*6/20+my_animal[b,a]*14/20
            # javad[y1-t1+b,x1-t+a]=javad[y1-t1+b,x1-t+a]*1/2+my_animal[b,a]*0.75 

mix_result=javad
# mix_result=np.add(my_animal,javad)
cv2.imwrite("output/animal_face.jpg",mix_result)
mix_result=mix_result.astype(np.uint8)

cv2.imshow(" ", mix_result)

cv2.waitKey()
