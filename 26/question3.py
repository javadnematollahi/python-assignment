import cv2
import numpy as np

angry_image=cv2.imread('angry.png')
angry_image_WB=cv2.cvtColor(angry_image,cv2.COLOR_BGR2GRAY)
print(f"input_size={angry_image_WB.shape}")
def rotate_90(image):
    image_size=image.shape
    image_rotated=np.zeros((image_size[1],image_size[0]),dtype=np.uint8)
    for i in range(image_size[0]):
        for j in range(image_size[1]):
            image_rotated[image_size[1]-j-1,i]=image[i,j]
    return image_rotated

def rotate_180(image):
    image_rotate_90=rotate_90(image)
    image_rotate_180=rotate_90(image_rotate_90)
    print(f"output_size={image_rotate_180.shape}")
    cv2.imshow("180_degree_rotated",image_rotate_180)
    cv2.waitKey()
    # cv2.imwrite('image_rotated_180.png',image_rotate_180)


rotate_180(angry_image_WB)