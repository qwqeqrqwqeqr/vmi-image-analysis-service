import cv2
import numpy as np


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
