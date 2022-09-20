import urllib

import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import degrees

from analysis.rule.util.message import RULE_5_MESSAGE

success_message = "유사도 및 규칙을 충족합니다."


def rule_5(img_path):
    score = 1
    message = ""

    resp = urllib.request.urlopen(img_path)
    img = np.asarray(bytearray(resp.read()), dtype='uint8')
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    lines = cv2.HoughLines(edges, 1, np.pi / 180, 50)


    if lines is None:
        message = RULE_5_MESSAGE["NO_DETECT_LINE"]
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
        degree_all = positive + negative

        if len(degree_all) > 20:
            message = RULE_5_MESSAGE["NOISE"]
            score = 0
        else:
            positive_mean = np.mean(positive)
            negative_mean = np.mean(negative)
            positive_diff = positive_mean - 0
            negative_diff = abs(negative_mean) - 0
            diff = positive_diff + negative_diff

            if diff > 10:
                message = RULE_5_MESSAGE["MULTIPLE_LINES"]
                score = 0
            else:
                negative_abs = []
                for degree in negative:
                    negative_abs.append(abs(degree))
                degree_all = positive + negative_abs

                if np.mean(degree_all) >= 30:
                    message = RULE_5_MESSAGE["INCORRECT_ANGLE"]
                    score = 0

    if score == 1:
        print("규칙을 충족합니다.")
        return True, success_message
    else:
        print(message)
        return False, message




def drawLines(img, lines):
    h, w = img.shape[:2]

    if lines is not None:
        for line in lines:
            r ,theta = line[0]  # 거리와 각도
            tx, ty = np.cos(theta), np.sin(theta)  # x, y축에 대한 삼각비
            x0, y0 = tx *r, ty *r  # x, y 기준(절편) 좌표
            x1, y1 = int(x0 + w* (-ty)), int(y0 + h * tx)
            x2, y2 = int(x0 - w * (-ty)), int(y0 - h * tx)

            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 1)

    return img





