import cv2

bat=cv2.imread('batman.jpg')
bat=cv2.cvtColor(bat,cv2.COLOR_BGR2GRAY)
rows,cols=bat.shape
threshold=130
threshold2=179
threshold1=140
# print(rows)
# print(cols)


for r in range(300,320):
    for c in range(480,500):
        if bat[r,c]>threshold and bat[r,c]<threshold2:
            bat[r,c]=0

_,bat=cv2.threshold(bat,threshold1,255,cv2.THRESH_BINARY_INV)




cv2.putText(bat,"BATMAN",(cols//3+50,rows-100),cv2.FONT_HERSHEY_SIMPLEX,2,255,2)

cv2.imshow("",bat)
cv2.waitKey()