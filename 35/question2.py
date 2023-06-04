import cv2
import numpy as np
import matplotlib.pyplot as plt

fps = 20

##use mobile camera
url='http://192.168.231.105:8080/video'
# you can put zero(0) instead of url
cap= cv2.VideoCapture(url)
_ , frame = cap.read()

frame=cv2.resize(frame,(600,600))
frame=frame.astype(dtype=np.uint8)
frame=cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
width= frame.shape[0]
height= frame.shape[1]

writer1= cv2.VideoWriter("color_detect.avi",cv2.VideoWriter_fourcc(*'MJPG'),fps, (width,height))
light_blue = np.array([5,15,50])
dark_blue = np.array([40,70,120])
light_Purple  = np.array([35,25,60])
dark_Purple  = np.array([90,60,110])
light_Red  = np.array([80,20,30])
dark_Red  = np.array([190,80,80])
light_Yellow  = np.array([110,80,10])
dark_Yellow  = np.array([170,130,50])
light_Green  = np.array([50,100,20])
dark_Green  = np.array([110,180,60])
light_Orange  = np.array([120,55,7])
dark_Orange  = np.array([190,100,50])
light_White  = np.array([100,100,100])
dark_White  = np.array([210,210,210])
light_Black  = np.array([0,0,0])
dark_Black = np.array([60,60,60])
while True:
    _ ,frame=cap.read()
    frame=cv2.resize(frame,(width,height))

    frame=cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)

    frame= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    cv2.rectangle(frame,(width//3,height//3),((2*width)//3,(2*height)//3),255,10)
    detector_part=frame[height//3:(2*height)//3,width//3:(2*width)//3]

    mask_blue = cv2.inRange(detector_part, light_blue, dark_blue)
    mask_Purple = cv2.inRange(detector_part, light_Purple, dark_Purple)
    mask_Red = cv2.inRange(detector_part, light_Red, dark_Red)
    mask_Yellow = cv2.inRange(detector_part, light_Yellow, dark_Yellow)
    mask_Green = cv2.inRange(detector_part, light_Green, dark_Green)
    mask_Orange = cv2.inRange(detector_part, light_Orange, dark_Orange)
    mask_White = cv2.inRange(detector_part, light_White, dark_White)
    mask_Black = cv2.inRange(detector_part, light_Black, dark_Black)
    print(detector_part[100,100,0],detector_part[100,100,1],detector_part[100,100,2])
    if (width*height//9)*0.5<cv2.countNonZero(mask_blue):
        cv2.putText(frame,"BLUE",(20,50),cv2.FONT_HERSHEY_SIMPLEX,2,(100,100,100),5)
    if (width*height//9)*0.5<cv2.countNonZero(mask_Purple):
        cv2.putText(frame,"Purple",(20,50),cv2.FONT_HERSHEY_SIMPLEX,2,(100,100,100),5)
    if (width*height//9)*0.5<cv2.countNonZero(mask_Red):
        cv2.putText(frame,"Red",(20,50),cv2.FONT_HERSHEY_SIMPLEX,2,(100,100,100),5)
    if (width*height//9)*0.5<cv2.countNonZero(mask_Yellow):
        cv2.putText(frame,"Yellow",(20,50),cv2.FONT_HERSHEY_SIMPLEX,2,(100,100,100),5)
    if (width*height//9)*0.5<cv2.countNonZero(mask_Green):
        cv2.putText(frame,"Green",(20,50),cv2.FONT_HERSHEY_SIMPLEX,2,(100,100,100),5)
    if (width*height//9)*0.5<cv2.countNonZero(mask_Orange):
        cv2.putText(frame,"Orange",(20,50),cv2.FONT_HERSHEY_SIMPLEX,2,(100,100,100),5)
    if (width*height//9)*0.5<cv2.countNonZero(mask_White):
        cv2.putText(frame,"White",(20,50),cv2.FONT_HERSHEY_SIMPLEX,2,(100,100,100),5)
    if (width*height//9)*0.5<cv2.countNonZero(mask_Black):
        cv2.putText(frame,"Black",(20,50),cv2.FONT_HERSHEY_SIMPLEX,2,(100,100,100),5)
    frame= cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    writer1.write(frame)

    cv2.imshow("",frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
writer1.release()
cv2.destroyAllWindows()
