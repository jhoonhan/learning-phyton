from typing import Optional
from Messages import Messages


class UserInput:
    def __init__(self, message: str, previous_passed=0):
        self.message = message
        self.previous_passed = previous_passed

    def validation(
        self,
        input_data: str,
    ):
        if (
            input_data.isdigit() == False
            or input_data == ""
            or input_data == None
            or int(input_data) >= 3
        ):
            return {"data": -1, "message": Messages().WRONG_INPUT}
        else:
            return {"data": int(input_data), "message": self.message}
