import tensorflow as tf
import numpy as np
import cv2
fashion_mnist = tf.keras.datasets.fashion_mnist
X_train=[]
X_test=[]
(x_train, y_train),(x_test, y_test) = fashion_mnist.load_data()

for i in range(x_train.shape[0]):
  X_train.append(cv2.cvtColor(x_train[i],cv2.COLOR_GRAY2BGR))
for i in range(x_test.shape[0]):
  X_test.append(cv2.cvtColor(x_test[i],cv2.COLOR_GRAY2BGR))

X_test=np.array(X_test)
X_train=np.array(X_train)
x_train, x_test = X_train / 255.0, X_test / 255.0

model = tf.keras.models.Sequential([

tf.keras.layers.Conv2D(25,(3,3),activation='relu',input_shape=(28,28,3)),   #30
tf.keras.layers.Conv2D(30,(3,3),activation='relu'),    #28
tf.keras.layers.MaxPooling2D(),  #14
tf.keras.layers.Conv2D(30,(3,3),activation='relu'), #12
tf.keras.layers.Conv2D(30,(3,3),activation='relu'),  #10
tf.keras.layers.MaxPooling2D(),  #5

tf.keras.layers.Flatten(),
tf.keras.layers.Dense(256, activation='relu'),
tf.keras.layers.Dense(128, activation='relu'),
tf.keras.layers.Dropout(0.2),
tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
loss=tf.keras.losses.sparse_categorical_crossentropy,
metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10)
model.evaluate(x_test, y_test)