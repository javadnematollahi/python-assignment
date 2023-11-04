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

df = load_house_attributes('assets/Houses Dataset/HousesInfo.txt')
# load the house images and then scale the pixel intensities to the
# range [0, 1]
print("[INFO] loading house images...")
images = load_house_images(df, 'assets/Houses Dataset')
images = images / 255.0
print("[INFO] processing data...")
split = train_test_split(df, images, test_size=0.25, random_state=42)
(trainAttrX, testAttrX, trainImagesX, testImagesX) = split
# find the largest house price in the training set and use it to
# scale our house prices to the range [0, 1] (will lead to better
# training and convergence)
maxPrice = trainAttrX["price"].max()
trainY = trainAttrX["price"] / maxPrice
testY = testAttrX["price"] / maxPrice
# process the house attributes data by performing min-max scaling
# on continuous features, one-hot encoding on categorical features,
# and then finally concatenating them together
(trainAttrX, testAttrX) = process_house_attributes(df,
												trainAttrX,
                                                testAttrX)

mlp = create_mlp(trainAttrX.shape[1], regress=False)
cnn = create_cnn(regress=False)
# create the input to our final set of layers as the *output* of both
# the MLP and CNN
combinedInput = concatenate([mlp.output, cnn.output])
# our final FC layer head will have two dense layers, the final one
# being our regression head
x = Dense(4, activation="relu")(combinedInput)
x = Dense(1, activation="linear")(x)

model_mix = Model(inputs=[mlp.input, cnn.input], outputs=x)

opt = Adam(learning_rate=1e-3)
model_mix.compile(loss="mean_absolute_percentage_error", optimizer=opt)

checkpoint = tf.keras.callbacks.ModelCheckpoint("best_mix_model_house_price",
                                            save_best_only=True)
stop_early = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=50)

print("[INFO] training model...")
model_mix.fit(
	x=[trainAttrX, trainImagesX], y=trainY,
	validation_data=([testAttrX, testImagesX], testY),
	epochs=200,
	callbacks=[stop_early, checkpoint, wandb_callbacks])

loaded_model = tf.keras.models.load_model('best_mix_model_house_price')
loaded_model.evaluate(x=[testAttrX, testImagesX],y=testY)
loaded_model.save('assets/mix_House_price.h5')

