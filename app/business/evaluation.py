# TODO 차후 모듈 확장시, param 'number' 제거

# 이미지 유사도 측정과 규칙 전부 검사
from ai.predict.util.predict_mapper import map_predict
from ai.rule.util.rule_mapper import map_rule
from database.query.image import get_patient_image


def evaluation(evaluation_code, number):
    image = get_patient_image(evaluation_code)
    image_path = "http://106.245.10.197:2323/" + find_image_path(image, number)
    # image 주소 변경
    # image_path = "http://106.245.10.197:2323/crop_ans/S330_vmi_16.jpg"

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
