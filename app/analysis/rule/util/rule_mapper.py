from analysis.rule.rule_14 import rule_14
from analysis.rule.rule_4 import rule_4
from analysis.rule.rule_5 import rule_5
from analysis.rule.rule_6 import rule_6
from analysis.rule.rule_7 import rule_7
from analysis.rule.rule_8 import rule_8
from analysis.rule.rule_9 import rule_9
from analysis.rule.rule_10 import rule_10
from analysis.rule.rule_11 import rule_11
from analysis.rule.rule_12 import rule_12
from analysis.rule.rule_13 import rule_13
from analysis.rule.rule_15 import rule_15
from analysis.rule.rule_16 import rule_16



def map_rule(number, image_path):
    if number == 4:
        # 4번 일 때
        return rule_4(image_path)
    if number == 5:
        # 5번 일 때
        return rule_5(image_path)
    if number == 6:
        # 6번 일 때
        return rule_6(image_path)
    if number == 7:
        # 7번 일 때
        return rule_7(image_path)
    if number == 8:
        # 8번 일 때
        return rule_8(image_path)
    if number == 9:
        # 9번 일 때
        return rule_9(image_path)
    if number == 10:
        # 10번 일 때
        return rule_10(image_path)
    if number == 11:
        # 11번 일 때
        return rule_11(image_path)
    if number == 12:
        # 12번 일 때
        return rule_12(image_path)
    if number == 13:
        # 13번 일 때
        return rule_13(image_path)
    if number == 14:
        # 14번 일 때
        return rule_14(image_path)
    if number == 15:
        # 15번 일 때
        return rule_15(image_path)
    else:  # 16번 일 때
        return rule_16(image_path)

