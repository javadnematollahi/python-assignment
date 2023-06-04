import cv2
import numpy as np 

class Encrypt:
    def __init__(self,image):
        self.image=image


    def encrypt(self):

        B,G,R=cv2.split(self.image)

        password = np.random.randint(0, 256, (self.image.shape[0], self.image.shape[1]), dtype=np.uint8) 
        cv2.imwrite("output\password.jpg", password)   

        b_encrypt = cv2.bitwise_xor(B, password)  
        g_encrypt = cv2.bitwise_xor(G, password)  
        r_encrypt = cv2.bitwise_xor(R, password)  
        encrypte_image=cv2.merge((b_encrypt,g_encrypt,r_encrypt))
        cv2.imwrite("output\encrypte_image.jpg",encrypte_image)

        return encrypte_image,password