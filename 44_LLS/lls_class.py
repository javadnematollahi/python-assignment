import numpy as np
import matplotlib.pyplot as plt

class LLS:
    def __init__(self):
        ...

    def fit(self,X,Y):
        self.X_train=X
        self.Y_train=Y
        self.w=np.matmul(np.matmul(np.linalg.inv(np.matmul(self.X_train.T , self.X_train)), self.X_train.T), self.Y_train)

        return self.w

    def predict(self,X):
        Y=[]
        for x in X:
            y=x*self.w
            Y.append(y)
        return Y
    
    # def evaluate(self,X_in,Y_in):
    #     Y_pred=self.predict(X_in)
    #     accuracy= np.sum(Y_pred ==Y_in)/(len(Y_in))
    #     return accuracy
