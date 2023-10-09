class Helpers:
    def __init__(self, state) -> None:
        self.state = state

    def get_user_name(self) -> str:
        if self.state["user_turn"] == True:
            return "O"
        else:
            return "X"
