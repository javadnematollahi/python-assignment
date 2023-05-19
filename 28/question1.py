import cv2
import numpy as np
rows=600
cols=900
image= np.ones((rows,cols),dtype=np.uint8)*180

for i in range(3):
    cv2.rectangle(image,[(2*i+1)*cols//7,0],[2*(i+1)*cols//7,rows],120,-1)

cv2.rectangle(image,[cols//28,cols//28],[cols-cols//28,rows-cols//28],255,4)

cv2.rectangle(image,[cols//28,rows//4],[(cols//7)+cols//28,rows*3//4],255,4)
cv2.rectangle(image,[cols-(cols//28+cols//7),rows//4],[cols-cols//28,rows*3//4],255,4)

cv2.rectangle(image,[cols//28,rows*3//8],[(cols//14)+cols//28,rows*5//8],255,4)
cv2.rectangle(image,[cols-(cols//28+cols//14),rows*3//8],[cols-cols//28,rows*5//8],255,4)

cv2.line(image,[cols//2,cols//28],[cols//2,rows-(cols//28)],255,4)

cv2.circle(image,[cols//2,rows//2],5,255,-1)
cv2.circle(image,[cols//2,rows//2],rows//6,255,4)

cv2.imshow(" ",image)
cv2.imwrite("output/soccer.jpg",image)
cv2.waitKey()