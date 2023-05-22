import cv2
import numpy as np

javad=cv2.imread("input/javad.jpg")
yanni=cv2.imread("input/yanni.jpg")


javad=cv2.resize(javad,[300,300])
yanni=cv2.resize(yanni,[300,300])

javad_gray=javad.astype(np.float32)
yanni_gray=yanni.astype(np.float32)

mix1=javad_gray*3/4+yanni_gray*1/4
mix2=javad_gray*1/2+yanni_gray*1/2
mix3=javad_gray*1/4+yanni_gray*3/4

mix1=mix1.astype(np.uint8)
mix2=mix2.astype(np.uint8)
mix3=mix3.astype(np.uint8)

final=np.concatenate((javad,mix1,mix2,mix3,yanni),axis=1)

cv2.imwrite("output/mix_picture.jpg",final)

cv2.imshow(" ",final)
cv2.waitKey()