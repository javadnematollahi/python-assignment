import random
import numpy as np
import cv2
 

cap = cv2.VideoCapture('input/cars.mp4')
# Randomly select 25 frames
# frameIds = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=25)
 
 
totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(totalFrames)
frames = []
count_frame=0
while True:
    randomFrameNumber=random.randint(0, totalFrames)
    cap.set(cv2.CAP_PROP_POS_FRAMES,randomFrameNumber)
    success, frame = cap.read()
    if success:
        count_frame+=1
        # print(count_frame)
        frames.append(frame)
    if count_frame==30:
        break
 
medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)  
 
cv2.imwrite("output/road_without_car.jpg",medianFrame)
cv2.imshow('frame', medianFrame)
cv2.waitKey(0)