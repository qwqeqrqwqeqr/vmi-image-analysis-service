from flask import Blueprint, request, jsonify

from business.evaluate_image.evaluate_image import evaluation
from business.object_detection.crop_image import whitenImages
from business.preprocess_image.preprocess_image import preprocess_pdf
from database.query.image import set_patient_image

from model.api_response import APIResponse
from util.constants import ANSWER_IMAGE_DIRECTORY, ANSWER_PDF_DIRECTORY
from util.file import save_files, save_file
from flask_cors import CORS

from database.query.image import get_patient_image

blue_print = Blueprint("analysis", __name__, url_prefix="/analysis")

CORS(blue_print)


@blue_print.route("/image", methods=["POST"])
def analysis_image():
  if request.method == 'POST':
    result = []

    evaluation_code_list = request.form.getlist('evaluationCodeList')

    files = request.files.getlist("files")
    image_list = []

    for file in files:
      print(file.content_type)
      if file.content_type == "application/pdf":
        save_file(file, ANSWER_PDF_DIRECTORY)
        preprocess_pdf(file)
      if file.content_type == "image/jpeg":
        image_list.append(file)
    if len(image_list) % 27 != 0:
      return jsonify(APIResponse("fail", "400", "올바른 입력 데이터가 아닙니다.", False))

    # 경로를 저장하고 채점을 진행합니다.
    for evaluation_code in evaluation_code_list:
      set_patient_image(evaluation_code)
      evaluation_result = evaluation(evaluation_code)
      result.append(
        {'evaluationCode': evaluation_code, 'scoreList': evaluation_result[0], 'total': evaluation_result[2],
         'performance': evaluation_result[3]})

    return jsonify(APIResponse("success", "200", "AI 이미지 분석을 완료 하였습니다.", result))


@blue_print.route("/object", methods=["POST"])
def object_detection():
  if request.method == 'POST':
    result = []

    files = request.files.getlist("files")

    input_path = f"./input/"
    output_path = f"./output/"

    for file in files:
      file.save(input_path + file.filename)

    whitenImages(input_path, output_path)

  return jsonify(APIResponse("success", "200", "객체를 인식하여 추출하기를 완료하였습니다.", True))


@blue_print.route("/patient/image/list/all", methods=["POST"])
def get_patient_image_list_all():
  if request.method == 'POST':
    params = request.get_json()

    result = []
    image_list = []

    for evaluation_code in params['evaluationCodeList']:
      number = 4
      image_list.clear()
      for image in get_patient_image(evaluation_code).get_image_list():
        image_list.append({'image': image, 'number': number})
        number += 1

      result.append({'evaluationCode': evaluation_code, 'imageList': image_list})

  return jsonify(APIResponse("success", "200", "AI 이미지 분석을 완료 하였습니다.", result))
