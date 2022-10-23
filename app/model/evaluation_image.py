import dataclasses


@dataclasses
class EvaluationImage:
    number: int
    status: str
    message: str

    def __init__(self, number, status, message):
        self.number = number
        self.status = status
        self.message = message

