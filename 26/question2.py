import cv2

man_picture=cv2.imread('man.png')
woman_picture=cv2.imread('woman.png')

man_picture_size=man_picture.shape
woman_picture_size=woman_picture.shape

for i in range(man_picture_size[0]):
    for j in range(man_picture_size[1]):
        man_picture[i,j]=255-man_picture[i,j]

for i in range(woman_picture_size[0]):
    for j in range(woman_picture_size[1]):
        woman_picture[i,j]=255-woman_picture[i,j]

cv2.imshow('man_invert',man_picture)
cv2.imshow('woman_invert',woman_picture)
cv2.waitKey()