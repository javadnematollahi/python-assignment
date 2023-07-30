import numpy as np


class TTS:
    def __init__(self,X,Y,test_size=0.3):
        self.X=X
        self.Y=Y
        self.test_size=test_size
        self.train_size=1-test_size
        self.split()


    def split(self):
        size_x=len(self.X)
        size_y=len(self.Y)
        if size_x==size_y:
            size_train=round(size_x*self.train_size)
            size_test=size_x-size_train
        else:
            print("The number of X row and Y row must be similar")
            return False

        X_Train=self.X[0:size_train]
        Y_Train=self.Y[0:size_train]
        X_Test=self.X[size_train:size_train+size_test]
        Y_Test=self.Y[size_train:size_train+size_test]

        return X_Train,Y_Train,X_Test,Y_Test
        
        
        





if __name__=="__main__":
    x=np.array([[1,2],[3,4],[5,6],[7,8]])
    y=np.array([[7],[8],[9],[10]])
    tts=TTS(x,y,0.5)
    xt,yt,xte,yte=tts.split()
    print(f'x train :\n {xt}')
    print(f'x test :\n {xte}')
    print(f'y train :\n {yt}')
    print(f'y test :\n {yte}')

        