###  cv2.contourArea()
import cv2
import numpy as np
from matplotlib import pyplot as plt


def contour_area_j(contour):
    area=0

    min=np.min(contour,axis=0)
    max=np.max(contour,axis=0)
    w=max[0][0]-min[0][0]+1
    h=max[0][1]-min[0][1]+1
    x=min[0][0]
    y=min[0][1]
    a=[contour]
    area_rect=np.zeros((max[0][1]+2,max[0][0]+2))
    cv2.drawContours(area_rect, a, 0, (255, 255, 255), -1)
    for i in range(w):
        for j in range(h):
            if area_rect[j+min[0][1],i+min[0][0]]==255:
                area+=1
    # plt.imshow(area_rect,cmap="gray")
    # plt.show()
    return area-len(contour)



image=cv2.imread("input/wolf.jpg",cv2.IMREAD_GRAYSCALE)
result= image.copy()
_, image_thresh = cv2.threshold(image,115,255,cv2.THRESH_BINARY)

contours, _ =cv2.findContours(image_thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_TC89_KCOS)


for i,contour in enumerate(contours):
    if cv2.contourArea(contour)>20000:
        x,y,w,h=cv2.boundingRect(contour)
        cv2.rectangle(result,(x,y),(x+w,y+h),(255,255,255),3)
        cv2.putText(result,f'opencv contourArea output:',(x,y-160),cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,255,255),thickness=2,lineType=cv2.LINE_AA)
        cv2.putText(result,f'{cv2.contourArea(contour)}',(x,y-120),cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,255,255),thickness=2,lineType=cv2.LINE_AA)

        cv2.putText(result,f'my contourArea output:',(x,y-80),cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,255,255),thickness=2,lineType=cv2.LINE_AA)
        cv2.putText(result,f'{contour_area_j(contour)}',(x,y-40),cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,255,255),thickness=2,lineType=cv2.LINE_AA)

cv2.imwrite("output/contour_area4_1.jpg",result)

plt.imshow(result,cmap="gray")
plt.show()