from flask import Blueprint, request, jsonify

from business.evaluate_image.evaluate_image import evaluation
from database.query.image import set_patient_image

from model.api_response import APIResponse
from util.file import save_files

from database.query.image import get_patient_image

blue_print = Blueprint("analysis", __name__, url_prefix="/analysis")


@blue_print.route("/image", methods=["POST"])
def analysis_image():
    if request.method == 'POST':
        result = []
        evaluation_code_list = request.form.getlist('evaluationCodeList')
        files = request.files.getlist("files")

        print(request.form.get('evaluationCodeList'))
        print(evaluation_code_list)
        print(files)

        # 클라이언트로 부터 받은 파일 저장
        save_files(files)

        # 경로를 저장하고 채점을 진행합니다.
        for evaluation_code in evaluation_code_list:
            set_patient_image(evaluation_code)
            evaluation_result = evaluation(evaluation_code)
            result.append(
                {'evaluationCode': evaluation_code, 'scoreList': evaluation_result[0], 'total': evaluation_result[2]})

        return jsonify(APIResponse("success", "200", "AI 이미지 분석을 완료 하였습니다.", result))


@blue_print.route("/patient/image/list/all", methods=["POST"])
def get_patient_image_list_all():
    if request.method == 'POST':
        params = request.get_json()

        result = []
        image_list = []

        for evaluation_code in params['evaluationCodeList']:
            number = 4
            image_list.clear()
            for image in  get_patient_image(evaluation_code).get_image_list():
                image_list.append({'image': image, 'number': number})
                number += 1

            result.append({'evaluationCode': evaluation_code, 'imageList': image_list})

    return jsonify(APIResponse("success", "200", "AI 이미지 분석을 완료 하였습니다.", result))
