from business.analysis_image.rule.rule_10 import rule_10
from business.analysis_image.rule.rule_11 import rule_11
from business.analysis_image.rule.rule_12 import rule_12
from business.analysis_image.rule.rule_13 import rule_13
from business.analysis_image.rule.rule_14 import rule_14
from business.analysis_image.rule.rule_15 import rule_15
from business.analysis_image.rule.rule_16 import rule_16
from business.analysis_image.rule.rule_4 import rule_4
from business.analysis_image.rule.rule_5 import rule_5
from business.analysis_image.rule.rule_6 import rule_6
from business.analysis_image.rule.rule_7 import rule_7
from business.analysis_image.rule.rule_8 import rule_8
from business.analysis_image.rule.rule_9 import rule_9
from model.evaluation import Evaluation

'''
    유사도가 예측을 통과한 이미지들(1점) 만 규칙검사를 진행합니다.
'''


def analysis_image(image, evaluation_list: list[Evaluation]):
    for i in range(0, 12):
        if evaluation_list[i].score == 1:
            evaluation_list[i] = map_result(i+4, select_image(i+4, image))
    return evaluation_list

def map_result(number, result):
    return Evaluation(number, result[0], result[1])


def select_image(number, image):
    if number == 4:
        return rule_4(image.a_4)
    elif number == 5:
        return rule_5(image.a_5)
    elif number == 6:
        return rule_6(image.a_6)
    elif number == 7:
        return rule_7(image.a_7)
    elif number == 8:
        return rule_8(image.a_8)
    elif number == 9:
        return rule_9(image.a_9)
    elif number == 10:
        return rule_10(image.a_10)
    elif number == 11:
        return rule_11(image.a_11)
    elif number == 12:
        return rule_12(image.a_12)
    elif number == 13:
        return rule_13(image.a_13)
    elif number == 14:
        return rule_14(image.a_14)
    else:
        return rule_15(image.a_15)
