#!/usr/bin/env python
# coding: utf-8

# 최종 수정 날짜: 2022-09-19

# 크롭한 이미지를 전처리하여 binary 이미지로 변환시켜 주는 코드입니다.



import os
import glob
import cv2
import numpy as np
import matplotlib.pyplot as plt

from config.develoment import IMAGE_URL


def showImageWithHistogram(img, title=""):
    plt.subplot(1,2,1)
    plt.imshow(img,cmap='gray')
    plt.title(title)
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(1,2,2)
    hist,bin = np.histogram(img.flatten(),256,[0,255])
    plt.xlim([0,255])
    plt.plot(hist)
    plt.title('histogram')
    plt.show()
    
    return hist




def drawLines(img, lines):
    h, w = img.shape[:2]
    #print(h, w)
    
    if lines is not None:
        for line in lines:
            r,theta = line[0]  # 거리와 각도
            tx, ty = np.cos(theta), np.sin(theta)  # x, y축에 대한 삼각비
            x0, y0 = tx*r, ty*r  # x, y 기준(절편) 좌표
            x1, y1 = int(x0 + w*(-ty)), int(y0 + h * tx)
            x2, y2 = int(x0 - w*(-ty)), int(y0 - h * tx)

            cv2.circle(img, (int(abs(x0)), int(abs(y0))), 5, (0,0,255), -1)
            #cv2.circle(img, (x1, y1), 5, (255,255,0), -1)
            #cv2.circle(img, (x2, y2), 5, (255,0,255), -1)

            cv2.line(img, (x1, y1), (x2, y2), (0,255,0), 1)
            
    return img




def calculateCropPoints(img, lines):  # 외곽선 자르기 위한 위치를 결정하는 함수
    h, w = img.shape[:2]
    
    x_start = 0
    x_end = w
    y_start = 0 
    y_end = h
    
    x_left_max = 0
    x_right_min = w
    y_up_max = 0
    y_down_min = h
    
    if lines is not None:
        for line in lines:
            r,theta = line[0]  # 거리와 각도
            tx, ty = np.cos(theta), np.sin(theta)  # x, y축에 대한 삼각비
            x0, y0 = tx*r, ty*r  # x, y 기준(절편) 좌표
            x1, y1 = int(x0 + w*(-ty)), int(y0 + h * tx)
            x2, y2 = int(x0 - w*(-ty)), int(y0 - h * tx)
            
            x0, y0 = int(abs(x0)), int(abs(y0))
            
            if x0==0 or y0==0:
                pass
            else:
                if x0 < 10: x0 = 0
                if y0 < 10: y0 = 0
            #print(x0, y0)
            
            if y0 == 0:
                if x0 < 50 and x0 > x_left_max:
                    x_left_max = x0
                elif x0 > (w-50) and x0 < x_right_min:
                    x_right_min = x0
            elif x0 == 0:
                if y0 < 50 and y0 > y_up_max:
                    y_up_max = y0
                elif y0 > (h-50) and y0 < y_down_min:
                    y_down_min = y0
                    
    x_start, x_end, y_start, y_end = x_left_max+5, x_right_min-5, y_up_max+4, y_down_min-4

    return (x_start, x_end, y_start, y_end)




def removeNoise(img, c=50, k=3):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)[1]
    
    kernel = np.ones((k,k), np.uint8)
    dilate = cv2.dilate(thresh, kernel, iterations=1)
    
    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area <= int(c):  # c값을 조절하여 노이즈 제거 강도를 조절할 수 있음
            cv2.fillPoly(img, [cnt], (255,255,255))
    
    return img




def calculateThreshValue(img):  
    hist,bin = np.histogram(img.flatten(),256,[0,255])
    hist_max = list(hist).index(max(hist))
    
    thresh = hist_max-15
    contours_min = 10000
    
    start = hist_max
    end = hist_max-30
    if end < 0: end = 0
    
    for i in range(start, end, -1):
        binary = cv2.threshold(img,i,255, cv2.THRESH_BINARY)[1]
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        #print(i, len(contours))
        
        if len(contours)!=0 and contours_min > len(contours):
            contours_min = len(contours)
            thresh = i
    
    #print("thresh: ", thresh)
    
    return thresh




def whitenImages(input_path, output_path):
    images = glob.glob(input_path + "S*.jpg")
    print(len(images))

    num = 0
    for img in images:
        num += 1

        strings = img.split('/')
        name = strings[-1]
    #     print(name)

        img = cv2.imread(img)
        img_copy = img.copy()
    #     plt.title("original")
    #     plt.imshow(img)
    #     plt.show()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 100)
        lines = cv2.HoughLines(edges, 1, np.pi/180, 98)
        img_copy = drawLines(img_copy, lines)
    #     plt.imshow(img_copy)
    #     plt.show()

        x_start, x_end, y_start, y_end = calculateCropPoints(img, lines)
        cv2.circle(img_copy, (x_start, 0), 5, (255,0,0), -1)
        cv2.circle(img_copy, (x_end, 0), 5, (255,0,0), -1)
        cv2.circle(img_copy, (0, y_start), 5, (255,0,0), -1)
        cv2.circle(img_copy, (0, y_end), 5, (255,0,0), -1)
    #     plt.imshow(img_copy)
    #     plt.show()

        crop = gray[y_start:y_end, x_start:x_end]  # 외곽선 내부의 이미지 부분만 크롭
    #     plt.title("crop")
    #     plt.imshow(crop, cmap="gray")
    #     plt.show()
    #     showImageWithHistogram(crop, "crop")

        alpha = 1.0
        crop_mean = np.mean(crop)
        contrast = np.clip((1+alpha)*crop - crop_mean*alpha, 0, 255).astype(np.uint8)
    #     contrast_hist = showImageWithHistogram(contrast, "contrast")
    #     print(contrast_hist)

        thresh = calculateThreshValue(contrast)

        binary = cv2.threshold(contrast,thresh,255, cv2.THRESH_BINARY)[1]
    #     plt.title("binary")
    #     plt.imshow(binary, cmap="gray")
    #     plt.show()

        h = binary.shape[0]
        w = binary.shape[1]
        preprocessing = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
        cv2.rectangle(preprocessing, (w-10, h-10), (w, h), (255,255,255), -1)

        preprocessing = removeNoise(preprocessing, c=80, k=7)
    #     plt.title("preprocess_image")
    #     plt.imshow(preprocess_image, cmap="gray")
    #     plt.show()



        cv2.imwrite(output_path + name, preprocessing)
        print(str(num) + "   " + name + "   " + "finish")

    print("end")




# input_path = "/home/ncyc-admin/JNotebookFolder/inhoo/Beery/module/input/"
# output_path = "/home/ncyc-admin/JNotebookFolder/inhoo/Beery/module/output/"

# whitenImages(input_path, output_path)






