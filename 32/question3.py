import numpy as np 
import cv2
import matplotlib.pyplot as plt

rural=cv2.imread("input/rural.jpg",cv2.IMREAD_GRAYSCALE)
city=cv2.imread("input/city.jpg",cv2.IMREAD_GRAYSCALE)
room=cv2.imread("input/room.png",cv2.IMREAD_GRAYSCALE)

rural_H_c=cv2.equalizeHist(rural)
# hist=cv2.calcHist([image],[0],None,[256],[0,256])

cv2.imwrite("output/rural_H_c.jpg",rural_H_c)
# plt.plot(hist)
# plt.show()

city_H_c=cv2.equalizeHist(city)
# hist=cv2.calcHist([image],[0],None,[256],[0,256])

cv2.imwrite("output/city_H_c.jpg",city_H_c)

# hist=cv2.calcHist([room],[0],None,[256],[0,256])
# plt.plot(hist)
# plt.show()
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
room_H_c = clahe.apply(room)
# room_H_c=cv2.equalizeHist(room)
# hist=cv2.calcHist([room_H_c],[0],None,[256],[0,256])

cv2.imwrite("output/room_H_c.jpg",room_H_c)
# plt.plot(hist)
# plt.show()