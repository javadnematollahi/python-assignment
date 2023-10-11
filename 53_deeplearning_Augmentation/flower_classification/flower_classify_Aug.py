import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

dataset_path = "assets/flower/train"

train_ds = tf.keras.utils.image_dataset_from_directory(
  dataset_path,
  validation_split=0.1,
  subset="training",
  seed=123,
  image_size=(224, 224),
  )

val_ds = tf.keras.utils.image_dataset_from_directory(
  dataset_path,
  validation_split=0.1,
  subset="validation",
  seed=123,
  image_size=(224, 224),
  )

data_augmentation = tf.keras.Sequential(
  [
    layers.RandomFlip("horizontal", input_shape=(224,224,3)),
    layers.RandomRotation(factor=(-0.1,0.1)),
    layers.RandomZoom(0.1),
  ]
)

aug_model = models.Sequential([
    data_augmentation,
    layers.Rescaling(1./255,  input_shape=(224, 224,3)),
    layers.Conv2D(32, 3, strides=2, activation="relu", padding="same"),
    layers.MaxPooling2D(),
    layers.Conv2D(64,3, strides=2, activation="relu", padding="same"),
    layers.MaxPooling2D(),
    layers.Conv2D(128, 3, strides=1, activation="relu"),
    layers.MaxPooling2D(),
    layers.Dropout(0.2),
    layers.Flatten(),
    layers.Dense(256, activation="relu"),
    layers.Dense(17, activation="softmax"),
])

aug_model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate=0.001),
              loss = tf.keras.losses.sparse_categorical_crossentropy,
              metrics = ['accuracy'])

history = aug_model.fit(train_ds, validation_data=val_ds, epochs=20)
aug_model.save('weights/flower_aug.h5')

Y_true = []
Y_pred = []

for images, labels in val_ds:
    for image in images:
        image = np.expand_dims(image, axis=0) 
        prediction=aug_model.predict(image)
        Y_true.append(np.argmax(prediction))

    for label in labels:
        Y_pred.append(label.numpy().tolist())  # append list
print(f'Y_true:  {Y_true}\nY_pred: {Y_pred}')

labels =val_ds.class_names

cm = confusion_matrix(Y_true, Y_pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)

disp.plot(cmap=plt.cm.Blues,xticks_rotation=90)
plt.title("Flower Classification with Augmentation")
plt.savefig('output/confusionmatric_floweraug.jpg')
plt.show()