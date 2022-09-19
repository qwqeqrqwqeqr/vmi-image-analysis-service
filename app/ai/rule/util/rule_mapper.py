from ai.rule.rule_10 import rule_10
from ai.rule.rule_16 import rule_16


def map_rule(number, image_path):
    if number == 10: #10번 일 때
        return  rule_10(image_path)
    else:  #16번 일 때
        return rule_16(image_path)

