import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from generate_dataset import generate_dataset


generate_dataset()
df = pd.read_csv('dataset/input_data.csv')
df=df.dropna()
X = df.drop(['label','file_name'],axis=1)
y = df['label']
y=y.to_frame()
print(y.head)
enc = OneHotEncoder()
enc.fit(y)
onehotlabels = enc.transform(y).toarray()
labels = pd.DataFrame(onehotlabels)
X_train, X_test, Y_train, Y_test = train_test_split(X,labels,test_size=0.1)
print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)
labels.to_csv('dataset/label.csv', mode = 'a', index = False)

model = tf.keras.models.Sequential([
tf.keras.layers.Dense(512, activation='relu'),
tf.keras.layers.Dense(1000, activation='relu'),
tf.keras.layers.Dense(256, activation='sigmoid'),
tf.keras.layers.Dense(30, activation='softmax')
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              loss=tf.keras.losses.binary_crossentropy,
              metrics=['accuracy'])

model.fit(X_train, Y_train, epochs=50)
model.evaluate(X_test, Y_test)
model.save("weights/face_model.h5")
