import cv2
import numpy as np
import matplotlib.pyplot as plt

ballone=cv2.imread("input/ballones.jpg")
ballone=cv2.cvtColor(ballone,cv2.COLOR_BGR2HSV)

h,s,v=cv2.split(ballone)
h1=h.copy()
# h1=np.where(np.logical_and(h>150,h<165),h,0)
v1=np.where(np.logical_and(h>7,h<18),v,0)
v1=np.where(s>210,v1,0)
ballone1=cv2.merge((h,s,v1))
ballone=cv2.cvtColor(ballone,cv2.COLOR_HSV2RGB)
ballone1=cv2.cvtColor(ballone1,cv2.COLOR_HSV2RGB)
ballone_mix=np.hstack((ballone,ballone1))
cv2.imshow("",ballone_mix)
cv2.waitKey()
cv2.imwrite("output/ballone.jpg",ballone_mix)


