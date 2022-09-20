# 요구사항:
# 1. 하나의 선일 것 (추가로 그린 것도 가능)
# 2. 선의 1/2 이상이 20~70도 사이에 있을 것
# 3. 갑작스런 방향 변화가 없을 것

import urllib

import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import degrees

from analysis.rule.util.message import RULE_PREDICT_SUCCESS_MESSAGE, RULE_13_MESSAGE, RULE_SUCCESS_MESSAGE


def rule_13(img_path):
    score = 1
    message = ""

    resp = urllib.request.urlopen(img_path)
    img = np.asarray(bytearray(resp.read()), dtype='uint8')
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    lines = cv2.HoughLines(edges, 1, np.pi / 180, 30)


    if lines is None:
        message = RULE_13_MESSAGE["NO_DETECT_LINE"]
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

        if len(negative) > 0:
            message = RULE_13_MESSAGE["OVER_ANGLE"]
            score = 0
        else:
            positive_mean = np.mean(positive)
            if positive_mean <= 20 or positive_mean >= 70:
                message = RULE_13_MESSAGE["INCORRECT_ANGLE"]
                score = 0

    if score == 1:
        print(RULE_SUCCESS_MESSAGE)
        return True, RULE_PREDICT_SUCCESS_MESSAGE
    else:
        print(message)
        return False, message





def drawLines(img, lines):
    h, w = img.shape[:2]

    if lines is not None:
        for line in lines:
            r, theta = line[0]  # 거리와 각도
            tx, ty = np.cos(theta), np.sin(theta)  # x, y축에 대한 삼각비
            x0, y0 = tx * r, ty * r  # x, y 기준(절편) 좌표
            x1, y1 = int(x0 + w * (-ty)), int(y0 + h * tx)
            x2, y2 = int(x0 - w * (-ty)), int(y0 - h * tx)

            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 1)

    return img









