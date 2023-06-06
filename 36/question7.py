import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread("input/spiderman.jpg")
image_copy=image.copy()
image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

# tshirt=image[480:810,220:480]
# tshirt=cv2.cvtColor(tshirt,cv2.COLOR_RGB2HSV)
h,s,v=cv2.split(image)
lower = np.array([100, 220, 0], dtype = "uint8")
upper = np.array([114, 255, 255], dtype = "uint8")


lower_r_down = np.array([0, 100, 10], dtype = "uint8")
upper_r_down = np.array([5, 255, 255], dtype = "uint8")
Mask_r_down = cv2.inRange(image, lower_r_down, upper_r_down)

lower_r_up = np.array([175, 100, 10], dtype = "uint8")
upper_r_up = np.array([180, 255, 255], dtype = "uint8")
Mask_r_up = cv2.inRange(image, lower_r_up, upper_r_up)
Mask_r_up=np.where(Mask_r_down>250,Mask_r_down,Mask_r_up)

Mask = cv2.inRange(image, lower, upper)
h_m=np.where(Mask>250,60,h)
h_m=np.where(Mask_r_up>250,25,h_m)
s_m=np.where(np.logical_and(Mask_r_up>250,s<230),s+30,s)
final=cv2.merge((h_m,s_m,v))
final=cv2.cvtColor(final,cv2.COLOR_HSV2RGB)


plt.imshow(final,cmap="gray")
plt.savefig("output/spiderman.jpg")
plt.show()
