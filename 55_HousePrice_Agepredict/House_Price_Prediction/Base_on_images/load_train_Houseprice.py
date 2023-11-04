import tensorflow as tf
from tf.keras.models import Sequential
from tf.keras.layers import BatchNormalization
from tf.keras.layers import Activation
from tf.keras.layers import Dropout
from tf.keras.layers import Flatten
from tf.keras.layers import Input
from tf.keras.models import Model
from sklearn.model_selection import train_test_split
from tf.keras.layers import Dense
from tf.keras.optimizers import Adam
from tf.keras.layers import concatenate
from load_process_data import *
import wandb


from wandb.keras import (
   WandbMetricsLogger,
   WandbModelCheckpoint,
)
run = wandb.init(project="House_price_by_image_numerical")
config = wandb.config
wandb_callbacks = [
   WandbMetricsLogger(log_freq=5),
   WandbModelCheckpoint("models"),
]


def create_mlp(dim, regress=False):
	# define our MLP network
	model = Sequential()
	model.add(Dense(8, input_dim=dim, activation="relu"))
	model.add(Dense(4, activation="relu"))
	# check to see if the regression node should be added
	if regress:
		model.add(Dense(1, activation="linear"))
	# return our model
	return model


def create_cnn( regress=False):

	inputShape = (64, 64, 3)
	inputs = Input(shape=inputShape)

	Base_model = tf.keras.applications.VGG16(
			include_top=False,
			weights="imagenet",
			input_shape=(64,64,3),
			pooling ='avg'
			)
	for layer in Base_model.layers[0:-8]:
		layer.trainable = False

	# flatten the volume, then FC => RELU => BN => DROPOUT
	Base_model = inputs
	x = Flatten()(Base_model)
	x = Dense(16)(x)
	x = Activation("relu")(x)
	x = BatchNormalization(axis=-1)(x)
	x = Dropout(0.5)(x)
	# apply another FC layer, this one to match the number of nodes
	# coming out of the MLP
	x = Dense(4)(x)
	x = Activation("relu")(x)
	# check to see if the regression node should be added
	if regress:
		x = Dense(1, activation="linear")(x)
	# construct the CNN
	model = Model(inputs, x)
	# return the CNN
	return model

print("[INFO] loading house attributes...")
inputPath = os.path.sep.join(["assets/Houses Dataset", "HousesInfo.txt"])
df = load_house_attributes(inputPath)
# load the house images and then scale the pixel intensities to the
# range [0, 1]
print("[INFO] loading house images...")
images = load_house_images(df, 'assets/Houses Dataset')

# partition the data into training and testing splits using 75% of
# the data for training and the remaining 25% for testing
(trainAttrX, testAttrX, trainImagesX, testImagesX) = train_test_split(df, images, test_size=0.25, random_state=42)

maxPrice = trainAttrX["price"].max()
trainY = trainAttrX["price"] / maxPrice
testY = testAttrX["price"] / maxPrice


image_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255,
    horizontal_flip=True,
    brightness_range=[0.8,1.2],
)

train_data = image_data_generator.flow(
                                       trainImagesX,
                                       trainY,
                                       batch_size=32,
                                       shuffle=True
                                       )

validation_data = image_data_generator.flow(
                                       testImagesX,
                                       testY,
                                       batch_size=91,
                                       shuffle=False
                                       )

mobile_net = tf.keras.applications.VGG16(
    include_top=False,
    weights="imagenet",
    input_shape=(64,64,3),
    pooling ='avg'
    )
for layer in mobile_net.layers[0:-8]:
  layer.trainable = False

my_model = Sequential([
    mobile_net,
    tf.keras.layers.Flatten(),
    # tf.keras.layers.Dense(512, activation="relu"),
    # tf.keras.layers.Dropout(0.2),
    # tf.keras.layers.Dense(256, activation="relu"),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(1, activation="linear"),
])

my_model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate=1e-4),
              loss = tf.keras.losses.mean_absolute_percentage_error
              )

checkpoint = tf.keras.callbacks.ModelCheckpoint("best_model_house_price_image",
                                            save_best_only=True)
stop_early = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=50)

history = my_model.fit(
    train_data,
    validation_data=validation_data,
    epochs=100 ,
    callbacks=[stop_early, checkpoint]
    )

loaded_model = tf.keras.models.load_model('best_model_house_price_image')
loaded_model.save('weights/image_House_price.h5')
loaded_model.evaluate(validation_data)
