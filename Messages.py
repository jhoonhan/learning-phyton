from Helpers import Helpers


class Messages:
    def __init__(self, state) -> None:
        self.state = state
        self.PICK_A_ROW = "Pick a row between 0,1,2 : "
        self.WRONG_INPUT = "\nWrong input. Must be a number and less than 3"
        self.UNAVAILABLE_COL = "\n### Unavailable. The column is already taken ###"

    def PICKED_ROW(self, validated_selected_row) -> str:
        return f"\nYou have picked row {validated_selected_row}, \nPick a column between 0,1,2 : "

    def GAME_OVER(self) -> str:
        return f"\nGAME OVER. PLAYER {Helpers(self.state).get_user_name()} WON"

    def GAME_CURRENT_TURN(self) -> str:
        return f"\nCurrent turn: {self.state['user_turn_count']}\nUser {Helpers(self.state).get_user_name()}'s turn"

    pass
