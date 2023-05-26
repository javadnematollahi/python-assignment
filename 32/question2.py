import numpy as np 
import cv2
import matplotlib.pyplot as plt
body=cv2.imread("input/body.png",cv2.IMREAD_GRAYSCALE)
elec=cv2.imread("input/elec.png",cv2.IMREAD_GRAYSCALE)
circle=cv2.imread("input/circle.png",cv2.IMREAD_GRAYSCALE)
party=cv2.imread("input/party.png")
woman=cv2.imread("input/woman.png")
things=cv2.imread("input/things.png",cv2.IMREAD_GRAYSCALE)


for i in range(5):
    body=cv2.medianBlur(body,3)

for i in range(2):
    elec=cv2.medianBlur(elec,3)

for i in range(2):
    circle=cv2.medianBlur(circle,3)

for i in range(5):
    party=cv2.medianBlur(party,3)

for i in range(4):
    woman=cv2.medianBlur(woman,5)
for i in range(3):
    woman=cv2.medianBlur(woman,7)

for i in range(7):
    things=cv2.medianBlur(things,3)



cv2.imshow("",body)
cv2.waitKey()
cv2.imshow("",elec)
cv2.waitKey()
cv2.imshow("",circle)
cv2.waitKey()
cv2.imshow("",party)
cv2.waitKey()
cv2.imshow("",woman)
cv2.waitKey()
cv2.imshow("",things)
cv2.waitKey()

cv2.imwrite("output/body.jpg",body)
cv2.imwrite("output/elec.jpg",elec)
cv2.imwrite("output/circle.jpg",circle)
cv2.imwrite("output/party.jpg",party)
cv2.imwrite("output/woman.jpg",woman)
cv2.imwrite("output/things.jpg",things)