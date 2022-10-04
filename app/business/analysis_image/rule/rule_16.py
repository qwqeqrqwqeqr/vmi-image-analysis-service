import urllib

import cv2
import numpy as np
from math import pi, sqrt, atan2, degrees

from business.analysis_image.util.constants import DEFAULT_SCORE
from business.analysis_image.util.message import RULE_16_MESSAGE, RULE_PREDICT_SUCCESS_MESSAGE, RULE_SUCCESS_MESSAGE, \
    RULE_DEFAULT_MESSAGE


def rule_16(img_path):
    score = DEFAULT_SCORE
    message = RULE_DEFAULT_MESSAGE

    resp = urllib.request.urlopen(img_path)
    img = np.asarray(bytearray(resp.read()), dtype='uint8')
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)

    shape = np.shape(img)

    img = removeNoise(img, c=100)  # 이미지 노이즈 제거

    img_copy = img.copy()

    ### cv2.HoughCircles를 사용하여 원 검출하기 ###
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=22, minRadius=0, maxRadius=0)
    # print(circles)

    if circles is None or len(circles[0]) != 1:
        message = RULE_16_MESSAGE["INCORRECT_DETECTING_CIRCLE"]
        score = 0
    else:
        circles = np.uint16(np.around(circles))
        for i in circles[0]:
            cv2.circle(img_copy, (i[0], i[1]), i[2], (0, 255, 0), 2)
            center = (i[0], i[1])
            radius = i[2]

        thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)[1]
        thresh_copy = thresh.copy()
        kernel = np.ones((5, 5), np.uint8)
        binary = cv2.dilate(thresh, kernel, iterations=1)
        kernel = np.ones((3, 3), np.uint8)
        binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=3)
        blur = cv2.medianBlur(binary, 3)
        # plt.title("binary")  # 선을 두껍게 변형한 이진 이미지 출력
        # plt.imshow(binary, cmap="gray")
        # plt.show()

        mask = np.zeros((shape[0] + 2, shape[1] + 2), np.uint8)
        cv2.floodFill(binary, mask, (i[0], i[1]), 1, flags=cv2.FLOODFILL_MASK_ONLY)  # 원 검출
        mask = np.where(mask == 1, 255, 0)
        mask = mask.astype('uint8')
        mask = mask[1:shape[0] + 1, 1:shape[1] + 1]  # 원본 이미지 크기로 crop

        thresh_copy_inv = 255 - thresh_copy
        kernel = np.ones((3, 3), np.uint8)
        mask = cv2.dilate(mask, kernel, iterations=5)
        square = cv2.add(thresh_copy_inv, mask)  # 원을 제거한 새로운 이진 이미지 생성

        square = cv2.cvtColor(square, cv2.COLOR_GRAY2BGR)
        binary_padding, corners, score, message = detectOpenSquare(square)

        if score != 0:
            square_box = cv2.cvtColor(binary_padding, cv2.COLOR_GRAY2BGR)
            contours = cv2.findContours(binary_padding, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contours = contours[0] if len(contours) == 2 else contours[1]
            for c in contours:
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(square_box, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(square_box, (i[0] + 10, i[1] + 10), i[2], (0, 255, 0), 2)

            diagonal = sqrt(w * w + h * h)
            ratio = calculateRatio(diagonal, radius * 2)
            # print("ratio: ", ratio)
            if ratio >= 2:
                message = RULE_16_MESSAGE["INCORRECT_RATIO"] + " (ratio: " + str(ratio) + ")"
                score = 0
            else:
                bisector, score, message = detectBisector(square_box, corners, center)



    if score == 1:
        print(RULE_SUCCESS_MESSAGE)
        return True , RULE_PREDICT_SUCCESS_MESSAGE
    else:
        print(message)
        return False , message




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


def haveSquarePossibility(img, corners, c=20):
    min_x = 1000
    min_y = 1000
    max_x = 0
    max_y = 0
    for corner in corners:
        if min_x > corner[0][0]: min_x = corner[0][0]
        if min_y > corner[0][1]: min_y = corner[0][1]
        if max_x < corner[0][0]: max_x = corner[0][0]
        if max_y < corner[0][1]: max_y = corner[0][1]

    near_min_x = 0
    near_min_y = 0
    near_max_x = 0
    near_max_y = 0
    for corner in corners:
        if (corner[0][0] < min_x + c) and (corner[0][0] > min_x - c):
            near_min_x += 1
    for corner in corners:
        if (corner[0][1] < min_y + c) and (corner[0][1] > min_y - c):
            near_min_y += 1
    for corner in corners:
        if (corner[0][0] < max_x + c) and (corner[0][0] > max_x - c):
            near_max_x += 1
    for corner in corners:
        if (corner[0][1] < max_y + c) and (corner[0][1] > max_y - c):
            near_max_y += 1
    # print(near_min_x,near_min_y,near_max_x,near_max_y)

    if near_min_x == 2 and near_min_y == 2 and near_max_x == 2 and near_max_y == 2:
        possibility = 1
    else:
        possibility = 0

    return possibility


def detectOpenSquare(img):
    message = ""
    img = removeNoise(img, k=5, c=80)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)[1]

    kernel3 = np.ones((3, 3), np.uint8)
    kernel5 = np.ones((5, 5), np.uint8)

    binary = cv2.dilate(thresh, kernel5, iterations=1)
    binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel5, iterations=5)
    binary = cv2.blur(binary, (5, 5))
    binary = cv2.Canny(binary, 50, 50)
    binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel5, iterations=5)
    binary = cv2.dilate(binary, kernel3, iterations=1)
    binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel5, iterations=5)
    binary = cv2.erode(binary, kernel3, iterations=1)
    binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel3, iterations=5)

    square_corners = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
    square_corners = cv2.copyMakeBorder(square_corners, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value=0)
    binary_padding = cv2.copyMakeBorder(binary, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value=0)
    corners = cv2.goodFeaturesToTrack(binary_padding, 100, 0.3, 20, blockSize=3, useHarrisDetector=True, k=0.03)
    if corners is None:
        message = RULE_16_MESSAGE["NO_DETECT_ANGLE"]
        score = 0
    else:
        for corner in corners:
            coordinate = corner[0]
            coordinate = [int(i) for i in coordinate]
            cv2.circle(square_corners, tuple(coordinate), 3, (0, 255, 255), 2)

        if len(corners) != 4:
            message = RULE_16_MESSAGE["INCORRECT_VERTEX"]
            score = 0
        else:
            possibility = haveSquarePossibility(img, corners)
            if possibility == 0:
                message = RULE_16_MESSAGE["TWISTED_RECTANGLE"]
                score = 0
            else:
                score = 1

    return (binary_padding, corners, score, message)


