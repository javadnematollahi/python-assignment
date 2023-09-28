import cv2
import numpy as np


floor1=cv2.imread("input/floor1.jpg")
floor2=cv2.imread("input/floor2.jpg")
mask=cv2.imread("input/floor3.jpg")

# floor1=floor1.astype(np.float32)
# floor2=floor2.astype(np.float32)
# mask=mask.astype(np.float32)
floor1=cv2.resize(floor1,[800,800])
floor2=cv2.resize(floor2,[800,800])
mask=cv2.resize(mask,[800,800])
print(mask.shape)

# mask=mask/255
mask=mask.astype(np.uint8)
a,b,_=mask.shape

mask1=cv2.multiply(mask,floor2)

cv2.imshow("",mask1)
cv2.waitKey()

for i in range(a):
    for j in range(b):
        for k in range(3):
            if mask1[i,j,k]!=255:
                mask1[i,j]=0
cv2.imshow("",mask1)
cv2.waitKey()               

mask1=mask1/255
mask1=mask1.astype(np.uint8)

ground_extract=cv2.multiply(mask1,floor2)

# cv2.imshow("",ground_extract)
# cv2.waitKey()

mask1=mask1-1
# mask1=mask1/255
mask1=mask1.astype(np.uint8)
mask2=cv2.multiply(mask1,floor1)

for i in range(a):
    for j in range(b):
        for k in range(3):
            if mask2[i,j,k]!=0:
                mask2[i,j]=255
# cv2.imshow("",mask2)
# cv2.waitKey()  

mask2=mask2/255
mask2=mask2.astype(np.uint8)
other_extracted=cv2.multiply(mask2,floor1)

final=other_extracted+ground_extract
other_extracted=cv2.resize(final,[800,800])
# cv2.imwrite("output/masking_picture.jpg",final)

# cv2.imshow("",other_extracted)
# cv2.waitKey()