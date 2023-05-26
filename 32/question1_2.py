import numpy as np 
import cv2

image=cv2.imread("input/1.jpg",cv2.IMREAD_GRAYSCALE)

kernel_55_04=np.ones((5,5))/25
kernel_55_1=np.ones((5,5))
kernel_55_5=np.ones((5,5))*5
kernel_33_04=np.ones((3,3))/25
kernel_33_1=np.ones((3,3))
kernel_33_5=np.ones((3,3))*5

result_55_04=cv2.filter2D(image,-1,kernel=kernel_55_04)
result_55_1=cv2.filter2D(image,-1,kernel=kernel_55_1)
result_55_5=cv2.filter2D(image,-1,kernel=kernel_55_5)
result_33_04=cv2.filter2D(image,-1,kernel=kernel_33_04)
result_33_1=cv2.filter2D(image,-1,kernel=kernel_33_1)
result_33_5=cv2.filter2D(image,-1,kernel=kernel_33_5)

total_result=np.hstack((image,result_33_04,result_55_1,result_55_5,result_33_04,result_33_1,result_33_5))

cv2.imwrite("output/dycreption.jpg",total_result)
cv2.imshow("",total_result)
cv2.waitKey()

