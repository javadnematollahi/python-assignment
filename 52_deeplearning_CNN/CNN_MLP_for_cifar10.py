import tensorflow as tf
cifar10 = tf.keras.datasets.cifar10

(x_train, y_train),(x_test, y_test) = cifar10.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
print(x_train.shape)
model = tf.keras.models.Sequential([

tf.keras.layers.Conv2D(32,(3,3),activation='relu',input_shape=(32,32,3)),   #30
tf.keras.layers.Conv2D(64,(3,3),activation='relu'),    #28
tf.keras.layers.MaxPooling2D(),  #14
tf.keras.layers.Conv2D(64,(3,3),activation='relu'), #12
tf.keras.layers.Conv2D(32,(3,3),activation='relu'),  #10
tf.keras.layers.AveragePooling2D(),  #5

tf.keras.layers.Flatten(),
tf.keras.layers.Dense(256, activation='relu'),
tf.keras.layers.Dense(128, activation='relu'),
tf.keras.layers.Dropout(0.2),
tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
loss=tf.keras.losses.sparse_categorical_crossentropy,
metrics=['accuracy'])

model.fit(x_train, y_train, epochs=15)
model.evaluate(x_test, y_test)