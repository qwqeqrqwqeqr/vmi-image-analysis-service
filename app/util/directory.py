import os
from flask import Blueprint, request, jsonify
from werkzeug.datastructures import ImmutableMultiDict, FileStorage

from util.constants import ANSWER_IMAGE_DIRECTORY




def create_directory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: 디렉터리 생성을 실패 하였습니다, 디렉터리 명 :' + directory)


def init_directory(evaluation_code, files : list[ImmutableMultiDict[str, FileStorage]]):
    create_directory(ANSWER_IMAGE_DIRECTORY)
    for file in files:
        file.sa

