import json
import boto3


def lambda_handler(event, context):
    client = boto3.client("dynamodb")
    connectionId = event["requestContext"].get("connectionId")

    game_state = {
        "connectionId": {"S": connectionId},
        "Rows": {
            "M": {
                "row0": {"L": [{"S": " "}, {"S": " "}, {"S": " "}]},
                "row1": {"L": [{"S": " "}, {"S": " "}, {"S": " "}]},
                "row2": {"L": [{"S": " "}, {"S": " "}, {"S": " "}]},
            }
        },
        "game_finished": {"BOOL": False},
        "user_turn": {"BOOL": True},
        "user_turn_count": {"N": "0"},
    }

    client.put_item(
        TableName="ticTacToe-games",
        Item=game_state,
    )

    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
