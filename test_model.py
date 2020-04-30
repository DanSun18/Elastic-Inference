'''Test saved model with test image'''
import numpy as np
import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model('mnist_tf_model') 

'''source: https://www.tensorflow.org/tutorials/load_data/images'''
IMG_HEIGHT = 28
IMG_WIDTH = 28


def decode_img(img):
    # convert the compressed string to a 3D uint8 tensor
    img = tf.image.decode_jpeg(img, channels=3)
    # Use `convert_image_dtype` to convert to floats in the [0,1] range.
    img = tf.image.convert_image_dtype(img, tf.float32)
    # resize the image to the desired size.
    return tf.image.resize(img, [IMG_WIDTH, IMG_HEIGHT])


def process_path(file_path):
    # load the raw data from the file as a string
    img = tf.io.read_file(file_path)
    img = decode_img(img)
    return img

test_image_path = 'test_data/img_1.jpg'
img = process_path(test_image_path)
img_grey = tf.image.rgb_to_grayscale(img)
small_batch = tf.expand_dims(img_grey, 0) 
# print(small_batch)
pred_prob = model.predict(small_batch)[0]
pred_label = pred_prob.argmax(axis=-1)
print(pred_label)