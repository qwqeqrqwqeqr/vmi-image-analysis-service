# TODO 차후 모듈 확장시, param 'number' 제거

# 이미지 유사도 측정과 규칙 전부 검사
from analysis_image.analysis.analysis import analysis
from database.query.image import get_patient_image


def evaluation(evaluation_code):
    image = get_patient_image(evaluation_code)

    # print(image)
    # result, message = map_predict(number, image_path)
    # if result:
    #     result, message = map_rule(number, image_path)
    #     if result==True:
    #         return 1, message
    #     else:
    #         return 0, message
    # else:
    #     return 0, message

    result, message = analysis(image)
    return result, message



# TODO 2022-09-30
# TODO 1. input -> evaluation code  (
# TODO 2. 문항별 각기 다른 학습 및 로직 적용 (mapping)
# TODO 3. 문항별 학습 및 분석 시작 (병렬 처리?)
# TODO 4. 문항별 학습 결과 (message,score) concat 하기
# TODO 5. output -> score list from to analysis_image
