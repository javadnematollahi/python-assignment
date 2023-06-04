import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread("input/my_microsoft.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGBA)

print(image[0,0,0])

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i,j,0]>70 and image[i,j,0]<245 and image[i,j,1]>70 and image[i,j,1]<245 and image[i,j,2]>69 and image[i,j,2]<245:
            image[i,j,3]=0


image=cv2.cvtColor(image,cv2.COLOR_RGBA2BGRA)
cv2.imwrite("output/microsoft_transparent.png",image)
cv2.imshow("",image)
cv2.waitKey()




