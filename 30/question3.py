import math
from mtcnn import MTCNN
from PIL import Image
import numpy as np
import cv2


def EuclideanDistance(source_representation, test_representation):
    euclidean_distance = source_representation - test_representation
    euclidean_distance = np.sum(np.multiply(euclidean_distance, euclidean_distance))
    euclidean_distance = np.sqrt(euclidean_distance)
    return euclidean_distance

def alignment_procedure(img, left_eye, right_eye):

    #this function aligns given face in img based on left and right eye coordinates

    left_eye_x, left_eye_y = left_eye
    right_eye_x, right_eye_y = right_eye

    #-----------------------
    #find rotation direction

    if left_eye_y > right_eye_y:
        point_3rd = (right_eye_x, left_eye_y)
        direction = -1 #rotate same direction to clock
    else:
        point_3rd = (left_eye_x, right_eye_y)
        direction = 1 #rotate inverse direction of clock

    #-----------------------
    #find length of triangle edges

    # a = EuclideanDistance(np.array(left_eye), np.array(point_3rd))
    b = EuclideanDistance(np.array(right_eye), np.array(point_3rd))
    c = EuclideanDistance(np.array(right_eye), np.array(left_eye))

    #-----------------------

    #apply cosine rule

    # if b != 0 and c != 0: #this multiplication causes division by zero in cos_a calculation

        # cos_a = (b*b + c*c - a*a)/(2*b*c)
    cos_a = b/c
    angle = np.arccos(cos_a) #angle in radian
    angle = (angle * 180) / math.pi #radian to degree

    #-----------------------
    #rotate base image

    if direction == -1:
        angle = 90 - angle

    img = Image.fromarray(img)
    img = np.array(img.rotate(direction * angle))

    return img #return img anyway

image=cv2.imread("input/javad1.jpg")
img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
detector = MTCNN()
box=detector.detect_faces(img)

detection = box[0]
keypoints = detection["keypoints"]
left_eye = keypoints["left_eye"]
right_eye = keypoints["right_eye"]

img = alignment_procedure(image, left_eye, right_eye)

cv2.imwrite("output/rotate_face.jpg",img)
cv2.imshow("",img)
cv2.waitKey()





