# TODO 차후 모듈 확장시, param 'number' 제거

# 이미지 유사도 측정과 규칙 전부 검사
from analysis.predict.util.predict_mapper import map_predict
from analysis.rule.util.rule_mapper import map_rule
from config.develoment import IMAGE_URL
from database.query.image import get_patient_image


def evaluation(evaluation_code, number):
    image = get_patient_image(evaluation_code)
    image_path = IMAGE_URL + find_image_path(image, number)


    print(image_path)
    result, message = map_predict(number, image_path)
    if result:
        result, message = map_rule(number, image_path)
        if result==True:
            return 1, message
        else:
            return 0, message
    else:
        return 0, message


# TODO 모듈 확장시, score 저장 부분 추가 예정


# TODO param 'number' 제거 시 같이 제거
def find_image_path(image, number):
    return {
        10: image.a_10,
        16: image.a_16
    }.get(number, )
