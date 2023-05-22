import cv2

image=cv2.imread("input/javad.jpg",0)

inverted= 255 -image

blurred = cv2.GaussianBlur(inverted,(21,21),0)

inverted_blurred = 255 - blurred

sketch= image / inverted_blurred

sketch= sketch *255


cv2.imwrite('output/result_blurred.jpg' , sketch)