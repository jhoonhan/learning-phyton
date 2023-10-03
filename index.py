# Tik Tak Toe
WON_SEQUENCE = ["OOO", "XXX"]

# State Management
game_state = {
    "rows": {"row0": [" ", " ", " "], "row1": [" ", " ", " "], "row2": [" ", " ", " "]},
    "game_finished": False,
    "user_turn": True,
    "user_turn_count": 0,
}

rows = [
    game_state["rows"]["row0"],
    game_state["rows"]["row1"],
    game_state["rows"]["row2"],
]


class Helpers:
    def get_user_name(self):
        if game_state["user_turn"] == True:
            return "O"
        else:
            return "X"


class InputController:
    def __init__(
        self,
        message,
    ):
        self.message = message

    def validation(self, user_selection):
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
        user_selection = input(self.message)
        result = self.validation(user_selection)

        if result != None:
            return result
        else:
            return None


class GameLogic:
    def __init__(self, user_turn, row, column):
        self.user_turn = user_turn
        self.row = row
        self.column = column

    def log_user_input(self):
        # Guard
        if rows[self.row][self.column] != " ":
            print("\n### Unavailable. The column is already taken ###")
            return False
        # Based on User turn,
        if self.user_turn == True:
            rows[self.row][self.column] = "O"
        else:
            rows[self.row][self.column] = "X"
        return True

    def check_won(self):
        game_finished = game_state["game_finished"]
        # Horizontal
        for row in rows:
            joined_row = "".join(row)

            if joined_row in WON_SEQUENCE:
                game_finished = True
                break
        pass

        # Vertical
        i = 0
        while i < 3:
            joined_row = (
                game_state["rows"]["row0"][i]
                + game_state["rows"]["row1"][i]
                + game_state["rows"]["row2"][i]
            )

            i += 1
            if joined_row in WON_SEQUENCE:
                game_finished = True
                break

        # Diagonal
        sequence_1 = (
            game_state["rows"]["row0"][0]
            + game_state["rows"]["row1"][1]
            + game_state["rows"]["row2"][2]
        )
        sequence_2 = (
            game_state["rows"]["row0"][2]
            + game_state["rows"]["row1"][1]
            + game_state["rows"]["row2"][0]
        )
        if sequence_1 in WON_SEQUENCE or sequence_2 in WON_SEQUENCE:
            game_finished = True
        return game_finished

    def display_rows(self):
        print("\n")
        print(rows[0])
        print(rows[1])
        print(rows[2])

    def increase_user_turn_count(self):
        game_state["user_turn_count"] += 1

    def switch_user_turn(self):
        game_state["user_turn"] = not game_state["user_turn"]


# Controller

while game_state["user_turn_count"] < 10:
    print(f"\nCurrent turn: {game_state['user_turn_count']}")

    input_controller = InputController("Pick a row between 0,1,2 : ")
    print(f"User {Helpers().get_user_name()}'s turn")

    # Validate first input
    passed_first = input_controller.get_input()

    # Validate second input IF first validation succesful
    passed_second = None
    if passed_first != None:
        passed_second = InputController(
            f"\nYou have picked row {passed_first}, \nPick a column between 0,1,2 : "
        ).get_input()
    else:
        pass

    # All pased. Log the result, change turn, and add turn count
    if passed_first != None and passed_second != None:
        # Log result
        # loggable = log_user_input(user_turn, passed_first, passed_second)
        game_logic = GameLogic(game_state["user_turn"], passed_first, passed_second)
        is_loggable = game_logic.log_user_input()

        if is_loggable != False:
            # Display the row
            game_logic.display_rows()

            # Check if won
            if game_logic.check_won() == True:
                # If won, break out
                print("\n")
                print(f"GAME OVER. PLAYER {Helpers().get_user_name()} WON")
                break

            # Increase turn count
            game_logic.increase_user_turn_count()

            # Change turn
            game_logic.switch_user_turn()

    # First validation failed
    else:
        pass
