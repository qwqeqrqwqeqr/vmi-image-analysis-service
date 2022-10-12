from flask import Blueprint, request, jsonify

from database.query.image import get_patient_image
from model.api_response import APIResponse

blue_print = Blueprint("image", __name__, url_prefix="/image")


@blue_print.route("/list/all", methods=["GET"])
def analysis_image():
    if request.method == 'GET':
        params = request.get_json()

        result = []
        image_list = []

        for evaluation_code in params['evaluationCodeList']:
            number = 4
            for image in get_patient_image(evaluation_code).get_image_list():
                image_list.append({'image': image, 'number': number})
                number += 1

            result.append({'evaluationCode': evaluation_code, 'imageList': image_list})

    return jsonify(APIResponse("success", "200", "AI 이미지 분석을 완료 하였습니다.", result))
