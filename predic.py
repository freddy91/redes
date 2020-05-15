#!D:/python/python.exe
import sys
import os
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from skimage import io
from skimage.transform import resize

modelo = tf.keras.models.load_model('modeloPHP.h5')

nombre = 'C:/xampp/htdocs/img/'+sys.argv[1]


img = io.imread("%s" % (nombre))

img = resize(img, (32, 32))

img = np.expand_dims(img, axis=0)

predic = modelo.predict(img)
categorias = ['avion', 'automovil', 'pajaro', 'gato', 'ciervo', 'perro', 'rana', 'caballo', 'barco', 'camion']

cosa = categorias[np.argmax(predic[0])]
print(cosa) 
