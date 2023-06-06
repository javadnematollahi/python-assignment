import cv2
import numpy as np
import matplotlib.pyplot as plt
import copy

image=cv2.imread("input/watermelon.jpg")

image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

h,s,v=cv2.split(image)
h_copy=h.copy()
h_copy=np.where( np.logical_and(h_copy>=0,h_copy<15),h_copy+60,h_copy)
h_copy=np.where( np.logical_and(h_copy>165,h_copy<=180),h_copy-120,h_copy)

h_copy=np.where(np.logical_and(h>25,h<=60),180+h-60, h_copy)
h_copy=np.where( np.logical_and(h>60,h<70),h-60,h_copy)


image_final=cv2.merge((h_copy,s,v))
materwelon=cv2.cvtColor(image_final,cv2.COLOR_HSV2RGB)

plt.imshow(materwelon,cmap="gray")
plt.savefig("output/materwelon_HSV.jpg")
plt.show()



