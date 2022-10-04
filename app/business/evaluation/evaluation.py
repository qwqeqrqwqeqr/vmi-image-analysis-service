# 이미지 유사도 측정과 규칙 전부 검사
from business.predict_image import predict
from database.query.image import get_patient_image
from model.evaluation import Evaluation


def evaluation(evaluation_code):
    image = get_patient_image(evaluation_code)
    evaluation_list = init_evaluation_list()
    evaluation_list = predict(image,evaluation_list)

    # evaluation_list = analysis(image,evaluation_list)

    message = "바보"
    return evaluation_list, message


def init_evaluation_list() -> list[Evaluation]:
    evaluation_list = []
    for i in range(4, 31):
        evaluation_list.append(Evaluation(i, False, ""))
    return evaluation_list


