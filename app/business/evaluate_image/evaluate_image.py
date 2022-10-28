# 이미지 유사도 측정과 규칙 전부 검사
from business.analysis_image.analysis_image import analysis_image
from business.evaluate_image.util.init_list import init_evaluation_list, init_score_list
from business.predict_image.predict_image import predict_image
from business.test_model.test_model import get_average_performance_from_model
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
    print("================이미지를 불러옵니다================")
    image = get_patient_image(evaluation_code)


    evaluation_list = evaluation_image_list(image)

    # 채점 결과를 반영한 score_list 만들기
    print("================총점 계산을 시작합니다.================")
    score_list = init_score_list(evaluation_code, evaluation_list)

    print("총점 : ", score_list.total)
    # DB에 점수 넣기
    if update_patient_score(score_list):
        message = "분석을 완료 하였습니다."
    else:
        message = "분석을 실패 하였습니다."

    # print("================성능을 측정합니다.================")
    # performance = get_average_performance_from_model()

    return map_image_analysis_response_dto(evaluation_list), message, score_list.total


def evaluation_image_list(image) -> list[Evaluation]:
    evaluation_list = init_evaluation_list()
    print("================유사도 측정을 시작합니다.================")
    evaluation_list = predict_image(image, evaluation_list)
    print("================규칙 검사를 시작합니다.================")
    evaluation_list = analysis_image(image, evaluation_list)
    return evaluation_list


def map_image_analysis_response_dto(evaluation_list: list[Evaluation]):
    result = []
    for i in evaluation_list:
        result.append(i.image_analysis_response_dto())
    return result


