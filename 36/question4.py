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

writer1= cv2.VideoWriter("color_detect.avi",cv2.VideoWriter_fourcc(*'MJPG'),fps, (width*2,height))
lower = np.array([0, 48, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")
while True:
    _ ,frame=cap.read()
    frame=cv2.resize(frame,(width,height))

    frame=cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)

    frame= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # H,S,V=cv2.split(frame)
    # mask=np.where(np.logical_and(H<21,H>=0),V,0)
    # mask1=np.where(np.logical_and(S>40,S<250),mask,0)#80
    # mask2=np.where(np.logical_and(V>80,V<=255),mask1,0)#80
    # frame1=cv2.merge((H,S,mask2))
    skinMask = cv2.inRange(frame, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    skinMask = cv2.erode(skinMask, kernel, iterations = 2)
    skinMask = cv2.dilate(skinMask, kernel, iterations = 2)
    skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
    skin = cv2.bitwise_and(frame, frame, mask = skinMask)



    # print(H[300,300],end=",");print(S[300,300],end=",");print(V[300,300])
    frame= cv2.cvtColor(frame,cv2.COLOR_HSV2BGR)
    skin= cv2.cvtColor(skin,cv2.COLOR_HSV2BGR)
    writer1.write(np.hstack([frame, skin]))

    cv2.imshow("",np.hstack([frame, skin]))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break