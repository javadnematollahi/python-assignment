import cv2
import numpy as np
show_sticker=0
boy_sticker=cv2.imread('boy.jpg')
sunglass_sticker=cv2.imread('sunglasses.jpg')
lip_sticker=cv2.imread('lip.jpg')
# rabbit_gray=cv2.cvtColor(boy_sticker)

cap=cv2.VideoCapture(0)
_,video=cap.read()
video=cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
rows,cols = video.shape
result = cv2.VideoWriter('output/sticker.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, (cols,rows))

while True:
    _ , video=cap.read()

    face_gray=cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)

    face_detector=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces=face_detector.detectMultiScale(face_gray,1.3,5)

    for face in faces:
        x_face,y_face,w_face,h_face=face
        x_face1=x_face-int(w_face//7)
        y_face1=y_face-int(h_face//6)
        w_face1=int(w_face*1.3)
        h_face1=int(h_face*1.3)
        if show_sticker==1:
            sticker=cv2.resize(boy_sticker,[w_face1,h_face1])
            try:
                for a in range(w_face1):
                    for b in range(h_face1):
                        if sticker[b,a,0]==247 and sticker[b,a,1]==247 and sticker[b,a,2]==247:
                            sticker[b,a,0]=video[y_face1+b,x_face1+a,0] 
                            sticker[b,a,1]=video[y_face1+b,x_face1+a,1]
                            sticker[b,a,2]=video[y_face1+b,x_face1+a,2]
                video[y_face1:y_face1+h_face1,x_face1:x_face1+w_face1]=sticker
            except:
                print("please move to be in front of camera")
    if show_sticker==2:

        eye_detector=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        eyes=eye_detector.detectMultiScale(face_gray,1.1,10)
        if len(eyes)==2:
            x1,y1,w1,h1=eyes[0]
            x2,y2,w2,h2=eyes[1]
            x1=x1-w1//2
            w=abs(x2-x1)+w2+w1
            h=h1
            if y1>y_face and x1>x_face and x1+w<x_face+w_face and y1+h<y_face+h_face:
                sticker=cv2.resize(sunglass_sticker,[w,h])
                try:
                    for a in range(w):
                        for b in range(h):
                            if sticker[b,a,0]>=200 and sticker[b,a,1]>=200 and sticker[b,a,2]>=200:
                                    sticker[b,a,0]=video[y1+b,x1+a,0] 
                                    sticker[b,a,1]=video[y1+b,x1+a,1]
                                    sticker[b,a,2]=video[y1+b,x1+a,2]
                    video[y1:y1+h,x1:x1+w]=sticker
                except:
                    print("Please stand in the middle of the picture")
            smile_detector=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
            smiles=smile_detector.detectMultiScale(face_gray,1.8 ,20)

            for smile in smiles:
                x,y,w,h=smile
                if y>y1 and x>x1 and x+w<x_face+w_face and y+h<y_face+h_face:
                    sticker=cv2.resize(lip_sticker,[w,h])
                    try:
                        for a in range(w):
                            for b in range(h):
                                if sticker[b,a,0]==76 and sticker[b,a,1]==112 and sticker[b,a,2]==71:
                                    sticker[b,a,0]=video[y+b,x+a,0] 
                                    sticker[b,a,1]=video[y+b,x+a,1]
                                    sticker[b,a,2]=video[y+b,x+a,2]
                        video[y:y+h,x:x+w]=sticker
                    except:
                        print("Please stand in the middle of the picture")
    if show_sticker==3:
        face_image= video[y_face:y_face+h_face,x_face:x_face+w_face]
        face_image_small=cv2.resize(face_image,[20,20])
        face_image_big=cv2.resize(face_image_small,[w_face,h_face],interpolation=cv2.INTER_NEAREST)

        video[y_face:y_face+h_face,x_face:x_face+w_face]=face_image_big
    if show_sticker==4:
        rows,cols=face_gray.shape
        mid=cols//2
        for j in range(mid):
            video[:,j]=video[:,cols-j-1]
    result.write(video)
    cv2.imshow(" ",video)
    key=cv2.waitKey(15) & 0xFF
    if key==ord('1'):
        show_sticker=1
    elif  key==ord('2'):
        show_sticker=2
    elif  key==ord('3'):
        show_sticker=3
    elif  key==ord('4'):
        show_sticker=4
    elif key==ord('q'):
        break


cap.release()
result.release()
    
# Closes all the frames
cv2.destroyAllWindows()
