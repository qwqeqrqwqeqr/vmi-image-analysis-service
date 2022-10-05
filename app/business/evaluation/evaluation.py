# 이미지 유사도 측정과 규칙 전부 검사
from business.analysis_image.analysis_image import analysis_image
from business.calculate_total.calculate_total import calculate_total
from business.evaluation.util.init_list import init_evaluation_list, init_score_list
from business.predict_image.predict_image import predict_image
from database.query.image import get_patient_image
from database.query.score import update_patient_score
from model.evaluation import Evaluation
from model.score import Score

'''
evaluation_list를 predict와 anlysis를 거쳐갈때마다 지속적으로 갱신합니다.
predict : AI모델을 이용한 예측
analysis: 규칙알고리즘을 이용한 이미지 분석

'''


def evaluation(evaluation_code):
    image = get_patient_image(evaluation_code)

    evaluation_list = evaluation_image_list(image)
    score_list = init_score_list(evaluation_code, evaluation_list)
    if update_patient_score(score_list):
        message = "AI 이미지 분석을 완료 하였습니다."
    else:
        message = "AI 이미지 분석을 실패 하였습니다."

    return map_image_analysis_response_dto(evaluation_list), message


def evaluation_image_list(image) -> list[Evaluation]:
    evaluation_list = init_evaluation_list()
    evaluation_list = predict_image(image, evaluation_list)
    evaluation_list = analysis_image(image, evaluation_list)
    return evaluation_list


def map_image_analysis_response_dto(evaluation_list: list[Evaluation]):
    result = []
    for i in evaluation_list:
        result.append(i.image_analysis_response_dto())
    return result
