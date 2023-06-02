import cv2
import numpy as np


def RGB_to_Gray(image,method):
    Gray_image=np.zeros((image.shape[0],image.shape[1]),dtype=np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            method=method.lower()
            if method=="lightness":
                Gray_image[i,j]=(min(int(image[i,j,0]),int(image[i,j,1]),int(image[i,j,2]))+max(int(image[i,j,0]),int(image[i,j,1]),int(image[i,j,2])))//2
            elif method=="average":
                Gray_image[i,j]=(int(image[i,j,0])+int(image[i,j,1])+int(image[i,j,2]))//3
            elif method=="luminosity":
                Gray_image[i,j]=(0.299*image[i,j,0]+0.587*image[i,j,1]+0.114*image[i,j,2])//1
    return Gray_image

image= cv2.imread("input/monkey.jpg")

image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
image_lightness=RGB_to_Gray(image,"lightness")

image_average=RGB_to_Gray(image,"average")

image_luminosity=RGB_to_Gray(image,"luminosity")
pics=np.hstack((image_lightness,image_average,image_luminosity))
distance=6*" "
cv2.putText(pics,f"lightness{distance}average{distance}luminosity",(40,30),cv2.FONT_HERSHEY_SIMPLEX,0.75,255,2)
cv2.imwrite("output/color_to_gray.jpg",pics)
cv2.imshow("",pics)
cv2.waitKey()