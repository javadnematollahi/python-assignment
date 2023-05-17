import cv2

threshold=100.
fps = 20
# be jaye 0 mitavan address yek file videoe dad
cap= cv2.VideoCapture(0)

_ , frame = cap.read()

height= frame.shape[0]
width= frame.shape[1]
# width=int(cap.get(3))
# height=int(cap.get(4))
size=(width,height)
writer= cv2.VideoWriter("color_detect.avi",cv2.VideoWriter_fourcc(*'MJPG'),fps, size,0)

while True:
    _ ,frame=cap.read()

    frame= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # _, frame=cv2.threshold(frame,threshold,255,cv2.THRESH_BINARY)
    cv2.rectangle(frame,(width//3,height//3),((2*width)//3,(2*height)//3),255,10)
    detector_part=frame[height//3:(2*height)//3,width//3:(2*width)//3]
    _, detector_part=cv2.threshold(detector_part,127,255,cv2.THRESH_BINARY)
    if (width*height//9)*0.3>cv2.countNonZero(detector_part):
        cv2.putText(frame,"Black",(20,50),
            cv2.FONT_HERSHEY_SIMPLEX,2,100,5)
    elif (width*height//9)*0.7<cv2.countNonZero(detector_part):
        cv2.putText(frame,"White",(20,50),
            cv2.FONT_HERSHEY_SIMPLEX,2,100,5)
    else:
        cv2.putText(frame,"Gray",(20,50),
            cv2.FONT_HERSHEY_SIMPLEX,2,100,5)        
    writer.write(frame)

    cv2.imshow("",frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
    # raveshe save kardan video