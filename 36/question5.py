import cv2
import numpy as np
import matplotlib.pyplot as plt

superman=cv2.imread("input/superman.jpg")
city=cv2.imread("input/city.jpg")
city=cv2.resize(city,(superman.shape[1],superman.shape[0]))
# print(city.shape);print(superman.shape)

superman_hsv=cv2.cvtColor(superman,cv2.COLOR_BGR2HSV)
city=cv2.cvtColor(city,cv2.COLOR_BGR2HSV)


lower = np.array([30, 30, 80], dtype = "uint8")
upper = np.array([75, 255, 255], dtype = "uint8")

lower1 = np.array([45, 30, 80], dtype = "uint8")
upper1= np.array([75, 255, 255], dtype = "uint8")

Mask = cv2.inRange(superman_hsv, lower, upper)
Mask=Mask.astype(dtype=np.uint8)
# print(Mask.shape)
detect_noise=superman_hsv[295:870,530:1250]
detect_noise_mask = cv2.inRange(detect_noise, lower1, upper1)

Mask[295:870,530:1250]=detect_noise_mask

Mask1=np.where(Mask>250,0,255)
Mask1=Mask1.astype(dtype=np.uint8)

city_alone = cv2.bitwise_and(city, city, mask = Mask)

superman_alone = cv2.bitwise_and(superman_hsv, superman_hsv, mask = Mask1)

superman_alone= cv2.cvtColor(superman_alone,cv2.COLOR_HSV2RGB)
city_alone= cv2.cvtColor(city_alone,cv2.COLOR_HSV2RGB)
final=np.add(superman_alone,city_alone)


plt.imshow(final,cmap="gray")
plt.savefig("output/s_in_city.jpg")
plt.show()
