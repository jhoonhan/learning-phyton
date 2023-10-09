from Helpers import Helpers


class Messages:
    def __init__(self) -> None:
        self.PICK_A_ROW = "Pick a row between 0,1,2 : "
        self.WRONG_INPUT = "\nWrong input. Must be a number and less than 3"
        self.UNAVAILABLE_COL = "\n### Unavailable. The column is already taken ###"
        self.SELECT_COL = "Pick a row between 0,1,2 : "
        self.WRONG_INPUT = "\nWrong input. Must be a number and less than 3"

    def SELECTED_ROW(self, validated_selected_row: int) -> str:
        return f"\nYou have picked row {validated_selected_row}, \nPick a column between 0,1,2 : "

    def GAME_OVER(self, state) -> str:
        return f"\nGAME OVER. PLAYER {Helpers(state).get_user_name()} WON"

    def GAME_CURRENT_STATUS(self, state) -> str:
        return f"\nCurrent turn: {state['user_turn_count']}\nUser {Helpers(state).get_user_name()}'s turn"

    pass
