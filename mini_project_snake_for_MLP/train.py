import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder


X = pd.read_csv('dataset/input_data.csv')
y = pd.read_csv('dataset/output_data.csv')
enc = OneHotEncoder()
enc.fit(y)
onehotlabels = enc.transform(y).toarray()
labels = pd.DataFrame(onehotlabels)
X = X.drop(['last_up', 'last_down', 'last_right', 'last_left'], axis=1)
X.shape, y.shape
print(len(X.columns))
print(len(X))
X.head()
X_train, X_test, Y_train, Y_test=train_test_split(X,labels,test_size=0.1)

model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(16, activation=tf.keras.activations.relu),  #  input layer
  tf.keras.layers.Dense(80, activation=tf.keras.activations.relu),
  tf.keras.layers.Dense(64, activation=tf.keras.activations.relu),
  tf.keras.layers.Dense(48, activation=tf.keras.activations.sigmoid), 
  tf.keras.layers.Dense(4, activation='softmax')     # output layer
])

model.compile(optimizer=tf.keras.optimizers.AdamW(learning_rate=0.0001),
              loss=tf.keras.losses.binary_crossentropy,
              metrics=['accuracy'])

output = model.fit(X_train, Y_train, epochs=2000)
loss,accuracy  =model.evaluate(X_test, Y_test)
model.save("weights/MLP_FOR_Snake.h5")
print(f'loss: {loss}, accuracy: {accuracy}')
plt.plot(output.history["loss"], label='loss')
plt.plot(output.history["accuracy"], label='accuracy')
plt.title("train loss and accuracy")
plt.xlabel("epochs")
plt.ylabel("loss")
plt.legend()
plt.show()
