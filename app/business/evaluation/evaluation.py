# TODO 차후 모듈 확장시, param 'number' 제거

# 이미지 유사도 측정과 규칙 전부 검사
from business.analysis_image.analysis.analysis import analysis
from database.query.image import get_patient_image


def evaluation(evaluation_code):
    image = get_patient_image(evaluation_code)



    result, message = analysis(image)
    return result, message
