from post_message import post_message


def display_status(state, gatewayapiClient, connection_id: str):
    print(state)

    msg: str = "aaaaaaaaaaa"
    post_message(gatewayapiClient, connection_id, msg)
