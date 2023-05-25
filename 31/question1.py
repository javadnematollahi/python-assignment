import numpy as np 
import cv2
import matplotlib.pyplot as plt

image=cv2.imread("input/home.png",cv2.IMREAD_GRAYSCALE)
rows,cols=image.shape
dict_hist=dict()


for k in range(256):
    dict_hist[k] = np.count_nonzero(image == k)

list_value=list(dict_hist.values())
list_index=list(dict_hist.keys())

plt.plot(list_value)
plt.savefig("output/homeplot.png")
plt.show()
plt.hist(list_value)
plt.savefig("output/homehist.png")
plt.show()
plt.bar(list_index,list_value, color ='maroon',width = 0.4)
plt.savefig("output/homebar.png")
plt.show()