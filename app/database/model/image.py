from dataclasses import dataclass


@dataclass
class Image:
    evaluation_code: int
    a_4: str
    a_5: str
    a_6: str
    a_7: str
    a_8: str
    a_9: str
    a_10: str
    a_11: str
    a_12: str
    a_13: str
    a_14: str
    a_15: str
    a_16: str
    a_17: str
    a_18: str
    a_19: str
    a_20: str
    a_21: str
    a_22: str
    a_23: str
    a_24: str
    a_25: str
    a_26: str
    a_27: str
    a_28: str
    a_29: str
    a_30: str

    def __init__(self, evaluation_code, image_dir_list):
        self.set_evaluation_code(evaluation_code)
        self.set_image(image_dir_list)

    def set_evaluation_code(self, evaluation_code):
        self.evaluation_code = evaluation_code

    def set_image(self, image_dir_list):
        self.a_4 = image_dir_list[0]
        self.a_5 = image_dir_list[1]
        self.a_6 = image_dir_list[2]
        self.a_7 = image_dir_list[3]
        self.a_8 = image_dir_list[4]
        self.a_9 = image_dir_list[5]
        self.a_10 = image_dir_list[6]
        self.a_11 = image_dir_list[7]
        self.a_12 = image_dir_list[8]
        self.a_13 = image_dir_list[9]
        self.a_14 = image_dir_list[10]
        self.a_15 = image_dir_list[11]
        self.a_16 = image_dir_list[12]
        self.a_17 = image_dir_list[13]
        self.a_18 = image_dir_list[14]
        self.a_19 = image_dir_list[15]
        self.a_20 = image_dir_list[16]
        self.a_21 = image_dir_list[17]
        self.a_22 = image_dir_list[18]
        self.a_23 = image_dir_list[19]
        self.a_24 = image_dir_list[20]
        self.a_25 = image_dir_list[21]
        self.a_26 = image_dir_list[22]
        self.a_27 = image_dir_list[23]
        self.a_28 = image_dir_list[24]
        self.a_29 = image_dir_list[25]
        self.a_30 = image_dir_list[26]
