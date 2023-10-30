from Messages import Messages

WON_SEQUENCE: list[str] = ["OOO", "XXX"]


class Game_logic:
    def __init__(self, state):
        self.state = state
        self.user_turn: bool = state["user_turn"]
        self.Messages_Class = Messages()

    # Display Functions
    def display_game_status(self) -> None:
        print(self.Messages_Class.GAME_CURRENT_STATUS(self.state))

    def display_rows(self) -> None:
        print("\n")
        print(self.state["combined_rows"][0])
        print(self.state["combined_rows"][1])
        print(self.state["combined_rows"][2])

    # Game Logics
    def increase_user_turn_count(self) -> None:
        self.state["user_turn_count"] += 1

    def switch_user_turn(self) -> None:
        self.state["user_turn"] = not self.state["user_turn"]

    def check_won(self) -> bool:
        # Class declaration
        Check_Won_Class = Check_Won(self.state)
        # Horizontal
        Check_Won_Class.check_horizontal()

        # Vertical
        Check_Won_Class.check_vertical()

        # Diagonal
        Check_Won_Class.check_diagonal()

        # Game Over Message
        if self.state["game_finished"] == True:
            print(self.Messages_Class.GAME_OVER(self.state))

        return self.state["game_finished"]

    def is_all_passed(self, selected_row: int, selected_col: int) -> bool:
        if selected_row != -1 and selected_col != -1:
            return True
        else:
            return False

    def is_log_succesful(self, selected_row: int, selected_col: int) -> bool:
        if self.is_all_passed(selected_row, selected_col) == False:
            return False
        # Guard
        if self.state["combined_rows"][selected_row][selected_col] != " ":
            print(self.Messages_Class.UNAVAILABLE_COL)
            return False
        # Based on User turn,
        if self.user_turn == True:
            self.state["combined_rows"][selected_row][selected_col] = "O"
        else:
            self.state["combined_rows"][selected_row][selected_col] = "X"
        return True


# Refactor for check_won
class Check_Won:
    def __init__(self, state) -> None:
        self.state = state

    # Horizontal
    def check_horizontal(self) -> None:
        for row in self.state["combined_rows"]:
            joined_row = "".join(row)

            if joined_row in WON_SEQUENCE:
                self.state["game_finished"] = True
                break
        pass

    # Vertical
    def check_vertical(self) -> None:
        i = 0
        while i < 3:
            joined_row = (
                self.state["rows"]["row0"][i]
                + self.state["rows"]["row1"][i]
                + self.state["rows"]["row2"][i]
            )

            i += 1
            if joined_row in WON_SEQUENCE:
                self.state["game_finished"] = True
                break

    # Diagonal
    def check_diagonal(self) -> None:
        sequence_1 = (
            self.state["rows"]["row0"][0]
            + self.state["rows"]["row1"][1]
            + self.state["rows"]["row2"][2]
        )
        sequence_2 = (
            self.state["rows"]["row0"][2]
            + self.state["rows"]["row1"][1]
            + self.state["rows"]["row2"][0]
        )
        if sequence_1 in WON_SEQUENCE or sequence_2 in WON_SEQUENCE:
            self.state["game_finished"] = True
