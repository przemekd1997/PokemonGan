from flask import Flask
from flask import jsonify
from flask import request
import os
from os import listdir
from os.path import isfile, join
import torch
import torch.nn as nn
from torch.autograd import Variable
from torchvision import transforms
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
import numpy as np
import io
import base64
from PIL import Image



app = Flask(__name__)

# generate points between 0,1000
def generate_seed1():	
	x_input = np.random.randint(0,1000, size=(5,100))
	return x_input
#
#  generate points between -100,100
def generate_seed2():
  x_input = np.random.randint(0,200, size=(5,100))
  x_input -= 100
  return x_input

# convert to base64
def to_base(pic,md):
  if(md == 0):
    img = Image.fromarray(pic.astype(np.uint8))
  else:
    img = pic
  rawBytes = io.BytesIO()
  img.save(rawBytes, "PNG")
  rawBytes.seek(0) 
  im_b64 = base64.b64encode(rawBytes.read())
  ENCODING = 'utf-8'
  base64_string = im_b64.decode(ENCODING)
  return base64_string

# de-normalizing the images
def denorm_monsters(x):
  renorm = (x*0.5)+0.5
  return renorm.clamp(0,1)

# generator for model 2
class Generator(nn.Module):
    # define the model it has 5 transpose
    # convolutions and uses relu activations
    # it has a TanH activation on the last
    # layer
    def __init__(self):
        super(Generator, self).__init__()
        self.main = nn.Sequential(
            nn.ConvTranspose2d(100, 
                              512, 
                              kernel_size=4, 
                              stride=1, 
                              padding=0,
                              bias=False),
            nn.BatchNorm2d(512),
            nn.ReLU(),

            nn.ConvTranspose2d(512, 
                              256, 
                              kernel_size=4, 
                              stride=2,
                              padding=1,
                              bias=False),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            
            nn.ConvTranspose2d(256, 
                              128, 
                              kernel_size=4, 
                              stride=2, 
                              padding=1,
                              bias=False),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            
            nn.ConvTranspose2d(128, 
                              64, 
                              kernel_size=4, 
                              stride=2, 
                              padding=1,
                              bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            
            nn.ConvTranspose2d(64, 
                               3,
                               kernel_size=4,
                               stride=2,
                               padding=1,
                               bias=False),
            nn.Tanh()
        )
        
    # define how to propagate 
    # through this network
    def forward(self, inputs):
        output = self.main(inputs)
        return output

# load trained models
model2 = Generator()
model2.load_state_dict(torch.load("models/gen2.zip",map_location=torch.device('cpu')))
model5 = Generator()
model5.load_state_dict(torch.load("models/gen5.zip",map_location=torch.device('cpu')))
model1 = keras.models.load_model("models/gen1.h5")
model3 = keras.models.load_model("models/gen3.h5")
model4 = keras.models.load_model("models/gen4.h5")
model6 = keras.models.load_model("models/gen6.h5")
model7 = keras.models.load_model("models/gen7.h5")

# endpoint for model 1 - color
@app.route("/predict1", methods=["POST"] )
def predict1():
  seed = generate_seed1()
  image = model1.predict(seed)
  image *= 255
  response = {
	  'img1' : to_base(image[0],0),
    'img2' : to_base(image[1],0),
    'img3' : to_base(image[2],0),
    'img4' : to_base(image[3],0),
    'img5' : to_base(image[4],0)
	}
	
  return jsonify(response)

# endpoint for model 2 - color
@app.route("/predict2", methods=["POST"] )
def predict2():
  noise = Variable(torch.randn(5, 100, 1, 1))
  fixed_imgs = model2(noise)
  result = denorm_monsters(fixed_imgs.cpu().data)
  response = {
	  'img1' : to_base(transforms.Compose([transforms.ToPILImage()])(result[0]),1),
    'img2' : to_base(transforms.Compose([transforms.ToPILImage()])(result[1]),1),
    'img3' : to_base(transforms.Compose([transforms.ToPILImage()])(result[2]),1),
    'img4' : to_base(transforms.Compose([transforms.ToPILImage()])(result[3]),1),
    'img5' : to_base(transforms.Compose([transforms.ToPILImage()])(result[4]),1)
	}
	
  return jsonify(response)

# endpoint for model 3 - color
@app.route("/predict3", methods=["POST"] )
def predict3():
  seed = generate_seed2()
  image = model3.predict(seed)
  image *= 255
  response = {
	  'img1' : to_base(image[0],0),
    'img2' : to_base(image[1],0),
    'img3' : to_base(image[2],0),
    'img4' : to_base(image[3],0),
    'img5' : to_base(image[4],0)
	}
	
  return jsonify(response)

# endpoint for model 1 - white
@app.route("/predict4", methods=["POST"] )
def predict4():
  seed = generate_seed1()
  image = model4.predict(seed)
  image *= 255
  response = {
	  'img1' : to_base(image[0],0),
    'img2' : to_base(image[1],0),
    'img3' : to_base(image[2],0),
    'img4' : to_base(image[3],0),
    'img5' : to_base(image[4],0)
	}
	
  return jsonify(response)

# endpoint for model 2 - white
@app.route("/predict5", methods=["POST"] )
def predict5():
  noise = Variable(torch.randn(5, 100, 1, 1))
  fixed_imgs = model5(noise)
  result = denorm_monsters(fixed_imgs.cpu().data)
  response = {
	  'img1' : to_base(transforms.Compose([transforms.ToPILImage()])(result[0]),1),
    'img2' : to_base(transforms.Compose([transforms.ToPILImage()])(result[1]),1),
    'img3' : to_base(transforms.Compose([transforms.ToPILImage()])(result[2]),1),
    'img4' : to_base(transforms.Compose([transforms.ToPILImage()])(result[3]),1),
    'img5' : to_base(transforms.Compose([transforms.ToPILImage()])(result[4]),1)
	}
	
  return jsonify(response)

# endpoint for model 3 - white
@app.route("/predict6", methods=["POST"] )
def predict6():
  seed = generate_seed2()
  image = model6.predict(seed)
  image *= 255
  response = {
	  'img1' : to_base(image[0],0),
    'img2' : to_base(image[1],0),
    'img3' : to_base(image[2],0),
    'img4' : to_base(image[3],0),
    'img5' : to_base(image[4],0)
	}
	
  return jsonify(response)

# endpoint for model 1 - week
@app.route("/predict7", methods=["POST"] )
def predict7():
  seed = generate_seed1()
  image = model7.predict(seed)
  image *= 255
  response = {
	  'img1' : to_base(image[0],0),
    'img2' : to_base(image[1],0),
    'img3' : to_base(image[2],0),
    'img4' : to_base(image[3],0),
    'img5' : to_base(image[4],0)
	}
	
  return jsonify(response)


app.run(port=3000)

