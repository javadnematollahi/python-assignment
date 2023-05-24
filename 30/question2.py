import numpy as np
import cv2

from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel
from SolvePnPHeadPoseEstimation import HeadPoseEstimator

def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

def put_on_face(face_part,image_in):

    face_part = np.array(face_part,dtype=int)

    x,y,w,h= cv2.boundingRect(face_part)

    mask=np.zeros(image_in.shape,dtype=np.uint8)
    # print(image_in.shape)
    cv2.drawContours(mask,[face_part],-1,(255,255,255),-1)

    mask=mask//255   #age 2ta / nazarim float mishavad va imshow sefid mishavad
    result= image_in*mask
    result= result[y:y+h,x:x+w]
    # result_big=cv2.resize(result,(0,0),fx=1,fy=1)

    for i in range(w):
        for j in range(h):
            if result[j,i,0]==0 and result[j,i,1]==0 and result[j,i,2]==0:
                result[j,i]=image_in[y+h-j,x+i]
    for i in range(w):
        for j in range(h):
            image_in[y+j,x+i]=result[h-j-1,i]
    
    return image_in



image=cv2.imread("input/javad.jpg")
fd = UltraLightFaceDetecion("weights/RFB-320.tflite",conf_threshold=0.88)
fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")
hp = HeadPoseEstimator("weights/head_pose_object_points.npy",image.shape[1], image.shape[0])

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

    face_center = np.mean(pred, axis=0)
    euler_angle = hp.get_head_pose(pred).flatten()

    print(int(euler_angle[2]))
    image=rotate_image(image,int(euler_angle[2]))
boxes, scores = fd.inference(image)
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



image=put_on_face(lip_mark,image)
image=put_on_face(left_eye,image)
final=put_on_face(right_eye,image)

final=cv2.rotate(final,cv2.ROTATE_180)


image1=cv2.resize(image,(800,800))
cv2.imwrite("output/odd_face.jpg",final)
cv2.imshow("result", final)
cv2.waitKey()
