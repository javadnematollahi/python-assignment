import cv2
import numpy as np

first= cv2.imread("input/firstpic.jpg")
second=cv2.imread("input/secondpic.jpg")

first_f=255-first
seconde_f=255-second
result=first_f- seconde_f
result=255-result


cv2.imwrite("output/secret_txt.jpg",result)

cv2.imshow(" ",result)
cv2.waitKey()