import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageFont, ImageDraw, Image 

microsoft= cv2.imread("input/microsoft.png")
microsoft=cv2.cvtColor(microsoft,cv2.COLOR_BGR2RGB)

microguid= cv2.imread("input/microguid.png")
microguid=cv2.cvtColor(microguid,cv2.COLOR_BGR2RGB)
microsoft=cv2.resize(microsoft,(689,310))
print(microsoft.shape[0],microsoft.shape[1])

print(microguid.shape[0],microguid.shape[1])


for i in range(microguid.shape[0]):
    for j in range(microguid.shape[1]):
        if i<152 and i>101 and j>101 and j<152:
            microguid[i,j,0]=242;microguid[i,j,1]=80;microguid[i,j,2]=34
        elif i<206 and i>155 and j>101 and j<152:
            microguid[i,j,0]=127;microguid[i,j,1]=186;microguid[i,j,2]=0
        elif i<206 and i>155 and j>155 and j<206:
            microguid[i,j,0]=255;microguid[i,j,1]=185;microguid[i,j,2]=0
        elif i<152 and i>101 and j>155 and j<206:
            microguid[i,j,0]=0;microguid[i,j,1]=164;microguid[i,j,2]=239
        elif i<149 and i>139 and j>565 and j<570:
            microguid[i,j,0]=255;microguid[i,j,1]=255;microguid[i,j,2]=255
        else:
            microguid[i,j,0]=87;microguid[i,j,1]=83;microguid[i,j,2]=82


my_microsoft = Image.fromarray(microguid)  
draw = ImageDraw.Draw(my_microsoft)  
# use a truetype font  
font = ImageFont.truetype("input/segoeuib.ttf", 82)  

draw.text((228,92), "Microsoft", font=font)  



plt.imshow(microsoft,cmap="gray")
plt.show()
plt.imshow(my_microsoft,cmap="gray")
plt.show()

convert=cv2.cvtColor(np.array(my_microsoft),cv2.COLOR_RGB2BGR)
cv2.imwrite("output/my_microsoft.jpg",convert)