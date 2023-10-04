import tensorflow as tf
cifar100 = tf.keras.datasets.cifar100

(x_train, y_train),(x_test, y_test) = cifar100.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
print(x_train.shape)
model = tf.keras.models.Sequential([

tf.keras.layers.Flatten(input_shape=(32,32,3)),
tf.keras.layers.Dense(256, activation='relu'),
tf.keras.layers.Dense(128, activation='relu'),
tf.keras.layers.Dropout(0.2),
tf.keras.layers.Dense(100, activation='softmax')
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
loss=tf.keras.losses.sparse_categorical_crossentropy,
metrics=['accuracy'])

model.fit(x_train, y_train, epochs=30)
model.evaluate(x_test, y_test)