import json


def post_message(gatewayapiClient, connection_id: str, msg: str) -> None:
    gateway_resp = gatewayapiClient.post_to_connection(
        ConnectionId=connection_id, Data=json.dumps(msg)
    )
