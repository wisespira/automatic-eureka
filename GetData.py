## From Data
import pandas as pd
import numpy as np
## ML
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import glob
## Web Scraping 
import requests
from bs4 import BeautifulSoup
## Image manipulation
from PIL import Image
from torchvision import transforms 
import matplotlib.pyplot as plt
## Filing Functionality 
import io
import os
import hashlib



im = Image.open("C:/Users/Admin/Desktop/ART/data/Abstract_gallery/Abstract_image_50.jpg")
#im.show()
width, height = im.size
size = 100, 100


trans = transforms.ToPILImage()
trans1 = transforms.ToTensor()

tensorPic = trans1(im)
print(tensorPic.shape)
tensorPic[2] = 0.75
print(tensorPic)
#trans(tensorPic[1]).show()


im.thumbnail(size, Image.ANTIALIAS)
im.show()

"""
## Build the encoder
"""

latent_dim = 2
#https://stackoverflow.com/questions/44747343/keras-input-explanation-input-shape-units-batch-size-dim-etc#:~:text=The%20input%20shape&text=In%20Keras%2C%20the%20input%20layer,shape%20as%20your%20training%20data.
# 30 images of 50x50 pixels in RGB (3 channels)
encoder_inputs = keras.Input(shape=(30,100,100,3))
#x = layers.Conv2D(32, 3, activation="relu", strides=2, padding="same")(encoder_inputs)
#x = layers.Conv2D(64, 3, activation="relu", strides=2, padding="same")(x)
#x = layers.Flatten()(x)
#x = layers.Dense(16, activation="relu")(x)
#z_mean = layers.Dense(latent_dim, name="z_mean")(x)
#z_log_var = layers.Dense(latent_dim, name="z_log_var")(x)


#z = Sampling()([z_mean, z_log_var])
#encoder = keras.Model(encoder_inputs, [z_mean, z_log_var, z], name="encoder")
#encoder.summary()


#plt.imshow(trans(trans1(im)))


#tf.reset_default_graph()

#batch_size = 64

#X_in = tf.placeholder(dtype=tf.float32, shape=[None, 28, 28], name='X')
#Y    = tf.placeholder(dtype=tf.float32, shape=[None, 28, 28], name='Y')
#Y_flat = tf.reshape(Y, shape=[-1, 28 * 28])
#keep_prob = tf.placeholder(dtype=tf.float32, shape=(), name='keep_prob')

#dec_in_channels = 1
#n_latent = 8

#reshaped_dim = [-1, 7, 7, dec_in_channels]
#inputs_decoder = 49 * dec_in_channels / 2


#def lrelu(x, alpha=0.3):
#    return tf.maximum(x, tf.multiply(x, alpha))
































def persist_image(folder_path:str,url:str):
    try:
        image_content = requests.get(url).content

    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")

    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        file_path = os.path.join(folder_path,hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
        print(f"SUCCESS - saved {url} - as {file_path}")
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")

#persist_image(r"C:\Users\Admin\Desktop\ART", "https://d3d00swyhr67nd.cloudfront.net/w1200h1200/collection/SFK/SED/SFK_SED_ST_1992_9_587-001.jpg")

#artLoc = pd.read_csv("./painting_dataset_2018.csv")
#print(artLoc.describe())

#print(artLoc['Image URL'][0])
#result = requests.get(artLoc['Image URL'][0])