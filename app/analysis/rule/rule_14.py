# 요구사항:
# 1. 2개의 선이 교차할 것
# 2. 선의 각도가 각각 20도에서 70도 사이, 110도에서 160도 사이일 것
# 3. 4개의 발(legs) 중 가장 긴 것은 가장 짧은 것의 2배를 넘지 않을 것(추가된 부분은 포함시키지 않음)
# 4. 2개의 선을 교차시키지 않고 4개의 선을 각각 따로 그려서 연결한 경우 0점으로 채점
import urllib
from math import sqrt
from math import atan2
from math import degrees

import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob

from analysis.rule.util.constants import DEFAULT_SCORE
from analysis.rule.util.message import RULE_DEFAULT_MESSAGE, RULE_SUCCESS_MESSAGE, RULE_PREDICT_SUCCESS_MESSAGE, \
    RULE_14_MESSAGE


def rule_14(img_path):
    score = DEFAULT_SCORE
    message = RULE_DEFAULT_MESSAGE

    resp = urllib.request.urlopen(img_path)
    img = np.asarray(bytearray(resp.read()), dtype='uint8')
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)

    img = removeNoise(img, 20)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)[1]

    kernel3 = np.ones((3, 3), np.uint8)
    binary = cv2.dilate(thresh, kernel3, iterations=1)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    one_object = np.zeros_like(img)  # 원본과 동일한 크기의 0으로만 채워진 이미지 생성

    if not contours:
        message = RULE_14_MESSAGE["NO_FOUND_SHAPE"]
        score = 0
    else:
        c = max(contours, key=cv2.contourArea)
        cv2.fillPoly(one_object, [c], (255, 255, 255))

        one_object = cv2.copyMakeBorder(one_object, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value=0)
        one_object_copy = one_object.copy()

        one_object = cv2.cvtColor(one_object, cv2.COLOR_RGB2GRAY)
        corners = cv2.goodFeaturesToTrack(one_object, 100, 0.4, 20, blockSize=5, useHarrisDetector=True, k=0.03)
        if corners is None:
            message = RULE_14_MESSAGE["NO_DETECT_CORNER"]
            score = 0
        else:
            for corner in corners:
                coordinate = corner[0]
                coordinate = [int(i) for i in coordinate]
                cv2.circle(one_object_copy, tuple(coordinate), 3, (0, 255, 255), 2)
            if len(corners) != 5:
                message = RULE_14_MESSAGE["INCORRECT_CORNER"]
                score = 0
            else:
                points = findCenter(corners)
                if points['center'] is None:
                    message = RULE_14_MESSAGE["NO_DETECT_CENTER_POINT"]
                    score = 0
                else:
                    cv2.circle(one_object_copy, tuple(points['center']), 3, (255, 0, 255), 2)

                    length_all = []

                    length_left_up, degree_left_up = calculateLineFeatures(points['center'], points['left_up'])
                    length_all.append(length_left_up)
                    if length_left_up < 10:
                        message = RULE_14_MESSAGE["NOT_ENOUGH_CROSS_POINT"]
                        score = 0
                    elif degree_left_up < 20 or degree_left_up > 70:
                        message = RULE_14_MESSAGE["INCORRECT_ANGLE"]
                        score = 0

                    length_left_down, degree_left_down = calculateLineFeatures(points['center'], points['left_down'])
                    length_all.append(length_left_down)
                    if length_left_down < 10:
                        message = RULE_14_MESSAGE["NOT_ENOUGH_CROSS_POINT"]
                        score = 0
                    elif degree_left_down > -20 or degree_left_down < -70:
                        message = RULE_14_MESSAGE["INCORRECT_ANGLE"]
                        score = 0

                    length_right_up, degree_right_up = calculateLineFeatures(points['center'], points['right_up'])
                    length_all.append(length_right_up)
                    if length_right_up < 10:
                        message = RULE_14_MESSAGE["NOT_ENOUGH_CROSS_POINT"]
                        score = 0
                    elif degree_right_up < 110 or degree_right_up > 160:
                        message = RULE_14_MESSAGE["INCORRECT_ANGLE"]
                        score = 0

                    length_right_down, degree_right_down = calculateLineFeatures(points['center'], points['right_down'])
                    length_all.append(length_right_down)
                    if length_right_down < 10:
                        message = RULE_14_MESSAGE["NOT_ENOUGH_CROSS_POINT"]
                        score = 0
                    elif degree_right_down > -110 or degree_right_down < -160:
                        message = RULE_14_MESSAGE["INCORRECT_ANGLE"]
                        score = 0

                    length_max = 0
                    length_min = 10000
                    for l in length_all:
                        if length_max < l:
                            length_max = l
                        if length_min > l:
                            length_min = l

                    if length_max / length_min > 2:
                        message = RULE_14_MESSAGE["INCORRECT_LENGTH"]
                        score = 0

    if score == 1:
        print(RULE_SUCCESS_MESSAGE)
        return True, RULE_PREDICT_SUCCESS_MESSAGE
    else:
        print(message)
        return False, message


def removeNoise(img, c=50):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)[1]

    kernel = np.ones((3, 3), np.uint8)
    dilate = cv2.dilate(thresh, kernel, iterations=1)

    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area <= int(c):  # c값을 조절하여 노이즈 제거 강도를 조절할 수 있음
            cv2.fillPoly(img, [cnt], (255, 255, 255))

    return img


def findCenter(corners):
    corners_int = []
    for corner in corners:
        coordinate = corner[0]
        coordinate = [int(i) for i in coordinate]
        corners_int.append(coordinate)

    points = {}

    sort_by_x = sorted(corners_int, key=lambda x: (x[0], x[1]))

    if sort_by_x[0][1] < sort_by_x[1][1]:
        points['left_up'] = sort_by_x[0]
        points['left_down'] = sort_by_x[1]
    else:
        points['left_up'] = sort_by_x[1]
        points['left_down'] = sort_by_x[0]

    if sort_by_x[3][1] < sort_by_x[4][1]:
        points['right_up'] = sort_by_x[3]
        points['right_down'] = sort_by_x[4]
    else:
        points['right_up'] = sort_by_x[4]
        points['right_down'] = sort_by_x[3]

    sort_by_y = sorted(corners_int, key=lambda x: (x[1], x[0]))

    if sort_by_x[2] == sort_by_y[2]:
        points['center'] = sort_by_x[2]

    return points


def calculateLineFeatures(point1, point2):
    x = point1[0] - point2[0]
    y = point1[1] - point2[1]
    length = sqrt(x * x + y * y)
    radian = atan2(y, x)
    degree = degrees(radian)

    return (length, degree)
