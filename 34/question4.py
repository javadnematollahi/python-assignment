import cv2
import numpy as np
import matplotlib.pyplot as plt

image= cv2.imread("input/rubic.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

print(image.shape[0],image.shape[1])
imagec=image.copy()
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i,j,0]>95 and image[i,j,1]<90 and image[i,j,2]<45:
            image[i,j,0]=0;image[i,j,1]=255;image[i,j,2]=255
        if image[i,j,0]<105 and image[i,j,1]<105 and image[i,j,2]>120:
            image[i,j,0]=255;image[i,j,1]=255;image[i,j,2]=0
        if image[i,j,0]<70 and image[i,j,1]>70 and image[i,j,2]<55:
            image[i,j,0]=255;image[i,j,1]=0;image[i,j,2]=255



plt.imshow(image,cmap="gray")
plt.show()
plt.imshow(imagec,cmap="gray")
plt.show()

convert=np.hstack((imagec,image))
convert=cv2.cvtColor(convert,cv2.COLOR_RGB2BGR)
cv2.imwrite("output/solved_rubic.jpg",convert)
