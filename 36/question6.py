import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread("input/javad.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
image_copy=image.copy()
tshirt=image[480:810,220:480]
tshirt=cv2.cvtColor(tshirt,cv2.COLOR_RGB2HSV)
h,s,v=cv2.split(tshirt)
lower = np.array([100, 0, 130], dtype = "uint8")
upper = np.array([185, 150, 255], dtype = "uint8")

Mask = cv2.inRange(tshirt, lower, upper)
h_m=np.where(Mask>250,30,h)
s_m=np.where(Mask>250,s-140,s)
final=cv2.merge((h_m,s_m,v))
final=cv2.cvtColor(final,cv2.COLOR_HSV2RGB)
image[480:810,220:480]=final
image[793:810,225:294]=image_copy[793:810,225:294]
image[790:811,453:480]=image_copy[790:811,453:480]
fig = plt.figure()
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)
ax1.axis('off')
ax2.axis('off')
ax3.axis('off')
image_big=image_copy[287:968,127:631]
yellow_big=image[287:968,127:631]
ax1.imshow(image_big,cmap="gray")
ax2.imshow(yellow_big,cmap="gray")


h_m=np.where(Mask>250,60,h)
s=np.where(np.logical_and(Mask>250,s<70) ,s-180,s)
s=np.where(np.logical_and(Mask>250,s>70) ,s+100,s)

final=cv2.merge((h_m,s,v))
final=cv2.cvtColor(final,cv2.COLOR_HSV2RGB)
image[480:810,220:480]=final
image[793:810,225:294]=image_copy[793:810,225:294]
image[790:811,453:480]=image_copy[790:811,453:480]


green_big=image[287:968,127:631]
ax3.imshow(green_big,cmap="gray")
plt.savefig("output/Tshirt.jpg")
plt.show()