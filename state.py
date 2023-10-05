# State Management
game_state: dict[str, dict[str, list[str]] | bool | int] = {
    "rows": {"row0": [" ", " ", " "], "row1": [" ", " ", " "], "row2": [" ", " ", " "]},
    "game_finished": False,
    "user_turn": True,
    "user_turn_count": 0,
}

rows: list[list[str]] = [
    game_state["rows"]["row0"],
    game_state["rows"]["row1"],
    game_state["rows"]["row2"],
]

combined_state = {**game_state, **{"combined_rows": rows}}
