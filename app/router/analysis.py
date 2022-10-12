import os

import cv2
from flask import Blueprint, request, jsonify
from w3lib import form

from business.evaluate_image.evaluate_image import evaluation
from database.query.image import set_patient_image

from model.api_response import APIResponse
from util.constants import ANSWER_IMAGE_DIRECTORY

blue_print = Blueprint("analysis", __name__, url_prefix="/analysis")


@blue_print.route("/image", methods=["POST"])
def analysis_image():
    if request.method == 'POST':
        result = []
        evaluationCodeList = request.form.getlist('evaluationCodeList')
        files = request.files.getlist("files")

        for file in files:
            print(ANSWER_IMAGE_DIRECTORY+"/"+file.filename)
            file.save(ANSWER_IMAGE_DIRECTORY+"/"+file.filename)

        set_patient_image(1)

        for evaluationCode in evaluationCodeList:
            result.append({'evaluationCode': evaluationCode, 'score': evaluation(evaluationCode)[0]})

        return jsonify(APIResponse("success", "200", "AI 이미지 분석을 완료 하였습니다.", result))



