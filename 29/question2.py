import cv2
import numpy as np

s_1_float=[];s_2_float=[];s_3_float=[];s_4_float=[]

s_1=[]
s_1.append(cv2.imread("input/1/1.jpg"));s_1.append(cv2.imread("input/1/2.jpg"));s_1.append(cv2.imread("input/1/3.jpg"))
s_1.append(cv2.imread("input/1/4.jpg"));s_1.append(cv2.imread("input/1/5.jpg"))
print(s_1[0].shape)
s_2=[]
s_2.append(cv2.imread("input/2/1.jpg"));s_2.append(cv2.imread("input/2/2.jpg"));s_2.append(cv2.imread("input/2/3.jpg"))
s_2.append(cv2.imread("input/2/4.jpg"));s_2.append(cv2.imread("input/2/5.jpg"))
s_3=[]
s_3.append(cv2.imread("input/3/1.jpg"));s_3.append(cv2.imread("input/3/2.jpg"));s_3.append(cv2.imread("input/3/3.jpg"))
s_3.append(cv2.imread("input/3/4.jpg"));s_3.append(cv2.imread("input/3/5.jpg"))
s_4=[]
s_4.append(cv2.imread("input/4/1.jpg"));s_4.append(cv2.imread("input/4/2.jpg"));s_4.append(cv2.imread("input/4/3.jpg"))
s_4.append(cv2.imread("input/4/4.jpg"));s_4.append(cv2.imread("input/4/5.jpg"))

for i in range(5):
    s_1_float.append(s_1[i].astype(np.float32))
    s_2_float.append(s_2[i].astype(np.float32))
    s_3_float.append(s_3[i].astype(np.float32))
    s_4_float.append(s_4[i].astype(np.float32))
    
for i in range(1,5):
    s_1_float[0]+=s_1_float[i]
    s_2_float[0]+=s_2_float[i]
    s_3_float[0]+=s_3_float[i]
    s_4_float[0]+=s_4_float[i]
    
s_1_float[0]=s_1_float[0]/5;s_2_float[0]=s_2_float[0]/5;s_3_float[0]=s_3_float[0]/5;s_4_float[0]=s_4_float[0]/5

result=[]
result.append(s_1_float[0].astype(np.uint8));result.append(s_2_float[0].astype(np.uint8))
result.append(s_3_float[0].astype(np.uint8));result.append(s_4_float[0].astype(np.uint8))

up=np.concatenate((result[0],result[1]),axis=1);down=np.concatenate((result[2],result[3]),axis=1)

final=np.concatenate((up,down),axis=0)

final=cv2.resize(final,(1000,1000))

cv2.imwrite("output/holespace.jpg",final)

cv2.imshow(" ",final)
cv2.waitKey()