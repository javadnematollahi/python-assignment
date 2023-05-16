import cv2
import numpy as np

shaded_image=np.zeros((500,500),np.uint8)

shaded_image_size=shaded_image.shape

step=255/shaded_image_size[0]

for i in range(shaded_image_size[0]):
   shaded_image[i,0:shaded_image_size[1]-1]=int(255-(step*i))

cv2.imshow(" ",shaded_image)
cv2.waitKey()