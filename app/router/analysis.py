from flask import Blueprint, request, jsonify

from business.evaluation.evaluation import evaluation

from model.api_response import APIResponse

blue_print = Blueprint("analysis", __name__, url_prefix="/analysis")


@blue_print.route("/image", methods=["POST"])
def question():
    if request.method == 'POST':
        params = request.get_json()

        result = evaluation(params['evaluationCode'])


        return jsonify(APIResponse("success", "200", result[1], result[0]))
