from business.calculate_total.constants import MAX_LENGTH


def calculate_total(score):
    score_list = score.get_score_list()
    score_list = update_score_five_failure(score_list)
    score_list = update_score_not_attempt(score_list)
    return get_total(score_list)


'''
수검자가 최조로 득점한 과제 이전의 미실시 문항들도 모두 득점으로 기록한다.
(예를 들어, 7번~9번 문항의 모사 과제를 모두 성공한 경우 실시하지 않은 문항인 1번~6번 문항도 모두 성공한 것으로 간주한다.)
'''


def update_score_not_attempt(score_list):
    for index, score in enumerate(reversed(score_list)):
        if score == 1:
            score_list[0:MAX_LENGTH - index] = [1] * (MAX_LENGTH - index)
            break
    return score_list


'''
득점에 연속 5문항 실패한 이후에 다시 득점에 성공하는 문항이 있을 수도 있다. 
이 경우 수검자의 한계를 검토하기 위해 문항 채점을 계속 진행할 수는 있지만 이들 문항의 점수는 수검자의 VMI 원점수에 포함시키지 않는다.
'''


def update_score_five_failure(score_list):
    count = 0
    for index, score in enumerate(score_list):
        if score == 0:
            count += 1
        else:
            count = 0
        if count == 5:
            score_list[index:MAX_LENGTH] = [0] * (MAX_LENGTH - index)
            break
    return score_list


'''
VMI 각 문항에 대한 채점이 완성되고 나면 1점 문항의 수를 합산하여 수검자의 VMI 원점수를 산출한다.
'''


def get_total(score_list):
    total = 0
    for score in score_list:
        total += score
    return total

