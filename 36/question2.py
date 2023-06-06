import cv2
import numpy as np


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
light_Red  = np.array([80,20,30])
dark_Red  = np.array([190,80,80])
while True:
    _ ,frame=cap.read()
    frame=cv2.resize(frame,(width,height))

    frame=cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)

    frame= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    cv2.rectangle(frame,(width//3,height//3),((2*width)//3,(2*height)//3),255,10)
    H,S,V=cv2.split(frame)
    frame1=frame.copy()
    frame1=cv2.blur(frame1,(15,15))
    frame1[height//3:(2*height)//3,width//3:(2*width)//3]=frame[height//3:(2*height)//3,width//3:(2*width)//3]
    frame1= cv2.cvtColor(frame1,cv2.COLOR_HSV2BGR)

    detector_part_h=H[height//3:(2*height)//3,width//3:(2*width)//3]
    detector_part_s=S[height//3:(2*height)//3,width//3:(2*width)//3]
    detector_part_v=V[height//3:(2*height)//3,width//3:(2*width)//3]
    detect_S_0_1=np.where(detector_part_s>130,1,0)
    detect_V_0_1=np.where(detector_part_v>130,1,0)
    print(H[300,300],end=",");print(S[300,300],end=",");print(V[300,300])
    detect_0_1=np.where(np.logical_or(detector_part_h<9,detector_part_h>173),1,0)
    if (width*height//9)*0.95<cv2.countNonZero(detect_0_1) and (width*height//9)*0.7<cv2.countNonZero(detect_S_0_1):
        cv2.putText(frame1,"RED",(20,50),cv2.FONT_HERSHEY_SIMPLEX,2,(100,100,100),5)
    detect_0_1=np.where(np.logical_and(detector_part_h<15,detector_part_h>7),1,0)
    if (width*height//9)*0.6<cv2.countNonZero(detect_0_1) and (width*height//9)*0.7<cv2.countNonZero(detect_S_0_1):
        cv2.putText(frame1,"Orange",(20,50),cv2.FONT_HERSHEY_SIMPLEX,2,(100,100,100),5)
    detect_0_1=np.where(np.logical_and(detector_part_h<26,detector_part_h>17),1,0)
    if (width*height//9)*0.6<cv2.countNonZero(detect_0_1) and (width*height//9)*0.7<cv2.countNonZero(detect_S_0_1):
        cv2.putText(frame1,"Yellow",(20,50),cv2.FONT_HERSHEY_SIMPLEX,2,(100,100,100),5)
    detect_0_1=np.where(np.logical_and(detector_part_h<115,detector_part_h>103),1,0)
    if (width*height//9)*0.6<cv2.countNonZero(detect_0_1) and (width*height//9)*0.7<cv2.countNonZero(detect_S_0_1):
        cv2.putText(frame1,"blue",(20,50),cv2.FONT_HERSHEY_SIMPLEX,2,(100,100,100),5)
    detect_0_1=np.where(np.logical_and(detector_part_h<39,detector_part_h>30),1,0)
    if (width*height//9)*0.6<cv2.countNonZero(detect_0_1) and (width*height//9)*0.7<cv2.countNonZero(detect_S_0_1):
        cv2.putText(frame1,"Green",(20,50),cv2.FONT_HERSHEY_SIMPLEX,2,(100,100,100),5)
    

    detect_V_0_1=np.where(detector_part_v<95,1,0);detect_S_0_1=np.where(detector_part_s<120,1,0)
    if (width*height//9)*0.7<cv2.countNonZero(detect_V_0_1) and (width*height//9)*0.7<cv2.countNonZero(detect_S_0_1):
        cv2.putText(frame1,"Black",(20,50),cv2.FONT_HERSHEY_SIMPLEX,2,(100,100,100),5)
    detect_S_0_1=np.where(detector_part_s<80,1,0);detect_V_0_1=np.where(detector_part_v>120,1,0)
    if (width*height//9)*0.6<cv2.countNonZero(detect_S_0_1) and (width*height//9)*0.6<cv2.countNonZero(detect_V_0_1):
        cv2.putText(frame1,"White",(20,50),cv2.FONT_HERSHEY_SIMPLEX,2,(100,100,100),5)

    writer1.write(frame1)

    cv2.imshow("",frame1)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
writer1.release()
cv2.destroyAllWindows()