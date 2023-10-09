from typing import Optional
from Messages import Messages


class UserInput:
    def __init__(self, message: str, previous_passed=0):
        self.message = message
        self.previous_passed = previous_passed

    def validation(
        self,
        user_selection: str,
    ) -> int:
        if (
            user_selection.isdigit() == False
            or user_selection == ""
            or user_selection == None
            or int(user_selection) >= 3
        ):
            print(Messages().WRONG_INPUT)

            return -1
        else:
            return int(user_selection)

    def get_input(self) -> int:
        if self.previous_passed == -1:
            return -1
        else:
            user_selection = input(self.message)
            return self.validation(user_selection)
