# 이미지 유사도 측정과 규칙 전부 검사
from business.analysis_image.analysis_image import analysis_image
from business.predict_image.predict_image import predict_image
from database.query.image import get_patient_image
from model.evaluation import Evaluation


'''
evaluation_list를 predict와 anlysis를 거쳐갈때마다 지속적으로 갱신합니다.
predict : AI모델을 이용한 예측
analysis: 규칙알고리즘을 이용한 이미지 분석

'''
def evaluation(evaluation_code):
    image = get_patient_image(evaluation_code)
    evaluation_list = init_evaluation_list()
    evaluation_list = predict_image(image, evaluation_list)
    evaluation_list = analysis_image(image, evaluation_list)
    calculate_total()
    message = "바보"
    return evaluation_list, message


def init_evaluation_list() -> list[Evaluation]:
    evaluation_list = []
    for i in range(4, 31):
        evaluation_list.append(Evaluation(i, False, ""))
    return evaluation_list

def map_score_list(evaluation_list) -> list[evaluation]: