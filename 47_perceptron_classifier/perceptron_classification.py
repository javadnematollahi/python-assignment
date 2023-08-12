import numpy as np
from tqdm import tqdm


class Perceptron:
    def __init__(self, input_length, learning_rate):
        self.W = np.random.rand(input_length)
        self.b = np.random.rand(1)
        self.learning_rate = learning_rate
    
    def activation(self, x, function):
        if function == "sigmoid":
            return 1 / (1 + np.exp(-x))
        elif function == "relu":
            return np.maximum(0, x)
        elif function == "tanh":
            return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
        elif function == "unitstep":
            if x>0:
                return 1
            elif x==0:
                return 0.5
            elif x<0:
                return 0
        elif function == "sign":
            if x>0:
                return 1
            elif x==0:
                return 0
            elif x<0:
                return -1
        elif function == "piece-wise-linear":
            if x>0.5:
                return 1
            elif -0.5<=x<=0.5:
                return x+0.5
            elif x<=-0.5:
                return 0
        else:
            raise Exception("Not supported activation function")

    def forward(self, x,activation_func):
        return self.activation(x @ self.W + self.b,activation_func)
    
    def back_propagation(self, x_train, y_train, y_pred):
        dW = (y_pred - y_train) * x_train
        db = (y_pred - y_train)
        return dW, db
    
    def update(self, dW, db):
        self.W = self.W - self.learning_rate * dW
        self.b = self.b - self.learning_rate * db

    def fit(self, X_train, Y_train, epochs,func):
        for epoch in tqdm(range(epochs)):
            for x_train, y_train in zip(X_train, Y_train):
                y_pred = self.forward(x_train,func)
                dW, db = self.back_propagation(x_train, y_train, y_pred)
                self.update(dW, db)

    def predict(self, X_test,func):
        Y_pred = []
        for x_test in X_test:
            y_pred = self.forward(x_test,func)
            Y_pred.append(y_pred)
        return np.array(Y_pred)
    
    def calc_loss(self, X_test, Y_test,func, metric='mse'):
        y_pred = self.predict(X_test,func)
        if metric == 'mse':
            loss = np.mean((y_pred - Y_test) ** 2)
        elif metric == 'mae':
            loss = np.mean(np.abs(y_pred - Y_test))
        else:
            raise Exception('Not supported metric')
        return loss
    
    def calc_accuracy(self, X_test, Y_test,func):
        Y_pred = self.predict(X_test,func)
        Y_pred=Y_pred.reshape(-1)
        if func=="sigmoid":
            Y_pred=np.where(Y_pred>0.5,1,0)
        elif func=="relu":
            Y_pred=np.where(Y_pred>0,1,0)
        elif func=="tanh":
            Y_pred=np.where(Y_pred>0,1,0)
        elif func=="unitstep":
            Y_pred=np.where(Y_pred>0.5,1,0)
        elif func=="sign":
            Y_pred=np.where(Y_pred>0,1,0)
        elif func=="piece-wise-linear":
            Y_pred=np.where(Y_pred>0.5,1,0)
        else:
            raise Exception("Not supported activation function")
        accuracy = np.mean(Y_pred == Y_test)
        return accuracy

    def evaluate(self, X_test, Y_test,func):
        loss = self.calc_loss(X_test, Y_test,func)
        accuracy = self.calc_accuracy(X_test, Y_test,func)
        return loss, accuracy