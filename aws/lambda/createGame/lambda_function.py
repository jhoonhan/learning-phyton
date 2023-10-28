import json
import boto3

URL = "https://r9mzbnosmd.execute-api.us-east-1.amazonaws.com/dev"
gatewayapiClient = boto3.client("apigatewaymanagementapi", endpoint_url=URL)
client = boto3.client("dynamodb")


def lambda_handler(event, context):
    # print(event["requestContext"]["connectionId"])
    connectionId = event["requestContext"].get("connectionId")
    print(connectionId)

    game_state = {
        "connectionId": {"S": connectionId},
        "guestConnectionId": {"S": "null"},
        "Rows": {
            "M": {
                "row0": {"L": [{"S": " "}, {"S": " "}, {"S": " "}]},
                "row1": {"L": [{"S": " "}, {"S": " "}, {"S": " "}]},
                "row2": {"L": [{"S": " "}, {"S": " "}, {"S": " "}]},
            }
        },
        "game_started": {"BOOL": False},
        "game_finished": {"BOOL": False},
        "user_turn": {"BOOL": True},
        "user_turn_count": {"N": "0"},
    }

    client.put_item(
        TableName="ticTacToe-games",
        Item=game_state,
    )
    post_message(connectionId, "You are connected")

    return {
        "statusCode": 200,
        "body": json.dumps(
            f"Game Created. Share this connection ID with your opponent: {connectionId}."
        ),
    }


def post_message(connectionId, msg):
    gateway_resp = gatewayapiClient.post_to_connection(
        ConnectionId=connectionId, Data=json.dumps({"data": msg})
    )