def calculateRatio(diagonal, radius):
    if diagonal >= radius:
        ratio = diagonal / radius
    else:
        ratio = radius / diagonal

    return ratio


def calculateAngle(y, x):
    angle = atan2(y, x)

    if angle < 0:
        angle += 2 * pi

    return (180 / pi) * angle


def subtractTwoLists(list1, list2):
    result = []
    for i, j in zip(list1, list2):
        result.append(i - j)

    return result


def multiplyList(input_list, c):
    result = []
    for i in input_list:
        result.append(i * c)

    return result


def detectBisector(img, corners, center):
    message = ""

    center = [i + 10 for i in center]

    edges = []
    edges_dict = {1: [0, 0], 2: [0, 0], 3: [0, 0], 4: [0, 0]}
    for corner in corners:
        coordinates = corner[0]
        coordinates = [int(i) for i in coordinates]
        edges.append(coordinates)

    edge_min = 1000
    edge_max = 0
    for edge in edges:
        edge_sum = edge[0] + edge[1]
        if edge_sum < edge_min:
            edge_min = edge_sum
            edges_dict[1] = edge
        if edge_sum > edge_max:
            edge_max = edge_sum
            edges_dict[4] = edge

    edge23 = []
    for edge in edges:
        if edge != edges_dict[1] and edge != edges_dict[4]:
            edge23.append(edge)
    edge23.sort(key=lambda x: x[0])
    edges_dict[2] = edge23[0]
    edges_dict[3] = edge23[1]

    ### 점4(사각형에서 오른쪽 아래에 있는 점)를 기준으로 center를 점대칭 ###
    point = multiplyList(edges_dict[4], 2)
    point = subtractTwoLists(point, center)

    ### edges_dict에서 edge의 번호가 왼쪽위, 오른쪽위, 왼쪽아래, 오른쪽아래 순으로 잘 매겨졌는지 확인하는 코드 ###
    # print(edges_dict)
    cv2.circle(img, edges_dict[1], 2, (255, 0, 0), 2)
    cv2.circle(img, edges_dict[2], 2, (0, 0, 255), 2)
    cv2.circle(img, edges_dict[3], 2, (255, 255, 0), 2)
    cv2.circle(img, edges_dict[4], 2, (255, 0, 255), 2)

    ### 요구사항4 만족여부 판단을 위해 필요한 line 확인용 코드 ###
    cv2.line(img, edges_dict[4], edges_dict[2], (150, 150, 150), 2)
    cv2.line(img, edges_dict[4], edges_dict[3], (150, 150, 150), 2)
    cv2.line(img, edges_dict[4], center, (250, 190, 230), 2)
    cv2.line(img, edges_dict[4], point, (250, 190, 230), 2)

    ### 디폴트 degree 값으로 계산한 결과 ###
    line2_radian = atan2(edges_dict[4][1] - edges_dict[2][1], edges_dict[4][0] - edges_dict[2][0])
    line3_radian = atan2(edges_dict[4][1] - edges_dict[3][1], edges_dict[4][0] - edges_dict[3][0])
    center_radian = atan2(edges_dict[4][1] - center[1], edges_dict[4][0] - center[0])
    bisector_radian = atan2(edges_dict[4][1] - point[1], edges_dict[4][0] - point[0])
    line2_degree = degrees(line2_radian)
    line3_degree = degrees(line3_radian)
    center_degree = degrees(center_radian)
    bisector_degree = degrees(bisector_radian)
    # print(line2_degree, line3_degree, bisector_degree)

    if (bisector_degree > line2_degree) and (bisector_degree < line3_degree):
        score = 1
    else:
        message = RULE_16_MESSAGE["INCORRECT_SHAPE"]
        score = 0

    return (img, score, message)
