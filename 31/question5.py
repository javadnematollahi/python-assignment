import numpy as np 
import cv2

body=cv2.imread("input/body.png",cv2.IMREAD_GRAYSCALE)
elec=cv2.imread("input/elec.png",cv2.IMREAD_GRAYSCALE)
circle=cv2.imread("input/circle.png",cv2.IMREAD_GRAYSCALE)


filter_5=np.ones((5,5))/25
filter_15=np.ones((15,15))/225

body_5 = cv2.filter2D(src=body, ddepth=-1, kernel=filter_5)
body_15 = cv2.filter2D(src=body, ddepth=-1, kernel=filter_15)

elec_5 = cv2.filter2D(src=elec, ddepth=-1, kernel=filter_5)
elec_15 = cv2.filter2D(src=elec, ddepth=-1, kernel=filter_15)

circle_5 = cv2.filter2D(src=circle, ddepth=-1, kernel=filter_5)
circle_15 = cv2.filter2D(src=circle, ddepth=-1, kernel=filter_15)

cv2.imwrite("output/body5.png",body_5)
cv2.imwrite("output/body15.png",body_15)

cv2.imwrite("output/elec_5.png",elec_5)
cv2.imwrite("output/elec_15.png",elec_15)

cv2.imwrite("output/circle_5.png",circle_5)
cv2.imwrite("output/circle_15.png",circle_15)

cv2.imshow("",body_15)
cv2.waitKey()
cv2.imshow("",elec_15)
cv2.waitKey()
cv2.imshow("",circle_15)
cv2.waitKey()