import os
import urllib

import cv2
import numpy as np
from keras.saving.save import load_model
from tensorflow import keras

from analysis.predict.util.message import PREDICT_FAIL_MESSAGE, PREDICT_SUCCESS_MESSAGE


def predict(image_path, model_path):
    img_size = 150

    try:
        resp = urllib.request.urlopen(image_path)
        img = np.asarray(bytearray(resp.read()), dtype='uint8')
        img = cv2.imdecode(img, cv2.IMREAD_GRAYSCALE)

        resized_image = cv2.resize(img, (img_size, img_size))  # Reshaping images to preferred size
        resized_255 = np.array(resized_image) / 255
        predict_image = resized_255.reshape(-1, img_size, img_size, 1)

    except Exception as e:

        print(e)

    model = keras.models.load_model(model_path)
    predict_val = model.predict(predict_image)

    print(predict_val)
    if predict_val < 0.7:
        print(PREDICT_FAIL_MESSAGE)
        return False, PREDICT_FAIL_MESSAGE
    else:
        print(PREDICT_SUCCESS_MESSAGE)
        return True, PREDICT_SUCCESS_MESSAGE
