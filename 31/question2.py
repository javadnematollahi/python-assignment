import cv2
import numpy as np

flower=cv2.imread("input/flower.jpg",cv2.IMREAD_GRAYSCALE)
rows , cols = flower.shape

mask=np.zeros((cols,rows),dtype=np.uint8)
filter2=np.ones((11,11))/121


for i in range(5,rows-5):
    for j in range(5,cols-5):
        mask[j,i]=np.abs(np.sum(flower[j-5:j+6,i-5:i+6]*filter2))

_, mask=cv2.threshold(mask,117,255,cv2.THRESH_BINARY)

mask[rows-30:rows,:]=0

mask=mask//255

flower1=np.multiply(mask,flower)

mask=mask-1
mask=mask//255
background=np.multiply(mask,flower)

blurred_frame = cv2.GaussianBlur(background, (25, 25), 0)

result=cv2.add(blurred_frame,flower1)
cv2.imwrite("output/flower.png",result)
cv2.imshow("",result)
cv2.waitKey()
