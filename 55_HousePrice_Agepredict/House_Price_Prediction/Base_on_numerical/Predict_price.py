import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelBinarizer
from turtle import Turtle, Screen

def predict(bedrooms, bathrooms, area, zipcode):
  bed_bath_area=abs((np.array([bedrooms,bathrooms,area])-np.array([  1.  , 1., 701.]))/(np.array([1.0e+01 ,6.5e+00 ,7.0e+03])-np.array([  1.  , 1. ,701.])))
  zipBinarizer = LabelBinarizer().fit([91901, 92276, 92677, 92880, 93446, 93510, 94501])
  inputCategorical = zipBinarizer.transform([zipcode])
  inputs = np.hstack([list(inputCategorical.ravel()), list(bed_bath_area)])

  num_data=inputs.reshape(1,10)
  loaded_model = tf.keras.models.load_model('weights/numerical_House_price.h5')
  preds = loaded_model.predict(num_data)
  return preds
  # diff = preds.flatten() - testY
  # percentDiff = (diff / testY) * 100
  # absPercentDiff = np.abs(percentDiff)


price = predict(2,1,2690,92276)*5858000
print("Your House Price base on numerical inputs is about {:.2f}$".format(price[0][0]))

font1 = ('Arial', 24, 'bold')
font2 = ('Arial', 34, 'bold')

marker = Turtle(visible=False)
marker.penup()

screen = Screen()
screen.bgcolor("black")
screen.title("House Price Prediction")
screen.setup(700, 400)

marker = Turtle(visible=False)
marker.penup()
marker.color('white')
marker.goto(-340, 140)
marker.write("Your House Price base ", font=font2)
marker.goto(-340, 100)
marker.write("on below numerical inputs", font=font2)
marker.goto(-340, 60)
marker.write("is about {:.2f}$".format(price[0][0]), font=font2)

marker.goto(-340, -20)
marker.color('gray')
marker.write("bedrooms=2", font=font1)
marker.goto(-340, -60)
marker.color('gray')
marker.write("bathrooms=1", font=font1)
marker.goto(-340, -100)
marker.color('gray')
marker.write("area=2690", font=font1)
marker.goto(-340, -140)
marker.color('gray')
marker.write("zipcode=92276", font=font1)

screen.onkey(screen.bye, "Escape")

screen.listen()

screen.mainloop()

