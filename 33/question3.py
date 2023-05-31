###  cv2.boundingRect()
import cv2
import numpy as np
from matplotlib import pyplot as plt


def boundrect_j(contour):
    min=np.min(contour,axis=0)
    max=np.max(contour,axis=0)
    h=max[0][1]-min[0][1]+1
    w=max[0][0]-min[0][0]+1
    x=min[0][0]
    y=min[0][1]
    return x,y,w,h



image=cv2.imread("input/wolf.jpg",cv2.IMREAD_GRAYSCALE)
result= image.copy()
_, image_thresh = cv2.threshold(image,115,255,cv2.THRESH_BINARY)

contours, _ =cv2.findContours(image_thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

counter=0
for contour in contours:
    if cv2.contourArea(contour)>300:
        x,y,w,h=cv2.boundingRect(contour)
        cv2.rectangle(result,(x,y),(x+w,y+h),(255,255,255),3)
        cv2.putText(result,f'opencv boundrect output:',(x,y-160),cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,255,255),thickness=2,lineType=cv2.LINE_AA)
        cv2.putText(result,f'x={x},y={y},w={w},h={h}',(x,y-120),cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,255,255),thickness=2,lineType=cv2.LINE_AA)
        x1,y1,w1,h1=boundrect_j(contour)
        cv2.rectangle(result,(x1,y1),(x1+w1,y1+h1),(0,255,0),3)
        cv2.putText(result,f'my boundrect output:',(x1,y1-80),cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,255,255),thickness=2,lineType=cv2.LINE_AA)
        cv2.putText(result,f'x={x1},y={y1},w={w1},h={h1}',(x1,y1-40),cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,255,255),thickness=2,lineType=cv2.LINE_AA)

cv2.imwrite("output/boundrect.jpg",result)
plt.imshow(result,cmap="gray")
plt.show()

