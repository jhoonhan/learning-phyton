from post_message import post_message


def conver_row_data(row):
    return [
        row["L"][0]["S"],
        row["L"][1]["S"],
        row["L"][2]["S"],
    ]


def display_status(state, gatewayapiClient, connection_id: str):
    rows = state["rows"]["M"]

    # print(conver_row_data(rows["row0"]))

    msg: str = f"{conver_row_data(rows['row0'])}\n{conver_row_data(rows['row1'])}\nconver_row_data(rows['row2'])"

    post_message(gatewayapiClient, connection_id, msg)
