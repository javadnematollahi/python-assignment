###  contours, _ = cv2.findContours(image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

import cv2
import numpy as np
from matplotlib import pyplot as plt
import copy




def find_contour_j(image):
    contours=[]
    filter=np.array([[-1,-1,-1],
                    [-1,8,-1],
                    [-1,-1,-1]])
    image=cv2.filter2D(image,-1,filter)
    def toward_up(i,j,rotatee):

        if image[i-1,j-1]==255:
            i=i-1;j=j-1;head_direction=9;rotatee=0
        elif image[i-1,j]==255:
            i=i-1;j=j;head_direction=0;rotatee=0
        elif image[i-1,j+1]==255:
            i=i-1;j=j+1;head_direction=0;rotatee=0
        else:
            head_direction=3;rotatee+=1
        return i,j,rotatee,head_direction
    def toward_down(i,j,rotatee):

        if image[i+1,j+1]==255:
            i=i+1;j=j+1;head_direction=3;rotatee=0
        elif image[i+1,j]==255:
            i=i+1;j=j;head_direction=6;rotatee=0
        elif image[i+1,j-1]==255:
            i=i+1;j=j-1;head_direction=6;rotatee=0
        else:
            head_direction=9;rotatee+=1
        return i,j,rotatee,head_direction
    def toward_left(i,j,rotatee):

        if image[i+1,j-1]==255:
            i=i+1;j=j-1;head_direction=6;rotatee=0
        elif image[i,j-1]==255:
            i=i;j=j-1;head_direction=9;rotatee=0
        elif image[i-1,j-1]==255:
            i=i-1;j=j-1;head_direction=9;rotatee=0
        else:
            head_direction=0;rotatee+=1
        return i,j,rotatee,head_direction
    def toward_right(i,j,rotatee):

        if image[i-1,j+1]==255:
            i=i-1;j=j+1;head_direction=0;rotatee=0
        elif image[i,j+1]==255:
            i=i;j=j+1;head_direction=3;rotatee=0
        elif image[i+1,j+1]==255:
            i=i+1;j=j+1;head_direction=3;rotatee=0
        else:
            head_direction=6;rotatee+=1
            # print(rotatee)
        return i,j,rotatee,head_direction

    for j in range(1,image.shape[1]-1):
        for i in range(image.shape[0]-2,1,-1):
            if image[i,j]==255:
                head_direction=0
                # if i+1<image.shape[0] and j+1<image.shape[1] and j-1>=0 and i-1>=0:
                image[i,j-1]=0;image[i+1,j+1]=0;image[i+1,j-1]=0
                # if image[i,j-1]==255:
                #     if image[i+1,j]==0:
                #         head_direction=9
                # print(head_direction)
                for con in contours:
                    if (i,j) in con:
                        break
                else:
                    rot=0
                    contour=set()
                    contour.add((i,j))
                    a=copy.deepcopy(i);b=copy.deepcopy(j) 
                    check_terminate=0
                    while True:
                        if head_direction==0:
                            i,j,rot,head_direction=toward_up(i,j,rot)
                            contour.add((i,j))
                        elif head_direction==3:
                            i,j,rot,head_direction=toward_right(i,j,rot)
                            contour.add((i,j))
                        elif head_direction==6:
                            i,j,rot,head_direction=toward_down(i,j,rot)
                            contour.add((i,j))
                        elif head_direction==9:
                            i,j,rot,head_direction=toward_left(i,j,rot)
                            contour.add((i,j))
                        if rot==3:
                            contours.append(contour)
                            rot=0
                            break
                        if j==b and i==a:
                            check_terminate+=1
                            
                            if check_terminate==4:
                                contours.append(contour)
                                break
                    del contour                   
    return contours



image=cv2.imread("input/wolf.jpg",cv2.IMREAD_GRAYSCALE)
result= image.copy()
_, image_thresh = cv2.threshold(image,115,255,cv2.THRESH_BINARY)

# border=np.zeros((image.shape[0],image.shape[1]))
border1=np.zeros((image.shape[0],image.shape[1]))
border2=np.zeros((image.shape[0],image.shape[1]))


# border[1:image.shape[0]-1,1:image.shape[1]-1]=image_thresh[1:image.shape[0]-1,1:image.shape[1]-1]

# print(image_thresh.shape[0],image_thresh.shape[1])
# print(border1.shape)
contours1, _ =cv2.findContours(image_thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
contours=find_contour_j(image_thresh)
len1=0
simi=0
similar1=set()
for similar in range(len(contours)):
    for m,con in enumerate(contours):
        if m!=similar:
            for i in con:
                if i in contours[similar]:
                    simi+=1
                    if simi>150:
                        simi=0
                        if len(con)<len(contours[similar]):
                            similar1.add(m)
                        else:
                            similar1.add(similar)
                        break
similar1=list(similar1)
similar1.sort(reverse=True)
# print(similar1)
for i in similar1:
    contours.pop(i)
for m,con in enumerate(contours):
    for i in con:
        border1[i[0],i[1]]=255
for con in contours1:
    for i in con:
        border2[i[0][1],i[0][0]]=255

print(f'Our contours count is :{len(contours1)}')
print(f'Opencv contours count is :{len(contours)}')
plt.imshow(border1,cmap="gray")
plt.title(f'Our contours count is :{len(contours1)}')
plt.savefig('output/Our_contours.png')
plt.show()

plt.imshow(border2,cmap="gray")
plt.title(f'Opencv contours count is :{len(contours)}')
plt.savefig('output/Opencv_contours.png')
plt.show()
