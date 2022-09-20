import urllib

import cv2
import numpy as np

from analysis.rule.util.constants import DEFAULT_SCORE
from analysis.rule.util.message import RULE_PREDICT_SUCCESS_MESSAGE, RULE_6_MESSAGE, RULE_SUCCESS_MESSAGE, \
    RULE_DEFAULT_MESSAGE


def rule_9(img_path):
    score = DEFAULT_SCORE
    message = RULE_DEFAULT_MESSAGE

    resp = urllib.request.urlopen(img_path)
    img = np.asarray(bytearray(resp.read()), dtype='uint8')
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)[1]

    contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    is_ellipse = 0
    for cnt in contours:
        if len(cnt) >= 10:
            ellipse = cv2.fitEllipse(cnt)
            width = ellipse[1][1] * 2
            height = ellipse[1][0] * 2

            if width >= 30 and height >= 30:  # 고리가 너무 작은 경우는 노이즈라고 생각하여 무시
                is_ellipse = 1
                img_copy = cv2.ellipse(img_copy, ellipse, (0, 255, 0), 2)

                if width * 2 <= height or height * 2 <= width:
                    message = RULE_6_MESSAGE["INCORRECT_RATIO"]
                    score = 0

    if is_ellipse == 0:
        message =  RULE_6_MESSAGE["NO_DETECT_CIRCLE"]
        score = 0


    if score == 1:
        print(RULE_SUCCESS_MESSAGE)
        return True, RULE_PREDICT_SUCCESS_MESSAGE
    else:
        print(message)
        return False, message




