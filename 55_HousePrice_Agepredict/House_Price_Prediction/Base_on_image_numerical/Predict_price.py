import numpy as np
import os
import cv2
import tensorflow as tf
from sklearn.preprocessing import LabelBinarizer
import matplotlib.pyplot as plt




def predict(bedrooms, bathrooms, area, zipcode,images_path):
  bed_bath_area=abs((np.array([bedrooms,bathrooms,area])-np.array([  1.  , 1., 701.]))/(np.array([1.0e+01 ,6.5e+00 ,7.0e+03])-np.array([  1.  , 1. ,701.])))
  zipBinarizer = LabelBinarizer().fit([91901, 92276, 92677, 92880, 93446, 93510, 94501])
  inputCategorical = zipBinarizer.transform([zipcode])
  inputs = np.hstack([list(inputCategorical.ravel()), list(bed_bath_area)])
  pathimages=[]
  for image in os.listdir(images_path):
    pathh = os.path.sep.join([images_path,image])
    pathimages.append(pathh)
  pathimages.sort()
  inputImages = []
  inputImages_for_show = []
  outputImage = np.zeros((64, 64, 3), dtype="uint8")
  showImage = np.zeros((1000, 1000, 3), dtype="uint8")
  # loop over the input house paths
  for housePath in pathimages:
    # load the input image, resize it to be 32 32, and then
    # update the list of input images
    image = cv2.imread(housePath)
    image_show = cv2.resize(image, (500, 500))
    inputImages_for_show.append(image_show)
    image = cv2.resize(image, (32, 32))
    inputImages.append(image)

  outputImage[0:32, 0:32] = inputImages[0]
  outputImage[0:32, 32:64] = inputImages[1]
  outputImage[32:64, 32:64] = inputImages[2]
  outputImage[32:64, 0:32] = inputImages[3]

  showImage[0:500, 0:500] = inputImages_for_show[0]
  showImage[0:500, 500:1000] = inputImages_for_show[1]
  showImage[500:1000, 500:1000] = inputImages_for_show[2]
  showImage[500:1000, 0:500] = inputImages_for_show[3]

  num_data=inputs.reshape(1,10)
  image_data=outputImage.reshape(1,64,64,3)
  image_data = image_data / 255.0
  loaded_model = tf.keras.models.load_model('weights/mix_House_price.h5')
  preds = loaded_model.predict([num_data, image_data])
  return preds*5858000,showImage
  # diff = preds.flatten() - testY
  # percentDiff = (diff / testY) * 100
  # absPercentDiff = np.abs(percentDiff)

price ,image= predict(2,1,2690,92276,'my_house')
plt.title("Your House Price base on \nnumerical and image inputs \nis about {:.2f}$".format(price[0][0]),fontsize = 25)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
plt.show()
