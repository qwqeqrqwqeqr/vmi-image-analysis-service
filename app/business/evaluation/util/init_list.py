from business.calculate_total.calculate_total import calculate_total
from model.evaluation import Evaluation
from model.score import Score


def init_evaluation_list() -> list[Evaluation]:
    evaluation_list = []
    for i in range(4, 31):
        evaluation_list.append(Evaluation(i, 0, ""))
    return evaluation_list


def init_score_list(evaluation_code: int, evaluation_list: list[Evaluation]) -> Score:
    score_list = []
    for i in evaluation_list:

        score_list.append(i.score)
    score = Score(evaluation_code, score_list)
    score.set_total(calculate_total(score))

    return score
