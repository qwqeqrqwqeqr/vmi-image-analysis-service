from analysis.rule.rule_4 import rule_4
from analysis.rule.rule_5 import rule_5

from analysis.rule.rule_7 import rule_7
from analysis.rule.rule_8 import rule_8
from analysis.rule.rule_10 import rule_10
from analysis.rule.rule_16 import rule_16


def map_rule(number, image_path):
    if number == 4:
        # 4번 일 때
        return rule_4(image_path)
    if number == 5:
        # 5번 일 때
        return rule_5(image_path)
    if number == 7:
        # 7번 일 때
        return rule_7(image_path)
    if number == 8:
        # 8번 일 때
        return rule_8(image_path)
    if number == 10:
        # 10번 일 때
        return rule_10(image_path)
    else:  # 16번 일 때
        return rule_16(image_path)

