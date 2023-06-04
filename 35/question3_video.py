import cv2
from time import time
import mediapipe as mp
import matplotlib.pyplot as plt

mp_pose=mp.solutions.pose

pose=mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.3, model_complexity=2)

mp_drawing=mp.solutions.drawing_utils







def detectPose(image, pose, display=True):

    output_image= image.copy()

    imageRGB=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

    results= pose.process(imageRGB)

    height,width,_=image.shape

    landmarks=[]

    if results.pose_landmarks:

        mp_drawing.draw_landmarks(image=output_image,
                                landmark_list=results.pose_landmarks,
                                connections=mp_pose.POSE_CONNECTIONS)
        for landmark in results.pose_landmarks.landmark:
            landmarks.append((int(landmark.x*width),int(landmark.y*height),
                              int(landmark.z*width)))
            
    if display:

        plt.figure(figsize=[22,22])
        plt.subplot(121);plt.imshow(image[:,:,::-1]);plt.title("Original Image");plt.axis("off");
        plt.subplot(122);plt.imshow(output_image[:,:,::-1]);plt.title("Output Image");plt.axis("off")

        mp_drawing.plot_landmarks(results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)

    else:

        return output_image, landmarks
    


pose_video = mp_pose.Pose(static_image_mode=False,min_detection_confidence=0.5,model_complexity=1)
url='http://192.168.231.105:8080/video'
video = cv2.VideoCapture(url)
_,frame = video.read()

video.set(3,1280)
video.set(4,960)

frame=cv2.flip(frame,1)
frame=cv2.rotate(frame,cv2.ROTATE_90_COUNTERCLOCKWISE)
width= frame.shape[0]
height= frame.shape[1]
writer1= cv2.VideoWriter("output/MY_pose_detection.avi",cv2.VideoWriter_fourcc(*'MJPG'),30, (640,int(width*(640/height))))
while video.isOpened():

    ok,frame = video.read()

    if not ok:
        break

    frame=cv2.flip(frame,1)
    frame=cv2.rotate(frame,cv2.ROTATE_90_COUNTERCLOCKWISE)
    frame_width,frame_height, _=frame.shape

    frame= cv2.resize(frame, (640,int(frame_width*(640/frame_height))))

    frame, _ = detectPose(frame,pose_video, display=False)

    writer1.write(frame)
    cv2.imshow("MY_pose_detection",frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()