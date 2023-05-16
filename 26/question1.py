import cv2
import numpy as np

chess_board=np.zeros((512,512),np.uint8)

size_chess=chess_board.shape

for i in range(4):
    for j in range(4):
        chess_board[i*128:64*((i*2)+1),j*128:64*((j*2)+1)]=255
        chess_board[(2*i+1)*64:128*(i+1),(2*j+1)*64:128*(j+1)]=255


cv2.imshow(f'{55*" "}Chess Board',chess_board)
cv2.waitKey()