import cv2
import os
import numpy as np


image=cv2.imread("input/numbers.png")
image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

try:
    for i in range(10):
        os.makedirs(f"output/{i}")
except:
    print("directories exist")


width_small=image_gray.shape[1]//100
height_small=image_gray.shape[0]//50
folder=0
for i in range(50):
    if i%5==0:
        folder+=1
    for j in range(100):
        small_pic=image[height_small*i:height_small*(i+1),width_small*j:width_small*(j+1)]
        cv2.imwrite(f"output/{folder-1}/{((i-(folder-1)*5)*100)+j}.png",small_pic)

            
