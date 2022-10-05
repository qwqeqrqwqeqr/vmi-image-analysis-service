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

#TODO 유사도를 충족한 문제들만 규칙을 검사한다.
def analysis_image(image, evaluation_list):
    evaluation_list[4] = map_result(4, rule_4(image.a_4))
    evaluation_list[5] = map_result(5, rule_5(image.a_5))
    evaluation_list[6] = map_result(6, rule_6(image.a_6))
    evaluation_list[7] = map_result(7, rule_7(image.a_7))
    evaluation_list[8] = map_result(8, rule_8(image.a_8))
    evaluation_list[9] = map_result(9, rule_9(image.a_9))
    evaluation_list[10] = map_result(10, rule_10(image.a_10))
    evaluation_list[11] = map_result(11, rule_11(image.a_11))
    evaluation_list[12] = map_result(12, rule_12(image.a_12))
    evaluation_list[13] = map_result(13, rule_13(image.a_13))
    evaluation_list[14] = map_result(14, rule_14(image.a_14))
    evaluation_list[15] = map_result(15, rule_15(image.a_15))
    evaluation_list[16] = map_result(16, rule_16(image.a_16))

    return evaluation_list


def map_result(number, result):
    return Evaluation(number, result[0], result[1])
