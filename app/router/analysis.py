from flask import Blueprint, request, jsonify

from business.evaluation import evaluation
from model.api_response import APIResponse

blue_print = Blueprint("analysis", __name__, url_prefix="/analysis")

#TODO 모듈 확장시 삭제 예정
ANSWER_IMAGE_NUM_10 = 10
ANSWER_IMAGE_NUM_16 = 16

@blue_print.route("/image/question/10", methods=["POST"])
def question10():
    if request.method == 'POST':
        params = request.get_json()

        result,message = evaluation(params['evaluationCode'], ANSWER_IMAGE_NUM_10)
        score = {"score": result}

        return jsonify(APIResponse("success","200", message, score))


@blue_print.route("/image/question/16", methods=["POST"])
def question16():
    if request.method == 'POST':
        params = request.get_json()

        result,message = evaluation(params['evaluationCode'], ANSWER_IMAGE_NUM_16)

        score = {"score": result}

    return jsonify(APIResponse("success", "200",message, score))
