import numpy as np
from tqdm import tqdm


class Mlp:
    def __init__(self,D_in,H1,H2,D_out,epochs,η,func1,func2,func_out):
        self.input=D_in
        self.H1=H1
        self.H2= H2
        self.output=D_out
        self.epochs=epochs
        self.η=η
        self.func1=func1
        self.func2=func2
        self.func_out=func_out

        self.W1=np.random.randn(self.input,self.H1)
        self.W2=np.random.randn(self.H1,self.H2)
        self.W3=np.random.randn(self.H2,self.output)

        self.B1=np.random.randn(1,self.H1)
        self.B2=np.random.randn(1,self.H2)
        self.B3=np.random.randn(1,self.output)



    def activation(self,method,x):
        if method == "sigmoid":
            return 1/(1 + np.exp(-x))
        
        if method == "softmax":
            return np.exp(x)/np.sum(np.exp(x))


    def forward(self, x):
        #forward

        # layer1
        out1 = self.activation(self.func1,x.T @ self.W1 + self.B1)

        # layer2

        out2 = self.activation(self.func2,out1 @ self.W2 + self.B2)

        # layer3
        out3 = self.activation(self.func_out,out2 @ self.W3 + self.B3)

        return out3,out2,out1

    def back_propagation(self, out3, out2, out1,x_train,y_train):
        # backward - we should calculate moshtaq

        # layer3
        error = -2 * (y_train - out3)
        grad_B3 = error
        grad_W3 = out2.T @ error

        # layer2
        error = error @ self.W3.T * out2 * (1 - out2)
        grad_B2 = error
        grad_W2 = out1.T @ error

        # layer1
        error = error @ self.W2.T * out1 * (1 - out1)
        grad_B1 = error
        grad_W1 =  x_train @error

        return grad_B1,grad_B2,grad_B3,grad_W1,grad_W2,grad_W3

    def update(self, grad_B1,grad_B2,grad_B3,grad_W1,grad_W2,grad_W3):
        #layer1
        self.W1 -= self.η * grad_W1
        self.B1 -= self.η * grad_B1

        #layer2
        self.W2 -= self.η * grad_W2
        self.B2 -= self.η * grad_B2


        #layer3
        self.W3 -= self.η * grad_W3
        self.B3 -= self.η * grad_B3


    def fit(self, X_train, Y_train):
        LOSSES=[]
        ACCURACYES=[]
        for epoch in tqdm(range(self.epochs)):
            Y_PRED=[]
            # train
            for x , y in zip(X_train,Y_train):

                x = x.reshape(-1,1)

                # forward
                out3,out2,out1 = self.forward(x)
                Y_pred=out3
                Y_PRED.append(Y_pred)

                # backward
                grad_B1,grad_B2,grad_B3,grad_W1,grad_W2,grad_W3=self.back_propagation( out3, out2, out1,x,y)
                
                # update
                self.update( grad_B1,grad_B2,grad_B3,grad_W1,grad_W2,grad_W3)
            l,a=self.evaluate(X_train,Y_train)
            LOSSES.append(l)
            ACCURACYES.append(a)
        return LOSSES,ACCURACYES


    def predict(self, X_test):
        Y_PRED=[]
        for x in X_test:
            x = x.reshape(-1,1)

            # forward
            out3,_,_ = self.forward(x)
            Y_pred=out3
            Y_PRED.append(Y_pred)
        Y_PRED = np.array(Y_PRED).reshape(-1,self.output)
        return Y_PRED

    def calc_loss(self, Y_pred, Y_test, metric='mse'):
        
        if metric == 'mse':
            loss = np.mean((Y_pred - Y_test) ** 2)

        elif metric == 'mae':
            loss = np.mean(np.abs(Y_pred - Y_test))
        elif metric == 'rmse':
            loss = np.sqrt(np.mean((Y_pred - Y_test) ** 2))
        else:
            raise Exception('Not supported metric')
        return loss


    def calc_accuracy(self, Y_pred, Y_test):

        accuracy = np.sum(np.argmax(Y_test,axis=1)==np.argmax(Y_pred,axis=1))/len(Y_pred)
        return accuracy
    

    def evaluate(self, X_test, Y_test):
        Y_pred = self.predict(X_test)
        loss = self.calc_loss(Y_pred, Y_test)
        accuracy = self.calc_accuracy(Y_pred, Y_test)
        return loss, accuracy

