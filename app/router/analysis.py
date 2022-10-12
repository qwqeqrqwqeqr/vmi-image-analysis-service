import os

import cv2
from flask import Blueprint, request, jsonify
from w3lib import form

from business.evaluate_image.evaluate_image import evaluation
from database.query.image import set_patient_image

from model.api_response import APIResponse
from util.constants import ANSWER_IMAGE_DIRECTORY
from util.file import save_files

blue_print = Blueprint("analysis", __name__, url_prefix="/analysis")


@blue_print.route("/image", methods=["POST"])
def analysis_image():
    if request.method == 'POST':
        result = []
        evaluationCodeList = request.form.getlist('evaluationCodeList')
        files = request.files.getlist("files")

        # 클라이언트로 부터 받은 파일 저장
        save_files(files)

        #경로를 저장하고 채점을 진행합니다.
        for evaluationCode in evaluationCodeList:
            set_patient_image(evaluationCode)
            evaluation_result = evaluation(evaluationCode)
            result.append({'evaluationCode': evaluationCode, 'scoreList': evaluation_result[0], 'total': evaluation_result[2]})

        return jsonify(APIResponse("success", "200", "AI 이미지 분석을 완료 하였습니다.", result))
