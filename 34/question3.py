import cv2
import numpy as np
import matplotlib.pyplot as plt

image= cv2.imread("input/watermelon.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

image=cv2.resize(image,(1200,1000))
main_image=image.copy()
print(image.shape[0],image.shape[1])

r,g,b=cv2.split(image)
for i in range(g.shape[0]):
    for j in range(g.shape[1]):
        if g[i,j]<150 and g[i,j]>20 and r[i,j]<95 and b[i,j]<35:   #135   70    30
            if g[i,j]*2>255:
                g[i,j]=255
            else:
                g[i,j]=g[i,j]*2
        if g[i,j]<180 and g[i,j]>100 and r[i,j]<155 and r[i,j]>50 and b[i,j]<135 and b[i,j]>10:   
            if g[i,j]*1.6>255:
                g[i,j]=255
            else:
                g[i,j]=g[i,j]*1.6
        if g[i,j]<226 and g[i,j]>170 and r[i,j]<215 and r[i,j]>140 and b[i,j]<195 and b[i,j]>35:   
            if g[i,j]*1.25>255:
                g[i,j]=255
            else:
                g[i,j]=g[i,j]*1.25
            r[i,j]=r[i,j]*0.8
            if b[i,j]*1.6>255:
                b[i,j]=250
            else:
                b[i,j]=b[i,j]*1.6

r=r.astype(np.uint8)
g=g.astype(np.uint8)
b=b.astype(np.uint8)
materwelon=cv2.merge((g,r,b))
# cv2.putText(materwelon,f"Materwelon",(40,30),cv2.FONT_HERSHEY_SIMPLEX,0.75,255,2)

text_image=np.zeros((materwelon.shape))
cv2.putText(text_image, 'Materwelon', (100,900), cv2.FONT_HERSHEY_COMPLEX,4,(74,74,74),4)
# Rotate the image using cv2.warpAffine()
M = cv2.getRotationMatrix2D( (100,900), 90, 1)
out_mater = cv2.warpAffine(text_image, M, (text_image.shape[1], text_image.shape[0]))
materwelon=np.add(out_mater,materwelon)
materwelon=materwelon.astype(np.uint8)

text_image=np.zeros((main_image.shape))
cv2.putText(text_image, 'Watermelon', (100,900), cv2.FONT_HERSHEY_COMPLEX,4,(74,74,74),4)
# Rotate the image using cv2.warpAffine()
M = cv2.getRotationMatrix2D( (100,900), 90, 1)
out_main = cv2.warpAffine(text_image, M, (text_image.shape[1], text_image.shape[0]))
main_image=np.add(out_main,main_image)
main_image=main_image.astype(np.uint8)

convert=np.hstack((main_image,materwelon))
convert=cv2.cvtColor(convert,cv2.COLOR_RGB2BGR)
cv2.imwrite("output/convert_watermelon.jpg",convert)
convert=cv2.cvtColor(convert,cv2.COLOR_BGR2RGB)
plt.imshow(convert,cmap="gray")
plt.show()


