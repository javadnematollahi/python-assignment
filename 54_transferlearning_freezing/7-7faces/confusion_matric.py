import tensorflow as tf
from keras.applications.vgg16 import preprocess_input
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

dataset_path_train = "dataset/7-7-dataset"

idg = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255,
    horizontal_flip=True,
    brightness_range=(0.8,1),
    zoom_range=0.1,
    validation_split=0.1,
    preprocessing_function=preprocess_input
)

train_data = idg.flow_from_directory(
    dataset_path_train,
    target_size=(224,224),
    class_mode='categorical',
    batch_size=32,
    shuffle=True,
    subset='training',
)
val_data = idg.flow_from_directory(
    dataset_path_train,
    target_size=(224,224),
    class_mode='categorical',
    batch_size=32,
    shuffle=True,
    subset='validation',
)

loaded_model = tf.keras.models.load_model('dataset/7_7.h5')

Y_true = []
Y_pred = []

for i in range(2):
    images = val_data[i][0]
    for image in images:
        image = np.expand_dims(image, axis=0)
        prediction=loaded_model.predict(image)
        Y_pred.append(np.argmax(prediction))

for i in range(2):
    labels = val_data[i][1]
    for label in labels:
        # print(np.argmax(label.tolist()))
        Y_true.append(np.argmax(label.tolist()))  # append list

labels=[]
for i in val_data.class_indices:
  labels.append(i)
print(labels)
cm = confusion_matrix(Y_true, Y_pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)

disp.plot(cmap=plt.cm.Blues,xticks_rotation=90)
plt.title("Flower Classification with Augmentation")
# plt.savefig('output/confusionmatric_floweraug.jpg')
plt.show()       