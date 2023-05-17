import cv2
import numpy as np
import imageio
import random

winter=cv2.imread('winter.jpg')
winter=cv2.cvtColor(winter,cv2.COLOR_BGR2GRAY)
a,b=winter.shape
print(a,b)
fps = 30
size=(b,a)
khoroj=0
i=0
x_center=[]
y_center=[]
for _ in range(50):
    random_x=random.randint(0,b)
    random_y=random.randint(0,a)
    x_center.append(random_x)
    y_center.append(random_y)
writer= cv2.VideoWriter("winter.avi",cv2.VideoWriter_fourcc(*'MJPG'),fps, size,0)
my_image=np.ones((5,5),dtype=np.uint8)*255
while True:
    counter=0
    for height in range(a):
        winter=cv2.imread('winter.jpg')
        winter=cv2.cvtColor(winter,cv2.COLOR_BGR2GRAY)
        for barf in range(50-counter):
            # print(random_x,random_y)
            if y_center[barf]+height>=a:
                counter+=1
                y_center.pop(barf)
                x_center.pop(barf)
                random_x=random.randint(0,b)
                # random_y=random.randint(0,a)
                x_center.append(random_x)
                y_center.append(height)
            cv2.circle(winter, (x_center[barf],y_center[barf]+height),4,255,-1)
            if height==a-1:
                y_center[barf]=y_center[barf]+height

        for barf in range(counter):
            cv2.circle(winter, (x_center[49-barf],height-y_center[49-barf]),4,255,-1)
            if height==a-1:
                y_center[49-barf]=height-y_center[49-barf]

        writer.write(winter)
        
        cv2.imshow(" ",winter)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            khoroj=1
            break
    if khoroj==1:
        break


writer.release()
cv2.destroyAllWindows()

cap = cv2.VideoCapture('winter.avi')
image_lst = []
 
while True:
    ret, frame = cap.read()
    image_lst.append(frame)

    i+=1
    if i==120:
        i=0
        break

    cv2.imshow('a', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
 
# Convert to gif using the imageio.mimsave method
imageio.mimsave('winter.gif', image_lst, fps=30)