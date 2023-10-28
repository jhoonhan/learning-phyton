from post_message import post_message


def conver_row_data(row):
    return [
        row["L"][0]["S"],
        row["L"][1]["S"],
        row["L"][2]["S"],
    ]


def display_status(state, gatewayapiClient, connection_id: str):
    rows = state["rows"]["M"]
    user_turn: bool = state["user_turn"]["BOOL"]
    user_turn_name: str = "Host"
    if user_turn:
        user_turn_name = "Host"
    else:
        user_turn_name = "Guest"

    print(state)

    # print(conver_row_data(rows["row0"]))

    status_board: str = f"\n{conver_row_data(rows['row0'])}\n{conver_row_data(rows['row1'])}\n{conver_row_data(rows['row2'])}"

    msg: str = (
        f"\n{status_board}\nUSER TURN: {user_turn_name}\nInput your choice. ex: 1,1"
    )

    # status_turn: str =

    post_message(gatewayapiClient, connection_id, msg)
