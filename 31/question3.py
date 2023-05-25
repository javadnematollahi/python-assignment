import cv2
import numpy as np

lion=cv2.imread("input/lion.png",cv2.IMREAD_GRAYSCALE)
spider=cv2.imread("input/spider.png",cv2.IMREAD_GRAYSCALE)


lion1 = cv2.Laplacian(lion,ddepth=cv2.CV_8U,ksize=1)


img = cv2.GaussianBlur(spider,(3,3),0)
spider1 = cv2.Laplacian(img,ddepth=cv2.CV_64F,ksize=5)
# this tends to localize the edge towards the brighter side.
spider2 = spider1/spider1.max()
spider3=spider2*255
# abs_dst = cv2.convertScaleAbs(spider2)
# spider2=spider2.astype(np.uint8)

cv2.imwrite("output/spider2.png",spider3)
cv2.imwrite("output/lion.png",lion1)
# cv2.imshow("",lion1)
# cv2.waitKey()
cv2.imshow("",spider2)
cv2.waitKey()