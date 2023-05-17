import cv2
import numpy as np
import imageio
import time

image=cv2.imread('tv.jpg')
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
a,b=image.shape
fps = 60
size=(b,a)
i=0
writer= cv2.VideoWriter("TV.avi",cv2.VideoWriter_fourcc(*'MJPG'),fps, size,0)
while True:

    my_image=np.random.random((134,178))*255
    my_image=np.array(my_image, dtype=np.uint8)
    image[18:152,21:199]=my_image
    writer.write(image)

    i+=1
    if i==100:
        i=0
        break
    
    # cv2.imshow(" ",image)
    # if cv2.waitKey(25) & 0xFF == ord('q'):
    #     break


writer.release()
cv2.destroyAllWindows()
# time.sleep(5)
cap = cv2.VideoCapture('TV.avi')
image_lst = []
 
while True:
    ret, frame = cap.read()
    image_lst.append(frame)

    i+=1
    if i==70:
        i=0
        break

    cv2.imshow('a', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
 
# Convert to gif using the imageio.mimsave method
imageio.mimsave('TV.gif', image_lst, fps=60)









######    why below code doesn't work??????????

# import cv2
# import numpy as np
# import imageio

# image=cv2.imread('tv.jpg')
# image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# a,b=image.shape
# image_list = []
# i=0

# while True:

#     my_image=np.random.random((134,178))*255
#     my_image=np.array(my_image, dtype=np.uint8)

#     image[18:152,21:199]=my_image

#     image_list.append(image)
#     print((image))

#     i+=1
#     if i==120:
#         break
#     cv2.imshow(" ",image)

#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break

# cv2.destroyAllWindows()

# imageio.mimsave('TV.gif', image_list, fps=60)

