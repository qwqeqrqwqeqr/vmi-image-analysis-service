import dataclasses


class Evaluation:
    number: int
    score: int
    message: str

    def __init__(self, number, score, message):
        self.number = number
        self.score = score
        self.message = message

