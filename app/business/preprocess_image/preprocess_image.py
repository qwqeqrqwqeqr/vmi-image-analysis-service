import os

import cv2
import numpy as np
import matplotlib.pyplot as plt
from pdf2image import convert_from_path

from business.preprocess_image.white import  whiten_image
from util.constants import ANSWER_PDF_DIRECTORY, ANSWER_IMAGE_DIRECTORY
from util.file import save_files


def preprocess_pdf(file):
  print("================pdf 파일을 크롭합니다.================")
  file_name = file.filename.split('.')[-2]
  print(file_name)
  pages = convert_from_path(ANSWER_PDF_DIRECTORY+"/"+file_name+".pdf", fmt='jpeg')
  image_list = []

  page_num = len(pages)
  for page in pages:
    page_name = file_name + "_" + str(page_num) + ".jpg"
    page_num -= 1

    page_img = np.array(page)

    if page_num == 0:
      qnum = 4
      crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
      print("전처리 완료 :"+crop_name)
      crop = page_img[1650:1935, 385:695]
      whiten_image(crop,crop_name)


      qnum = 5
      crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
      print("전처리 완료 :"+crop_name)
      crop = page_img[1650:1935, 658:968]
      whiten_image(crop,crop_name)

      qnum = 6
      crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
      print("전처리 완료 :"+crop_name)
      crop = page_img[1650:1935, 933:1243]
      whiten_image(crop,crop_name)

      qnum = 7
      crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
      print("전처리 완료 :"+crop_name)
      crop = page_img[995:1280, 385:695]
      whiten_image(crop,crop_name)

      qnum = 8
      crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
      print("전처리 완료 :"+crop_name)
      crop = page_img[995:1280, 658:968]
      whiten_image(crop,crop_name)


      qnum = 9
      crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
      print("전처리 완료 :"+crop_name)
      crop = page_img[995:1280, 933:1243]
      whiten_image(crop,crop_name)


      qnum = 10
      crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
      print("전처리 완료 :"+crop_name)
      crop = page_img[370:655, 385:695]
      whiten_image(crop,crop_name)

      qnum = 11
      crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
      print("전처리 완료 :"+crop_name)
      crop = page_img[370:655, 658:968]
      whiten_image(crop,crop_name)


      qnum = 12
      crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
      print("전처리 완료 :"+crop_name)
      crop = page_img[370:655, 933:1243]
      whiten_image(crop,crop_name)

    else:
      qnum = 4 + 9 * (int(page_num))
      crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
      print("전처리 완료 :"+crop_name)
      crop = page_img[1675:1970, 385:695]
      whiten_image(crop,crop_name)

      qnum = 5 + 9 * (int(page_num))
      crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
      print("전처리 완료 :"+crop_name)
      crop = page_img[1675:1970, 658:968]
      whiten_image(crop,crop_name)

      qnum = 6 + 9 * (int(page_num))
      crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
      print("전처리 완료 :"+crop_name)
      crop = page_img[1675:1970, 933:1243]
      whiten_image(crop,crop_name)

      qnum = 7 + 9 * (int(page_num))
      crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
      print("전처리 완료 :"+crop_name)
      crop = page_img[1015:1300, 385:695]
      whiten_image(crop,crop_name)

      qnum = 8 + 9 * (int(page_num))
      crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
      print("전처리 완료 :"+crop_name)
      crop = page_img[1015:1300, 658:968]
      whiten_image(crop,crop_name)

      qnum = 9 + 9 * (int(page_num))
      crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
      print("전처리 완료 :"+crop_name)
      crop = page_img[1015:1300, 933:1243]
      whiten_image(crop,crop_name)

      qnum = 10 + 9 * (int(page_num))
      crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
      print("전처리 완료 :"+crop_name)
      crop = page_img[340:625, 385:695]
      whiten_image(crop,crop_name)

      qnum = 11 + 9 * (int(page_num))
      crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
      print("전처리 완료 :"+crop_name)
      crop = page_img[340:625, 658:968]
      whiten_image(crop, crop_name)


      qnum = 12 + 9 * (int(page_num))
      crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
      print("전처리 완료 :"+crop_name)
      crop = page_img[340:625, 933:1243]
      whiten_image(crop,crop_name)

  for i in range(22 ,31):
    empty_file = cv2.imread("./static/empty_image.jpg")
    print("전처리 완료 :"+ANSWER_IMAGE_DIRECTORY + "/" + file_name + "_vmi_" + str(i) + ".jpg")
    cv2.imwrite(ANSWER_IMAGE_DIRECTORY + "/" + file_name + "_vmi_" + str(i) + ".jpg", empty_file)

  print("finish")
