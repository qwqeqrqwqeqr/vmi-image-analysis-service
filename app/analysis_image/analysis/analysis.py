from analysis_image.analysis.rule.rule_10 import rule_10
from analysis_image.analysis.rule.rule_11 import rule_11
from analysis_image.analysis.rule.rule_12 import rule_12
from analysis_image.analysis.rule.rule_13 import rule_13
from analysis_image.analysis.rule.rule_14 import rule_14
from analysis_image.analysis.rule.rule_15 import rule_15
from analysis_image.analysis.rule.rule_16 import rule_16
from analysis_image.analysis.rule.rule_4 import rule_4
from analysis_image.analysis.rule.rule_5 import rule_5
from analysis_image.analysis.rule.rule_6 import rule_6
from analysis_image.analysis.rule.rule_7 import rule_7
from analysis_image.analysis.rule.rule_8 import rule_8
from analysis_image.analysis.rule.rule_9 import rule_9


def analysis(image):
    result_list = []

    result_list.append(map_result(4, rule_4(image.a_4)))
    result_list.append(map_result(5, rule_5(image.a_5)))
    result_list.append(map_result(6, rule_6(image.a_6)))
    result_list.append(map_result(7, rule_7(image.a_7)))
    result_list.append(map_result(8, rule_8(image.a_8)))
    result_list.append(map_result(9, rule_9(image.a_9)))
    result_list.append(map_result(10, rule_10(image.a_10)))
    result_list.append(map_result(11, rule_11(image.a_11)))
    result_list.append(map_result(12, rule_12(image.a_12)))
    result_list.append(map_result(13, rule_13(image.a_13)))
    result_list.append(map_result(14, rule_14(image.a_14)))
    result_list.append(map_result(15, rule_15(image.a_15)))
    result_list.append(map_result(16, rule_16(image.a_16)))

    message = "이미지 분석을 완료하였습니다."
    return result_list, message


def map_result(number, result):
    return {"number": number, "result": result[0], "message": result[1]},
