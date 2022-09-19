import urllib

import cv2
import numpy as np
from math import pi, nan, isnan, degrees, sqrt, atan2

success_message = "유사도 및 규칙을 충족합니다."
def rule_10(img_path):
    score = 1
    message = ""

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
        message = "도형이 존재하지 않음"
        score = 0
    else:
        c = max(contours, key=cv2.contourArea)
        cv2.fillPoly(one_object, [c], (255, 255, 255))
        # cv2.drawContours(one_object, [c], 0, (255,255,255), 1)
        # one_object = cv2.morphologyEx(one_object, cv2.MORPH_CLOSE, kernel3, iterations=3)
        # plt.title("target")
        # plt.imshow(one_object)
        # plt.show()

        one_object = cv2.copyMakeBorder(one_object, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value=0)
        one_object_copy = one_object.copy()

        one_object = cv2.cvtColor(one_object, cv2.COLOR_RGB2GRAY)
        corners = cv2.goodFeaturesToTrack(one_object, 100, 0.25, 20, blockSize=3, useHarrisDetector=True, k=0.03)
        if corners is None:
            message = "도형 코너 검출 안됨"
            score = 0
        else:
            for corner in corners:
                coordinate = corner[0]
                coordinate = [int(i) for i in coordinate]
                cv2.circle(one_object_copy, tuple(coordinate), 3, (0, 255, 255), 2)
            # plt.title("draw corners")
            # plt.imshow(one_object_copy)
            # plt.show()
            if len(corners) != 5:
                message = "코너의 개수가 5개가 아님"
                score = 0
            else:
                points = findCenter(corners)
                if points['center'] is None:
                    message = "중심점을 찾을 수 없음"
                    score = 0
                else:
                    cv2.circle(one_object_copy, tuple(points['center']), 3, (255, 0, 255), 2)
                    # plt.title("draw center")
                    # plt.imshow(one_object_copy)
                    # plt.show()

                    length_left, degree_left = calculateLineFeatures(points['center'], points['left'])
                    if length_left < 10:
                        message = "교차점에서부터 뻗어 나온 선분의 길이가 충분하지 않음"
                        score = 0
                    elif degree_left > 20 or degree_left < -20:
                        message = "수평으로부터 20도 이상 벗어남"
                        score = 0

                    length_right, degree_right = calculateLineFeatures(points['center'], points['right'])
                    if length_right < 10:
                        message = "교차점에서부터 뻗어 나온 선분의 길이가 충분하지 않음"
                        score = 0
                    elif degree_right > 0 and degree_right < 160:
                        message = "수평으로부터 20도 이상 벗어남"
                        score = 0
                    elif degree_right < 0 and degree_right > -160:
                        message = "수평으로부터 20도 이상 벗어남"
                        score = 0

                    length_up, degree_up = calculateLineFeatures(points['center'], points['up'])
                    if degree_up < 10:
                        message = "교차점에서부터 뻗어 나온 선분의 길이가 충분하지 않음"
                        score = 0
                    elif degree_up < 70 or degree_up > 110:
                        message = "수직으로부터 20도 이상 벗어남"
                        score = 0

                    length_down, degree_down = calculateLineFeatures(points['center'], points['down'])
                    if length_down < 10:
                        message = "교차점에서부터 뻗어 나온 선분의 길이가 충분하지 않음"
                        score = 0
                    elif degree_down > -70 or degree_down < -110:
                        message = "수직으로부터 20도 이상 벗어남"
                        score = 0


    if score == 1:
        print("규칙을 충족합니다.")
        return True , success_message
    else:
        print(message)
        return False , message



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
    points['left'] = sort_by_x[0]
    points['right'] = sort_by_x[4]
    sort_by_x = sort_by_x[1:4]

    sort_by_y = sorted(corners_int, key=lambda x: (x[1], x[0]))
    points['up'] = sort_by_y[0]
    points['down'] = sort_by_y[4]
    sort_by_y = sort_by_y[1:4]

    intersection = []
    for i in sort_by_x:
        if i in sort_by_y:
            intersection.append(i)

    if len(intersection) == 1:
        points['center'] = intersection.pop()
    else:
        points['center'] = None

    return points


def calculateLineFeatures(point1, point2):
    x = point1[0] - point2[0]
    y = point1[1] - point2[1]
    length = sqrt(x * x + y * y)
    radian = atan2(y, x)
    degree = degrees(radian)

    return (length, degree)
