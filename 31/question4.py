import numpy as np 
import cv2

image=cv2.imread("input/home.png",cv2.IMREAD_GRAYSCALE)
rows  = image.shape[0]
cols= image.shape[1]
result_V=np.zeros((rows,cols),dtype=np.uint8)
result_H=np.zeros((rows,cols),dtype=np.uint8)

#filter jadid baraye labe yabi ofoghi
filter_H=np.array([[-1,-1,-1],
                 [0,0,0],
                 [1,1,1]])

#filter jadid baraye labe yabi amodi
filter_V=np.array([[2,0,-2],
                 [2,0,-2],
                 [2,0,-2]])


for i in range(1,rows-1):
    for j in range(1,cols-1):
        small=image[i-1:i+2,j-1:j+2]
        result_V[i,j]=np.abs(np.sum(filter_V*small))

for i in range(1,rows-1):
    for j in range(1,cols-1):
        small=image[i-1:i+2,j-1:j+2]
        result_H[i,j]=np.abs(np.sum(filter_H*small))


cv2.imwrite("output/home_vertical.png",result_V)
cv2.imwrite("output/home_horizental.png",result_H)