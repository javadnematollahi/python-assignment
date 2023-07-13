import numpy as np
from math import sqrt


class KNN:
    def __init__(self,K):
        self.k=K



    # training
    def fit(self,X,Y):
        self.X_train=X
        self.Y_train=Y

    def euclidean_distance(self,x1,x2):
        return np.sqrt(np.sum((x1-x2)**2))
    
    def predict(self,X_p):
        Y=[]
        for x in X_p:
            distances=[]
            for xtrain in self.X_train:
                d=self.euclidean_distance(x, xtrain)
                distances.append(d)
                
            nearest_neighbors= np.argsort(distances)[0:self.k]
            result = np.bincount(self.Y_train[nearest_neighbors])
            y=np.argmax(result)
            Y.append(y)
        return Y

    def evaluate(self,X_in,Y_in):
        Y_pred=self.predict(X_in)
        accuracy= np.sum(Y_pred ==Y_in)/(len(Y_in))
        return accuracy


