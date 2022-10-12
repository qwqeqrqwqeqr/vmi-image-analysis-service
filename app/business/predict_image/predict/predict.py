import urllib

import cv2
import numpy as np
from distributed.protocol import torch
from tensorflow import keras
from torch import device
import torch

from business.predict_image.util.message import PREDICT_FAIL_MESSAGE, PREDICT_SUCCESS_MESSAGE


def predict(image_path, model_path):
    img_size = 150
    test_data = []
    device = 'cpu'

    try:
        resp = urllib.request.urlopen(image_path)
        img = np.asarray(bytearray(resp.read()), dtype='uint8')
        img = cv2.imdecode(img, cv2.IMREAD_GRAYSCALE)

        resized_img = cv2.resize(img, (img_size, img_size))  # Reshaping images to preferred size
        resized_img = resized_img / 255

        test_data.append([resized_img])
        test_data = np.array(test_data)

        test_tensor = torch.FloatTensor(test_data)
        test_tensor = test_tensor.to(device)

    except Exception as e:

        print(e)

    model = torch.load(model_path, map_location=device)
    model = model.to(device)
    model.eval()

    outputs = model(test_tensor)
    predict_val, _ = torch.max(outputs, 1)

    if predict_val < 0.7:
        print(PREDICT_FAIL_MESSAGE)
        return 0, PREDICT_FAIL_MESSAGE
    else:
        print(PREDICT_SUCCESS_MESSAGE)
        return 1, PREDICT_SUCCESS_MESSAGE


def default_predict():
    return 0, PREDICT_FAIL_MESSAGE