import dataclasses


class Evaluation:
    number: int
    score: int
    message: str

    def __init__(self, number, score, message):
        self.number = number
        self.score = score
        self.message = message

    def image_analysis_response_dto(self):
        return {'number': self.number, 'score': self.score, 'message': self.message}
