# Tik Tak Toe
from state import combined_state as state

from UserInput import UserInput
from Helpers import Helpers
from GameLogic import GameLogic


def game_controller():
    # Controller
    while state["user_turn_count"] < 10:
        game_logic = GameLogic(state)

        # Display Game Status
        game_logic.display_game_status()

        # Validate first and second input
        validated_selected_row = UserInput("Pick a row between 0,1,2 : ").get_input()
        validated_selected_col = UserInput(
            f"\nYou have picked row {validated_selected_row}, \nPick a column between 0,1,2 : ",
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
