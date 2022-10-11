import os
import urllib.request

from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from model.api_response import APIResponse

blue_print = Blueprint("predict", __name__, url_prefix="/predict")

'''
예측을 위해 사용되는 router 입니다.
'''


@blue_print.route("/", methods=["POST"])
def predict():
    if request.method == 'POST':
        params = request.get_json()

        evaluation_code= params['evaluationCodeList']





        return jsonify(APIResponse("success", "200", "예측을 완료하였습니다.", True))




