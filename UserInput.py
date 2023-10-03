class UserInput:
    def __init__(self, message, previous_passed=True):
        self.message = message
        self.previous_passed = previous_passed

    def validation(
        self,
        user_selection,
    ):
        if (
            user_selection.isdigit() == False
            or user_selection == ""
            or user_selection == None
            or int(user_selection) >= 3
        ):
            print("\nWrong input. Must be a number and less than 3")
            return None
        else:
            return int(user_selection)

    def get_input(self):
        if self.previous_passed == None:
            return None
        else:
            user_selection = input(self.message)
            return self.validation(user_selection)
