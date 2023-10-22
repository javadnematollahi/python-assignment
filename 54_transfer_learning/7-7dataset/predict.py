import numpy as np
import tensorflow as tf
from keras.applications.vgg16 import preprocess_input

loaded_model = tf.keras.models.load_model('dataset/7_7.h5')

dataset_path_test = "dataset/test_images"

idg=tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255,
    preprocessing_function=preprocess_input
)

test_data=idg.flow_from_directory(
    dataset_path_test,
    target_size=(224,224),
    class_mode='categorical',
    batch_size=32,
    shuffle=True,
    subset='training',
)

Y_testtrue = []
Y_testpred = []

label_show = ['Ali_Khamenei', 'Angelina_Jolie', 'Barak_Obama', 'Behnam_Bani', 'Donald_Trump', 'Emma_Watson', 'Han_Hye_Jin', 'Kim_Jong_Un', 'Leyla_Hatami', 'Lionel_Messi', 'Michelle_Obama', 'Morgan_Freeman', 'Queen_Elizabeth', 'Scarlett_Johansson']

for i in range(1):
    images = test_data[i][0]
    # print(len(labels))
    for image in images:
        # X.append(image)                    # append tensor
        image = np.expand_dims(image, axis=0)
        prediction=loaded_model.predict(image)
        Y_testpred.append(np.argmax(prediction))

for i in range(1):
    labels = test_data[i][1]
    for label in labels:
        Y_testtrue.append(np.argmax(label.tolist()))  # append list
for i,j in zip(Y_testtrue,Y_testpred):
    print(f'real picture:  {label_show[i]}    ======>     predicte picture:  {label_show[j]}\n')