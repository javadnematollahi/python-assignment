import cv2

brave_boy=cv2.imread('pesar_shoja.jpg')
brave_boy=cv2.cvtColor(brave_boy,cv2.COLOR_BGR2GRAY)
pic_size=brave_boy.shape
black_width=50

for i in range(100):
        if i<=100-black_width:
           brave_boy[i,100-black_width-i:100-i]=0
        else:
           brave_boy[i,0:100-i]=0

cv2.imshow(" ",brave_boy)
cv2.waitKey()