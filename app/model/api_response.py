from dataclasses import dataclass
from typing import TypeVar

'''
    status: success or fail
    message : message
    resultCode: 200,400,403,...
    data : result data
'''
@dataclass
class APIResponse:
    status: str
    resultCode: str
    message: str
    data: TypeVar('T')

    def __init__(self, status, result_code, message, data):
        self.status = status
        self.message = message
        self.resultCode = result_code
        self.data = data
