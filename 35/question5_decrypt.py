import cv2
import numpy as np 

class Decrypt:
    def __init__(self,image,password):
        self.image=image
        self.password=password
    def decrypt(self):
        B,G,R=cv2.split(self.image)

        cv2.imwrite("output\password.jpg", self.password)   

        b_decrypt = cv2.bitwise_xor(B, self.password)  
        g_decrypt = cv2.bitwise_xor(G, self.password)  
        r_decrypt = cv2.bitwise_xor(R, self.password)  
        decrypte_image=cv2.merge((b_decrypt,g_decrypt,r_decrypt))
        cv2.imwrite("output\decrypte_image.jpg",decrypte_image)

        return decrypte_image