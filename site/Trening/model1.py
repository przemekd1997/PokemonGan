# -*- coding: utf-8 -*-
"""zal

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18lB3dnhyHr-KsCHm7P2idftq7YzwR88w
"""

import os
from os import listdir
from os.path import isfile, join
from PIL import Image
import tensorflow as tf
from tensorflow import keras
from keras.layers import Conv2D
from keras.layers import UpSampling2D
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LeakyReLU
from keras.layers import Dropout
from keras.optimizers import RMSprop
from keras.optimizers import Adam
from keras.layers import Reshape
from keras.layers import Flatten
from keras.layers import BatchNormalization
from keras.layers import Activation
from google.colab import drive
import numpy as np
import matplotlib.pyplot as plt

drive.mount("/content/drive", force_remount=True)
print(tf.__version__)

img_height = 64
img_width = 64
n_elements = 100
image_path = '/content/drive/My Drive/Colab Notebooks/image/data/dataset/'
generate_path = '/content/drive/My Drive/Colab Notebooks/image/generated/'

# load dataset
dataset = [file for file in listdir(image_path) if isfile(join(image_path, file))]
image_count = len(dataset)

# correct shape of images
temp = np.zeros((img_height,img_width,3))

#get single images from file name
def get_image(file_number):
  img = Image.open(image_path + dataset[file_number])
  new_img = img.resize((img_height,img_width))
  new_img.convert('RGB')
  data = np.asarray(new_img)
  # if image is not in correct shape get new random image
  if (data.shape != temp.shape):
    a = np.random.randint(0, image_count, 1)
    data = get_image(a[0])
  return data

#get multple images from array of file names
def get_array_images(numbers):
  data = np.zeros((len(numbers),img_height,img_width,3))
  i = 0
  for x in numbers:
    image = get_image(x)
    data[i] = image
    i += 1
  return data

# define the standalone discriminator model
def define_discriminator():
  model = Sequential()
  input_shape = (img_height, img_width, 3)
  dropout_prob = 0.4

  model.add(Conv2D(64, 5, strides=2, input_shape=input_shape, padding='same'))
  model.add(LeakyReLU())
    
  model.add(Conv2D(128, 5, strides=2, padding='same'))
  model.add(LeakyReLU())
  model.add(Dropout(dropout_prob))
    
  model.add(Conv2D(256, 5, strides=2, padding='same'))
  model.add(LeakyReLU())
  model.add(Dropout(dropout_prob))
    
  model.add(Conv2D(512, 5, strides=2, padding='same'))
  model.add(LeakyReLU())
  model.add(Dropout(dropout_prob))
    
  model.add(Flatten())
  model.add(Dense(1))
  model.add(Activation('sigmoid'))

  return model

# compile discriminator
def compile_discriminator(d_model):
  optim = RMSprop(lr=0.0002, clipvalue=1.0, decay=6e-8)
  d_model.compile(loss='binary_crossentropy', optimizer=optim, metrics=['accuracy'])
  return d_model

# define the standalone generator model
def define_generator():
  model = Sequential()
  model.add(Dense(8*8*256, input_dim=100))
  model.add(BatchNormalization(momentum=0.9))
  model.add(Activation('relu'))
  model.add(Reshape((8,8,256)))
  model.add(Dropout(0.4))
    
  model.add(UpSampling2D())
  model.add(Conv2D(128, 5, padding='same'))
  model.add(BatchNormalization(momentum=0.9))
  model.add(Activation('relu'))
    
  model.add(UpSampling2D())
  model.add(Conv2D(128, 5, padding='same'))
  model.add(BatchNormalization(momentum=0.9))
  model.add(Activation('relu'))
    
  model.add(UpSampling2D())
  model.add(Conv2D(64, 5, padding='same'))
  model.add(BatchNormalization(momentum=0.9))
  model.add(Activation('relu'))
    
  model.add(Conv2D(32, 5, padding='same'))
  model.add(BatchNormalization(momentum=0.9))
  model.add(Activation('relu'))
    
  model.add(Conv2D(3, 5, padding='same'))
  model.add(Activation('sigmoid'))
    
  return model

# define the combined generator and discriminator model, for updating the generator
def define_gan(gen_model, dis_model):
	model = Sequential()
	model.add(gen_model)
	# make weights in the discriminator not trainable (only for GAN)
	for layer in dis_model.layers:
		layer.trainable = False
	
	model.add(dis_model)
	# compile model
	optim = Adam(lr=0.0001, clipvalue=1.0, decay=3e-8)
	model.compile(loss='binary_crossentropy', optimizer=optim)
	return model
