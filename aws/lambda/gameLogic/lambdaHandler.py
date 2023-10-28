import json
import boto3

from start_game import start_game


# connection URL (i.e. backend URL)
URL = "https://r9mzbnosmd.execute-api.us-east-1.amazonaws.com/dev"
gatewayapiClient = boto3.client("apigatewaymanagementapi", endpoint_url=URL)
dynamoDbClient = boto3.client("dynamodb")


def lambda_handler(event, context):
    # Get host and guest connectionIds
    connectionId = event["requestContext"].get("connectionId")

    game_table = dynamoDbClient.get_item(
        TableName="ticTacToe-games",
        Key={
            "connectionId": {"S": connectionId},
        },
    )
    # Finds guest connection ID
    game_data = game_table["Item"]
    guest_connection_id = game_data["guestConnectionId"]["S"]

    # Finds command and execute
    event_body = json.loads(event["body"])
    # Guard clause
    if "command" not in event_body:
        return {
            "statusCode": 404,
            "body": json.dumps("No command found"),
        }

    command = event_body["command"]

    # Starts game
    start_game(gatewayapiClient, connectionId, guest_connection_id)

    # handling if message does not exist
