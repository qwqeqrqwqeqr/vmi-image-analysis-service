import numpy as np
import matplotlib.pyplot as plt
from pdf2image import convert_from_path


def convert_PDF(file):
  file_name = file.split('.')[-2]
  file_name = file_name.split('/')[-1]
  #     print(file_name)

  pages = convert_from_path(file, fmt='jpeg')

  page_num = len(pages)
  for page in pages:
    page_name = file_name + "_" + str(page_num) + ".jpg"
    page_num -= 1
    #         print(page_name)

    page_img = np.array(page)
    #         plt.imshow(page_img)
    #         plt.show()

    qnum = 4 + 9 * (int(page_num))
    crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
    print(crop_name)
    crop = page_img[1690:1920, 440:680]
    plt.imshow(crop)
    plt.show()
    #     cv2.imwrite("crop/" + crop_name, crop)

    qnum = 5 + 9 * (int(page_num))
    crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
    print(crop_name)
    crop = page_img[1690:1920, 700:940]
    plt.imshow(crop)
    plt.show()
    #     cv2.imwrite("crop/" + crop_name, crop)

    qnum = 6 + 9 * (int(page_num))
    crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
    print(crop_name)
    crop = page_img[1690:1920, 960:1200]
    plt.imshow(crop)
    plt.show()
    #     cv2.imwrite("crop/" + crop_name, crop)

    qnum = 7 + 9 * (int(page_num))
    crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
    print(crop_name)
    crop = page_img[1030:1260, 440:680]
    plt.imshow(crop)
    plt.show()
    #     cv2.imwrite("crop/" + crop_name, crop)

    qnum = 8 + 9 * (int(page_num))
    crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
    print(crop_name)
    crop = page_img[1030:1260, 700:940]
    plt.imshow(crop)
    plt.show()
    #     cv2.imwrite("crop/" + crop_name, crop)

    qnum = 9 + 9 * (int(page_num))
    crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
    print(crop_name)
    crop = page_img[1030:1260, 960:1200]
    plt.imshow(crop)
    plt.show()
    #     cv2.imwrite("crop/" + crop_name, crop)

    qnum = 10 + 9 * (int(page_num))
    crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
    print(crop_name)
    crop = page_img[370:600, 440:680]
    plt.imshow(crop)
    plt.show()
    #     cv2.imwrite("crop/" + crop_name, crop)

    qnum = 11 + 9 * (int(page_num))
    crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
    print(crop_name)
    crop = page_img[370:600, 700:940]
    plt.imshow(crop)
    plt.show()
    #     cv2.imwrite("crop/" + crop_name, crop)

    qnum = 12 + 9 * (int(page_num))
    crop_name = file_name + "_vmi_" + str(qnum) + ".jpg"
    print(crop_name)
    crop = page_img[370:600, 960:1200]
    print(crop)

  #     cv2.imwrite("crop/" + crop_name, crop)

  print("finish")
