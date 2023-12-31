# Tik Tak Toe
from state import combined_state as state

from User_input import User_input
from Game_logic import Game_logic
from Messages import Messages


# Init AWS
# AWS Websocket

# Connection
# wss connection
# Define routes
# Validation
# Database

# User Validation
# How?


def game_controller() -> None:
    Messages_Class = Messages()
    # Controller
    while state["user_turn_count"] < 10:
        game_logic = Game_logic(state)

        # Display Game Status
        game_logic.display_game_status()

        # Validate first and second input
        validated_selected_row: int = User_input(Messages_Class.SELECT_COL).get_input()
        validated_selected_col: int = User_input(
            Messages_Class.SELECTED_ROW(validated_selected_row),
            validated_selected_row,
        ).get_input()

        ### Game Logic starts
        # Log Input
        if game_logic.is_log_succesful(validated_selected_row, validated_selected_col):
            # Display the row
            game_logic.display_rows()
            # Check if won
            if game_logic.check_won() == True:
                # If won, break out
                break
            # Increase turn count
            game_logic.increase_user_turn_count()
            # Change turn
            game_logic.switch_user_turn()


# Run the game
game_controller()


# Integrate awus
