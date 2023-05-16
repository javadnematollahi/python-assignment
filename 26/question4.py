import cv2
import numpy as np

first_array=np.zeros((600,400),np.uint8)
first_array[0:600,0:400]=255

first_array[70:100,150:310]=100
first_array[100:450,215:245]=100
first_array[450:480,130:215]=100
first_array[400:450,100:130]=100

cv2.imshow(" ",first_array)
cv2.waitKey()