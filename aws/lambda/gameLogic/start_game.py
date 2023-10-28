from post_message import post_message


def start_game(gatewayapi_client, connection_id, guest_connection_id):
    # Starts game
    post_message(gatewayapi_client, connection_id, "Game started. You are Player Host")
    post_message(
        gatewayapi_client, guest_connection_id, "Game started. You are Player Guest"
    )
    post_message(gatewayapi_client, connection_id, "")
    post_message(gatewayapi_client, guest_connection_id, "")

    post_message(gatewayapi_client, connection_id, "Host's turn")
    post_message(gatewayapi_client, guest_connection_id, "Host's turn")
