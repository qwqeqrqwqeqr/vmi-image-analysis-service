import os
import cv2
import numpy as np
import urllib

from analysis.rule.util.constants import DEFAULT_SCORE
from analysis.rule.util.message import RULE_PREDICT_SUCCESS_MESSAGE, RULE_12_MESSAGE, RULE_SUCCESS_MESSAGE, \
    RULE_DEFAULT_MESSAGE


def rule_12(img_path):
    score = DEFAULT_SCORE
    message = RULE_DEFAULT_MESSAGE

    resp = urllib.request.urlopen(img_path)
    img = np.asarray(bytearray(resp.read()), dtype='uint8')
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)


    image = removeNoise(img, c=100)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, 20, 3, 0.04)
    ret, dst = cv2.threshold(dst, 0.1 * dst.max(), 255, 0)
    dst = np.uint8(dst)
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    corners = cv2.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)
    image[dst > 0.1 * dst.max()] = [0, 0, 255]

    corner = []
    for i in range(1, len(corners)):
        corner.append(corners[i, 0])
        cv2.circle(image, (int(corners[i, 0]), int(corners[i, 1])), 7, (0, 255, 0), 2)
    # print('number of corners:', len(corner))

    if len(corner) == 4 or len_sides(img_path) == 4:
        score = 1
        message = RULE_12_MESSAGE["DETECT_CORNER_LINE"]
    elif len(corner) < 5 and len_sides(img_path) == 4:
        score = 1
        message =  RULE_12_MESSAGE["NO_DETECT_CORNER"]
    else:
        score = 0
        message =  RULE_12_MESSAGE["NO_DETECT_CORNER_LINE"]

    if score == 1:
        print(RULE_SUCCESS_MESSAGE)
        return True, RULE_PREDICT_SUCCESS_MESSAGE
    else:
        print(message)
        return False, message


def removeNoise(img, k=3, c=50):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)[1]

    kernel = np.ones((k, k), np.uint8)
    dilate = cv2.dilate(thresh, kernel, iterations=1)

    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area <= int(c):  # c값을 조절하여 노이즈 제거 강도를 조절할 수 있음
            cv2.fillPoly(img, [cnt], (255, 255, 255))

    return img


def len_sides(img_path):
    resp = urllib.request.urlopen(img_path)
    img = np.asarray(bytearray(resp.read()), dtype='uint8')
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    # Find contours and perform contour approximation
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for cnt in cnts:
        hull = cv2.convexHull(cnt)    # convex hull of contour
        hull = cv2.approxPolyDP(hull,0.1*cv2.arcLength(hull,True),True)
    # print('number of sides:',len(hull))
    return len(hull)