import numpy as np
import cv2

from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel



def put_on_face(face_part,image_in,Fruit,offset_x,offset_y,close):
    scale=2
    face_part = np.array(face_part,dtype=int)

    x,y,w,h= cv2.boundingRect(face_part)
    if close==1:
        x_l,y_l,w_l,h_l= cv2.boundingRect(face_part)
        offset_x=x_l+w_l//2
        offset_y=y_l-2*h_l

    mask=np.zeros(image_in.shape,dtype=np.uint8)
    # print(image_in.shape)
    cv2.drawContours(mask,[face_part],-1,(255,255,255),-1)

    mask=mask//255   #age 2ta / nazarim float mishavad va imshow sefid mishavad
    result= image_in*mask
    result= result[y:y+h,x:x+w]
    result_big=cv2.resize(result,(0,0),fx=scale,fy=scale)
    Fruit= cv2.resize(Fruit,(image_in.shape[1],image_in.shape[0]))
    if close==0:
        x=offset_x-3*w//2
        y=offset_y
    if close==2:
        x=offset_x+w//2
        y=offset_y
    for i in range(w*scale):
        for j in range(h*scale):
            if result_big[j,i,0]==0 and result_big[j,i,1]==0 and result_big[j,i,2]==0:
                result_big[j,i]=Fruit[y-int(((scale-1)/2)*h)+j,x-int(((scale-1)/2)*w)+i]
    Fruit[y-int(((scale-1)/2)*h):y-int(((scale-1)/2)*h)+scale*h,x-int(((scale-1)/2)*w):x-int(((scale-1)/2)*w)+scale*w]=result_big
    


    return Fruit,offset_x,offset_y



fd = UltraLightFaceDetecion("weights/RFB-320.tflite",conf_threshold=0.88)
fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")
image=cv2.imread("input/javad.jpg")
orange=cv2.imread("input/orange.jpg")
apple=cv2.imread("input/apple.jpg")
carrot=cv2.imread("input/carrot.jpg")
# cap = cv2.VideoCapture("video.mp4")
# color = (0, 0, 125)


boxes, scores = fd.inference(image)
lip_mark=[]
left_eye=[]
right_eye=[]
lip_mark_index=[52,55,56,53,59,58,61,68,67,71,63,64]
left_eye_index=[35,36,33,37,39,42,40,41]
right_eye_index=[89,90,87,91,93,96,94,95]
for pred in fa.get_landmarks(image, boxes):
    # for i,p in enumerate(np.round(pred).astype(np.int)):
    #     cv2.circle(image, tuple(p), 2, color, -1, cv2.LINE_AA)
    #     cv2.putText(image,str(i),tuple(p),cv2.FONT_HERSHEY_TRIPLEX,0.6,(0,255,0))

    for i in lip_mark_index:
        lip_mark.append(pred[i])
    for i in left_eye_index:
        left_eye.append(pred[i])
    for i in right_eye_index:
        right_eye.append(pred[i])

fruit_face,x,y=put_on_face(lip_mark,image,apple,0,0,1)
print(x,y)
fruit_face,x,y=put_on_face(left_eye,image,fruit_face,x,y,0)
fruit_face,x,y=put_on_face(right_eye,image,fruit_face,x,y,2)


image1=cv2.resize(image,(800,800))
cv2.imwrite("output/apple.jpg",fruit_face)
cv2.imshow("result", fruit_face)
cv2.waitKey()