from flask import Blueprint, request, jsonify

from business.evaluate_image.evaluate_image import evaluation

from model.api_response import APIResponse

blue_print = Blueprint("analysis", __name__, url_prefix="/analysis")


@blue_print.route("/image", methods=["POST"])
def analysis_image():
    if request.method == 'POST':
        params = request.get_json()
        result = []
        evaluationCodeList = params['evaluationCodeList']

        for evaluationCode in evaluationCodeList:
            result.append({'evaluationCode': evaluationCode, 'score': evaluation(evaluationCode)[0]})

        return jsonify(APIResponse("success", "200", "AI 이미지 분석을 완료 하였습니다.", result))
