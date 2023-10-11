import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

dataset_path = "assets/animals"

idg = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.1,

    rotation_range=10,   #degree
    zoom_range=0.1,   #percent
    horizontal_flip=True
)

dataset_train = idg.flow_from_directory(
    dataset_path,
    shuffle=True,
    seed=123,
    # save_to_dir="/content/drive/MyDrive/dataset/animal_test",
    subset="training",
    target_size= (224,224)
)

dataset_validation = idg.flow_from_directory(
    dataset_path,
    shuffle=True,
    seed=123,
    subset="validation",
    target_size= (224,224)
)

model = models.Sequential([
    layers.Conv2D(64, (3, 3), strides=(2, 2), activation="relu", padding="same", input_shape=(224, 224, 3)),
    layers.MaxPooling2D(),
    layers.Conv2D(128, (3, 3), strides=(2, 2), activation="relu"),
    layers.MaxPooling2D(),
    layers.Conv2D(256, (3, 3), strides=(2, 2), activation="relu"),
    layers.MaxPooling2D(),

    layers.Flatten(),

    layers.Dense(512, activation="relu"),
    layers.Dense(5, activation="softmax"),
])

model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate=0.001),
              loss = tf.keras.losses.categorical_crossentropy,
              metrics = ['accuracy'])

history = model.fit(dataset_train, validation_data=dataset_validation, epochs=20)

model.save('weights/animals.h5')
model = tf.keras.models.load_model('weights/animals.h5')
count=0
Y_true = []
Y_pred = []
label_animal= ['cat', 'dog', 'elephant', 'giraffe', 'panda']
images,labels = dataset_validation[0]
    # print(len(labels))

for image in images:
    count=count+1
    print(count)
    image = np.expand_dims(image, axis=0) 
    prediction=model.predict(image)
    Y_pred.append(np.argmax(prediction))

for label in labels:
    Y_true.append(np.argmax(label))  # append list
print(f'Y_true:  {Y_true}\nY_pred: {Y_pred}')

# labels =dataset_validation.class_names

cm = confusion_matrix(Y_true, Y_pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=label_animal)

disp.plot(cmap=plt.cm.Blues,xticks_rotation=90)
plt.title("Animal Classification with Augmentation")
plt.savefig('output/confusionmatric_animal.jpg')
plt.show()



