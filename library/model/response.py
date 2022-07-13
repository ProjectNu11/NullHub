from typing import Any


class GenericResponse:
    status: int
    message: str
    data: Any

    def __init__(self, status: int, message: str, data):
        self.status = status
        self.message = message
        self.data = data

    def __str__(self):
        return str(self.__dict__)


class GenericError(GenericResponse):
    def __init__(self, status, message):
        super().__init__(status, message, None)


class GenericSuccess(GenericResponse):
    def __init__(self, data):
        super().__init__(200, "Success", data)
