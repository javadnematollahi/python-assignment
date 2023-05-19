import cv2

cat_image=cv2.imread('cats.jpg')
cat_gray=cv2.cvtColor(cat_image,cv2.COLOR_BGR2GRAY)

cat_detector=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')
cat_faces=cat_detector.detectMultiScale(cat_gray)

if len(cat_faces)>1:
    print(f'there are {len(cat_faces)} cats in the picture')
else:
    print(f'there is {len(cat_faces)} cat in the picture')

# for cat_face in cat_faces:
#     x,y,w,h=cat_face
#     cv2.rectangle(cat_image,[x,y],[x+w,y+h],0,4)

# cv2.imshow("",cat_image)
# cv2.waitKey()