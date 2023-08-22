import numpy as np
import pandas as pd


class OneHotEncoding:
    def __init__(self):
        pass



    def encode(self,X):
        X=np.array(X)
        self.unique_value=np.unique(X)
        self.unique_value.sort()
        label_number=[]
        self.encode_label=[]
        for i in range(len(self.unique_value)):
            label_number.append(i)
        label_number=np.array(label_number)    
        hotencode=[]
        encode=np.eye(len(self.unique_value))[label_number]
        encode=encode.astype("int")
        for x in X:
            for idx, val in np.ndenumerate(self.unique_value):
                if val == x:
                    hotencode.append(list(encode[idx]))
                    self.encode_label.append(idx[0])
        hotencode=np.array(hotencode)


        return hotencode
    

    def label(self):
        return np.array(self.encode_label)

    def decode(self,X):
        index=np.argmax(X)
        return self.unique_value[index]



if __name__=="__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.datasets import load_digits
    from sklearn.preprocessing import LabelEncoder
    from sklearn.preprocessing import OneHotEncoder

    dataset = load_digits()
    X= dataset.data
    Y=dataset.target


    #  scikitlearn onehotencoder
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(Y)
    print(f"scikitlearn onehotencoder label:\n {integer_encoded}")
    onehot_encoder = OneHotEncoder(sparse_output=False)
    integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
    print(f"scikitlearn onehotencoder:\n {onehot_encoded}")
    inverted = label_encoder.inverse_transform([np.argmax(onehot_encoded[100])])
    print(f"scikitlearn onehotdecoder for sample 100:\n {inverted}")

    #  My OneHotEncoder

    from onehotEncoder import OneHotEncoding


    one_hot=OneHotEncoding()

    X=np.array(Y)
    # this method used to get one ht encode 
    one=one_hot.encode(X)

    # this method used to get label (use this method after encode method)
    labels=one_hot.label()

    # this method used to decode 
    result=one_hot.decode(one[100])


    print(f"My onehotencoder label:\n {labels}")
    print(f"My onehotencoder:\n {one}")
    print(f"My onehotdecoder for sample 100:\n {result}")


