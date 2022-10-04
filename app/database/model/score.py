from dataclasses import dataclass


@dataclass
class Score:
    evaluation_code: int
    q_4: int
    q_5: int
    q_6: int
    q_7: int
    q_8: int
    q_9: int
    q_10: int
    q_11: int
    q_12: int
    q_13: int
    q_14: int
    q_15: int
    q_16: int
    q_17: int
    q_18: int
    q_19: int
    q_20: int
    q_21: int
    q_22: int
    q_23: int
    q_24: int
    q_25: int
    q_26: int
    q_27: int
    q_28: int
    q_29: int
    q_30: int
    total: int

    def __init__(self, evaluation_code, score_list):
        self.set_evaluation_code(evaluation_code)
        self.set_score(score_list)

    def set_evaluation_code(self, evaluation_code):
        self.evaluation_code = evaluation_code

    def set_total(self, total):
        self.total = total

    def set_score(self, score_list):
        self.q_4 = score_list[0]
        self.q_5 = score_list[1]
        self.q_6 = score_list[2]
        self.q_7 = score_list[3]
        self.q_8 = score_list[4]
        self.q_9 = score_list[5]
        self.q_10 = score_list[6]
        self.q_11 = score_list[7]
        self.q_12 = score_list[8]
        self.q_13 = score_list[9]
        self.q_14 = score_list[10]
        self.q_15 = score_list[11]
        self.q_16 = score_list[12]
        self.q_17 = score_list[13]
        self.q_18 = score_list[14]
        self.q_19 = score_list[15]
        self.q_20 = score_list[16]
        self.q_21 = score_list[17]
        self.q_22 = score_list[18]
        self.q_23 = score_list[19]
        self.q_24 = score_list[20]
        self.q_25 = score_list[21]
        self.q_26 = score_list[22]
        self.q_27 = score_list[23]
        self.q_28 = score_list[24]
        self.q_29 = score_list[25]
        self.q_30 = score_list[26]

    def get_score_list(self):
        return [self.q_4, self.q_5, self.q_6, self.q_7, self.q_8, self.q_9, self.q_10, self.q_11, self.q_12,
                self.q_13, self.q_14, self.q_15, self.q_16, self.q_17, self.q_18, self.q_19, self.q_20, self.q_21,
                self.q_22, self.q_23, self.q_24, self.q_25, self.q_26, self.q_27, self.q_28, self.q_29, self.q_30]
