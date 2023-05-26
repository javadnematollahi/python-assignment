import numpy as np 
import cv2

image=cv2.imread("input/bear.jpg",cv2.IMREAD_GRAYSCALE)
# kernel=np.ones((3,3))/9


# 1. Edge detection filter
kernel_e = np.array([[-1 , -1 , -1],
                   [-1 ,  8 , -1],
                   [-1 , -1 , -1]])

# 2. Sharpening filter
kernel_s = np.array([[0  , -1 ,  0],
                   [-1 ,  5 , -1],
                   [0  , -1 ,  0]])

# 3. Emboss filter
kernel_em = np.array([[-2 , -1 ,  0],
                   [-1 ,  1 ,  1],
                   [0  ,  1 ,  2]])

# 4. Identity filter
kernel_i = np.array([[0  ,  0 ,  0],
                   [0  ,  1 ,  0],
                   [0  ,  0 ,  0]])

# 4. j filter
kernel_j=np.array([[-1  ,  2 ,  -1],
                   [-1  ,  2 ,  -1],
                   [-1  ,  2 , -1]])



result_e=cv2.filter2D(image,ddepth=-1,kernel=kernel_e)
result_s=cv2.filter2D(image,ddepth=-1,kernel=kernel_s)
result_em=cv2.filter2D(image,ddepth=-1,kernel=kernel_em)
result_i=cv2.filter2D(image,ddepth=-1,kernel=kernel_i)
result_j=cv2.filter2D(image,ddepth=-1,kernel=kernel_j)

result=np.hstack((result_e,result_s,result_em,result_i,result_j))
cv2.imwrite("output/total_result.jpg",result)

cv2.imshow("",result)
cv2.waitKey()
