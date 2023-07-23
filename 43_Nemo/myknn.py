import numpy as np
from math import sqrt
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


class KNN:
    def __init__(self,K):
        self.k=K



    # training
    def fit(self,X,Y):
        self.X_train=X
        self.Y_train=Y

    def euclidean_distance(self,x1,x2):
        return np.sqrt(np.sum((x2-x1)**2,axis=1))
    
    def predict(self,X_p):
        Y=[]
        for x in X_p:
            distances=[]
            distances=self.euclidean_distance(x, self.X_train)

            nearest_neighbors= np.argsort(distances)[0:self.k]
            result = np.bincount(self.Y_train[nearest_neighbors])
            y=np.argmax(result)
            Y.append(y)
        return Y

    def evaluate(self,X_in,Y_in):
        Y_pred=self.predict(X_in)
        accuracy= np.sum(Y_pred ==Y_in)/(len(Y_in))
        return accuracy


if __name__== "__main__":
    iris=load_iris()
    X=iris.data
    Y=iris.target

    X_train, X_test,Y_train, Y_test=train_test_split(X,Y,test_size=0.2)

    print(X_train.shape,Y_train.shape)
    print(X_test.shape,Y_test.shape)


    knn=KNN(3)
    knn.fit(X_train,Y_train)
    accuracy=knn.evaluate(X_test,Y_test)


    knn_skleran=KNeighborsClassifier(3)
    knn_skleran.fit(X_train,Y_train)
    accuracy_sklearn=knn_skleran.score(X_test,Y_test)
    print("accuracy=", accuracy)

    print("accuracy_sklearn=", accuracy_sklearn)