import numpy as np
import cv2
import matplotlib.pyplot as plt
from myknn import KNN
from sklearn.model_selection import train_test_split

class FindingNemo(KNN):
    def __init__(self, K,path_of_img_test,scale_input_img=0.25):
        super().__init__(K)
        nemo= cv2.imread('input/nemo.jpg')
        nemo=cv2.resize(nemo,(0,0),fx=0.25,fy=0.25)
        self.nemo_hsv = cv2.cvtColor(nemo,cv2.COLOR_BGR2HSV)
        self.fit(self.make_train_X(),self.make_train_Y())
        self.scale=scale_input_img
        self.path_of_img_test=path_of_img_test


    def make_train_X(self):
        pixels_list_hsv=self.nemo_hsv.reshape(-1,3)
        x_train= pixels_list_hsv / 255
        return x_train


    def make_train_Y(self):
        light_orange=(1,90,200)
        dark_orange=(18,255,255)

        mask_orange=cv2.inRange(self.nemo_hsv,light_orange,dark_orange)

        light_white=(0,0,190)
        dark_white=(145,60,255)

        mask_white=cv2.inRange(self.nemo_hsv,light_white,dark_white)

        light_black=(0,0,0)
        dark_black=(255,250,5)

        mask_black=cv2.inRange(self.nemo_hsv,light_black,dark_black)

        final_mask=mask_black+mask_white+mask_orange
        y_train=final_mask.reshape(-1,)
        return y_train
    
    def make_predict(self):
        test_nemo=cv2.imread(self.path_of_img_test)
        test_nemo=cv2.resize(test_nemo,(0,0),fx=self.scale,fy=self.scale)
        abji_nemo_hsv=cv2.cvtColor(test_nemo,cv2.COLOR_BGR2HSV)
        x_test=abji_nemo_hsv.reshape(-1,3)/255
        y_pred=self.predict(x_test)
        image_output=np.array(y_pred).reshape(test_nemo.shape[:2])
        image_output=image_output.astype('uint8')
        final_result=cv2.bitwise_and(test_nemo,test_nemo,mask=image_output)
        final_result=cv2.cvtColor(final_result,cv2.COLOR_BGR2RGB)
        return final_result
    

if __name__=="__main__":
    findnemo=FindingNemo(5,"input/abji_nemo.jpg")
    image_output=findnemo.make_predict()
    plt.imshow(image_output,cmap='gray')
    plt.savefig("output/abji_nemo.jpg")
    plt.show()



