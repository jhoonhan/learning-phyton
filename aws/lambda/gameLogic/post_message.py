import json


def post_message(gatewayapiClient, connectionId, msg):
    gateway_resp = gatewayapiClient.post_to_connection(
        ConnectionId=connectionId, Data=json.dumps(msg)
    )
