import numpy as np
import cv2
import matplotlib.pyplot as plt
from myknn import KNN
from sklearn.model_selection import train_test_split

class FindingDori(KNN):
    def __init__(self, K,path_of_img_test,scale_input_img=0.25):
        super().__init__(K)
        dori= cv2.imread('input/dori.jpg')
        dori=cv2.resize(dori,(0,0),fx=0.25,fy=0.25)
        self.dori_hsv = cv2.cvtColor(dori,cv2.COLOR_BGR2HSV)
        self.dori_rgb = cv2.cvtColor(dori,cv2.COLOR_BGR2RGB)
        self.fit(self.make_train_X(),self.make_train_Y())
        self.scale=scale_input_img
        self.path_of_img_test=path_of_img_test


    def make_train_X(self):
        pixels_list_hsv=self.dori_hsv.reshape(-1,3)
        x_train= pixels_list_hsv / 255
        return x_train


    def make_train_Y(self):
        light_blue = (100,150,0)
        dark_blue = (140,255,255)

        mask_blue=cv2.inRange(self.dori_hsv,light_blue,dark_blue)

        light_yellow=(25, 50, 70)
        dark_yellow=(35, 255, 255)

        mask_yellow=cv2.inRange(self.dori_hsv,light_yellow,dark_yellow)

        light_blued=(210,50,5)
        dark_blued=(250,90,50)

        mask_blued=cv2.inRange(self.dori_hsv,light_blued,dark_blued)

        final_mask=mask_blued+mask_yellow+mask_blue
        # fig,axes=plt.subplots(nrows=1,ncols=3)
        # ax1,ax2,ax3=axes.flatten()

        # ax1.imshow(self.dori_rgb,cmap='gray')
        # ax1.set_title('Train picture')

        # ax2.imshow(final_mask,cmap='gray')
        # ax2.set_title('Dori Mask')

        # final_result=cv2.bitwise_and(self.dori_rgb,self.dori_rgb,mask=final_mask)
        # ax3.imshow(final_result)
        # ax3.set_title('Masked image')

        # plt.show()
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
    finddori=FindingDori(5,"input/doriparents.jpg")
    image_output=finddori.make_predict()
    
    plt.imshow(image_output,cmap='gray')
    plt.savefig("output/doriparents.png")
    plt.show()



