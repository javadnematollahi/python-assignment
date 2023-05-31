###  cv2.contourArea()
import cv2
import numpy as np
from matplotlib import pyplot as plt


# def contour_area_j(contour,areaaa):
def contour_area_j(contour):
    area=0
    min=np.min(contour,axis=0)
    max=np.max(contour,axis=0)
    dic_y=dict()
    dic_y_c=dict()
    for i in range(min[0][0],max[0][0]+1):
        for j in range(len(contour)):
            if contour[j][0][0]==i:
                if i in dic_y:
                    dic_y[i].append(contour[j][0][1])
                else:
                    dic_y[i]=[]
                    dic_y[i].append(contour[j][0][1])

    for i in dic_y:
        dic_y[i].sort(reverse=True)
        dic_y_c[i]=[]
        dic_y_c[i].append(dic_y[i][0])
        for c in range(len(dic_y[i])-1):
            if dic_y[i][c]-dic_y[i][c+1]>25:
                dic_y_c[i].append(dic_y[i][c+1])

        for j in range(len(dic_y_c[i])//2):
            area+=dic_y_c[i][2*j]-dic_y_c[i][2*j+1]+1
            # for k in range(dic_y_c[i][2*j+1],dic_y_c[i][2*j]):
            #     areaaa[k,i]=255

    # plt.imshow(areaaa,cmap="gray")
    # plt.show()
    return area



image=cv2.imread("input/wolf.jpg",cv2.IMREAD_GRAYSCALE)
result= image.copy()
_, image_thresh = cv2.threshold(image,115,255,cv2.THRESH_BINARY)
areaaa=np.zeros((image.shape[0],image.shape[1]))

contours, _ =cv2.findContours(image_thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)


for contour in contours:
    if cv2.contourArea(contour)>300:
        x,y,w,h=cv2.boundingRect(contour)
        cv2.rectangle(result,(x,y),(x+w,y+h),(255,255,255),3)
        cv2.putText(result,f'opencv contourArea output:',(x,y-160),cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,255,255),thickness=2,lineType=cv2.LINE_AA)
        cv2.putText(result,f'{cv2.contourArea(contour)}',(x,y-120),cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,255,255),thickness=2,lineType=cv2.LINE_AA)

        cv2.putText(result,f'my contourArea output:',(x,y-80),cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,255,255),thickness=2,lineType=cv2.LINE_AA)
        cv2.putText(result,f'{contour_area_j(contour)}',(x,y-40),cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,255,255),thickness=2,lineType=cv2.LINE_AA)

cv2.imwrite("output/contour_area4.jpg",result)

plt.imshow(result,cmap="gray")
plt.show()