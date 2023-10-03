class Helpers:
    def __init__(self, state):
        self.state = state

    def get_user_name(self):
        if self.state["user_turn"] == True:
            return "O"
        else:
            return "X"
