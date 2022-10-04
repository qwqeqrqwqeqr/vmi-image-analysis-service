import urllib

import cv2
import numpy as np
from math import degrees

from business.analysis_image.util.constants import DEFAULT_SCORE
from business.analysis_image.util.message import RULE_PREDICT_SUCCESS_MESSAGE, RULE_SUCCESS_MESSAGE, \
    RULE_DEFAULT_MESSAGE, RULE_11_MESSAGE


def rule_11(img_path):
    score = DEFAULT_SCORE
    message = RULE_DEFAULT_MESSAGE

    resp = urllib.request.urlopen(img_path)
    img = np.asarray(bytearray(resp.read()), dtype='uint8')
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    lines = cv2.HoughLines(edges, 1, np.pi / 180, 30)


    if lines is None:
        message = RULE_11_MESSAGE["NO_DETECT_LINE"]
        score = 0
    else:
        positive = []
        negative = []
        for line in lines:
            rho, theta = line[0]
            degree = degrees(theta) - 90
            if degree < 0:
                negative.append(degree)
            else:
                positive.append(degree)

        if len(positive) > 0:
            message = RULE_11_MESSAGE["OVER_ANGLE"]
            score = 0
        else:
            negative_mean = np.mean(negative)
            if negative_mean <= -70 or negative_mean >= -20:
                message = RULE_11_MESSAGE["INCORRECT_ANGLE"]
                score = 0

    if score == 1:
        print(RULE_SUCCESS_MESSAGE)
        return True, RULE_PREDICT_SUCCESS_MESSAGE
    else:
        print(message)
        return False, message







