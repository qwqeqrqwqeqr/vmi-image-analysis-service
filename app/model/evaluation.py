import dataclasses


class Evaluation:
    number: int
    status: bool
    message: str

    def __init__(self, number, status, message):
        self.number = number
        self.status = status
        self.message = message

