import cv2
import numpy as np
# from matplotlib import pyplot as plt



cap=cv2.VideoCapture("input/funny_video.mp4")
cap1=cv2.VideoCapture(0)

_,camera=cap1.read()
rows1=camera.shape[0]
cols1=camera.shape[1]
print(rows1,cols1)

_,video=cap.read()
rows=video.shape[0]
cols=video.shape[1]
print(rows,cols)
size=(cols,rows)

fps = 40
writer= cv2.VideoWriter("output/javad.mp4",cv2.VideoWriter_fourcc(*'XVID'),fps, size,0)
pause=0
while True:
    if pause==0:
        _,video=cap.read()
    _,camera=cap1.read()
    camera=cv2.resize(camera,(cols+200,rows-200))
    img_v = cv2.flip(camera, 1)
    # print(camera.shape)
    video_gray=cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
    camera_gray=cv2.cvtColor(img_v,cv2.COLOR_BGR2GRAY)
    video_gray[274:424,130:280]=camera_gray[274:424,130:280]
    writer.write(video_gray)


    cv2.imshow(" ",video_gray)
    key=cv2.waitKey(25) & 0xFF
    if key==ord('s'):
        pause=1
    if key==ord('p'):
        pause=0
    if key==ord('q'):
        break


cap.release()
writer.release()
cv2.destroyAllWindows()
