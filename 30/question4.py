import numpy as np
import cv2


from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel



def zoom_effect(landmark,image_in):
    scale=2
    landmark = np.array(landmark,dtype=int)
    # print(lip_mark)

    x,y,w,h= cv2.boundingRect(landmark)
    mask=np.zeros(image_in.shape,dtype=np.uint8)

    cv2.drawContours(mask,[landmark],-1,(255,255,255),-1)
    mask=mask//255   #age 2ta / nazarim float mishavad va imshow sefid mishavad


    result= image_in*mask
    result= result[y:y+h,x:x+w]
    result_big=cv2.resize(result,(0,0),fx=scale,fy=scale)
    for i in range(w*scale):
        for j in range(h*scale):
            if result_big[j,i,0]==0 and result_big[j,i,1]==0 and result_big[j,i,2]==0:
                result_big[j,i]=image_in[y-int(((scale-1)/2)*h)+j,x-int(((scale-1)/2)*w)+i]
    image_in[y-int(((scale-1)/2)*h):y-int(((scale-1)/2)*h)+scale*h,x-int(((scale-1)/2)*w):x-int(((scale-1)/2)*w)+scale*w]=result_big

    return image_in



fd = UltraLightFaceDetecion("weights/RFB-320.tflite",conf_threshold=0.88)
fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")
image=cv2.imread("input/javad.png")
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
    lip=zoom_effect(lip_mark,image)
    l_eye=zoom_effect(left_eye,lip)
    final=zoom_effect(right_eye,l_eye)





image1=cv2.resize(final,(600,800))
cv2.imwrite("output/Big_eye_lips.jpg",image1)
cv2.imshow("result", image1)
cv2.waitKey()
 