# get real images & create labels
def generate_real_samples(data_set, n_samples):
	# choose random instances
	ix = np.random.randint(0, image_count, n_samples)
	# retrieve selected images
	X = np.array(get_array_images(ix))
	X = X  / 255.0
	# generate 'real' class labels (1)
	y = np.ones((n_samples, 1))
	return X, y

# generate seed as input for the generator
def generate_seed(n_elements, n_samples):
	# generate points between 0,1000
	x_input = np.random.randint(0,1000, size=(n_samples,n_elements))
	return x_input
# generate fake images from generator & create labels
def generate_fake_samples(g_model, n_elements, n_samples):
	x_input = generate_seed(n_elements, n_samples)
	# predict outputs
	X = g_model.predict(x_input)
	# create 'fake' class labels (0)
	y = np.zeros((n_samples, 1))
	return X, y

#create and save a plot of generated images
def save_plot(examples, epoch, n=10):
	examples = examples * 255
	# plot images
	for i in range(n-1):
		# define subplot
		plt.subplot(3, 3, 1 + i)
		# turn off axis
		plt.axis('off')
		# plot raw pixel data
		plt.imshow(examples[i].astype("uint8"))
	# save plot to file
	filename = 'generated_plot_e%03d.png' % (epoch+1)
	plt.savefig(generate_path + filename)
	plt.close()

# evaluate the discriminator, plot generated images, save generator model
def summarize_performance(epoch, gan_model, g_model, d_model, dataset, n_elements, n_samples=100):
	# prepare real samples
	X_real, y_real = generate_real_samples(dataset, n_samples)
	# evaluate discriminator on real examples
	_, acc_real = d_model.evaluate(X_real, y_real, verbose=0)
	# prepare fake examples
	x_fake, y_fake = generate_fake_samples(g_model, n_elements, n_samples)
	# evaluate discriminator on fake examples
	_, acc_fake = d_model.evaluate(x_fake, y_fake, verbose=0)
	# summarize discriminator performance
	print('>Accuracy real: %.0f%%, fake: %.0f%%' % (acc_real*100, acc_fake*100))
	# save plot
	save_plot(x_fake, epoch)

# save model weights (generator & discriminator)
def save_weights(g_model, d_model,epoch):
  filename = 'generator_model_' + str(epoch) + '.h5'
  g_model.save_weights(generate_path + 'models/' + filename)
  filename = 'discriminator_model_' + str(epoch) + '.h5'
  d_model.save_weights(generate_path + 'models/' + filename)

# train the generator and discriminator
def train(g_model, d_model, gan_model, dataset, n_elements, n_epochs=1000, n_batch=256):
	bat_per_epo = int(image_count / n_batch)
	half_batch = int(n_batch / 2)
	# manually enumerate epochs
	for i in range(n_epochs):
		# enumerate batches over the training set
		for j in range(bat_per_epo):
			# get randomly selected 'real' samples
			X_real, y_real = generate_real_samples(dataset, half_batch)
			# generate 'fake' examples
			X_fake, y_fake = generate_fake_samples(g_model, n_elements, half_batch)
			# create training set for the discriminator
			X, y = np.vstack((X_real, X_fake)), np.vstack((y_real, y_fake))
			# update discriminator model weights
			d_loss, _ = d_model.train_on_batch(X, y) 
			# prepare seed as input for the generator
			X_gan = generate_seed(n_elements, n_batch)
			# create inverted labels for the fake samples
			y_gan = np.ones((n_batch, 1))
			# update the generator via the discriminator's error
			g_loss = gan_model.train_on_batch(X_gan, y_gan)
			# summarize loss on this batch
			print('>%d, %d/%d, d=%.3f, g=%.3f' % (i+1, j+1, bat_per_epo, d_loss, g_loss))
		# evaluate the model performance, sometimes
		if (i+1) % 10 == 0:
			summarize_performance(i, gan_model, g_model, d_model, dataset, n_elements)
			save_weights(g_model, d_model,i)

# creating networks
d_model = define_discriminator()
g_model = define_generator()

# load networks (optional)
#d_model.load_weights(generate_path + 'discriminator_model.h5')
#g_model.load_weights(generate_path + '123.h5')

d_model = compile_discriminator(d_model)
gan_model = define_gan(g_model, d_model)

# train model
train(g_model, d_model, gan_model, dataset, n_elements)