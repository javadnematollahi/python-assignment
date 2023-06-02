import cv2
import numpy as np

r= np.ones((500,800),dtype=np.uint8)*255
g= np.ones((500,800),dtype=np.uint8)*255
b= np.ones((500,800),dtype=np.uint8)*255
# purple= 128 0 128
# blue=  0  0  255    125
# cyan = 0   255  255    150
# green=  0  255  0     175
#yellow=  255  255  0    200
# orange= 255  165  0     225
#red=  255   0   0     250
rainbow=[[128,0,128],[0,0,255],[0,255,255],[0,130,0],[255,255,0],[255,165,0],[255,0,0]]
# r.shape[0]=800   r.shape[1]=1500
#axes=(radius, radius)

for i in range(7):
    cv2.ellipse(r, (r.shape[1]//2,450), axes=(100+(i)*25, 100+(i)*25), angle=0, startAngle=180, endAngle=360,color=rainbow[i][0], thickness=25)
    cv2.ellipse(g, (g.shape[1]//2,450), axes=(100+(i)*25, 100+(i)*25), angle=0, startAngle=180, endAngle=360,color=rainbow[i][1], thickness=25)
    cv2.ellipse(b, (b.shape[1]//2,450), axes=(100+(i)*25, 100+(i)*25), angle=0, startAngle=180, endAngle=360,color=rainbow[i][2], thickness=25)

rainbow_pic=cv2.merge((b,g,r))
rainbow_pic[450:500,:,0:3]=255

cv2.imwrite("output/my_rainbow.jpg",rainbow_pic)
cv2.imshow("",rainbow_pic)
cv2.waitKey()