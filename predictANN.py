import tensorflow as tf
import numpy as np
from PIL import ImageOps

def get_model():
    return tf.keras.models.load_model(r'D:\Projects\Handwritten Digit Recognition\best_ANNmodel1.model')

def loadimg(img):
    model = get_model()
    
    img = img.resize((28,28))
    #convert rgb to grayscale
    img = img.convert('L')
    img = ImageOps.invert(img)
    img = np.array(img)
    #reshaping to support our model input and normalizing
    img = img.reshape(1,28,28,1)
    img = img/255.0
    #predicting the class
    res = model.predict([img])[0]
    return np.argmax(res), max(res)