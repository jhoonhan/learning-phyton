import json
import boto3

from start_game import start_game
from display_status import display_status
from post_message import post_message


# connection URL (i.e. backend URL)
URL = "https://r9mzbnosmd.execute-api.us-east-1.amazonaws.com/dev"
gatewayapiClient = boto3.client("apigatewaymanagementapi", endpoint_url=URL)
dynamoDbClient = boto3.client("dynamodb")


# Game Controller
def lambda_handler(event, context):
    print("Step 1")

    # Get host and guest connectionIds
    connection_id = event["requestContext"].get("connectionId")

    game_table = dynamoDbClient.get_item(
        TableName="ticTacToe-games",
        Key={
            "connectionId": {"S": connection_id},
        },
    )
    print("Step 2")
    # Finds guest connection ID
    game_data = game_table["Item"]
    guest_connection_id = game_data["guestConnectionId"]["S"]

    # Finds command and execute
    event_body = json.loads(event["body"])
    # Guard clause
    print("Step 3")
    if "command" not in event_body:
        return {
            "statusCode": 404,
            "body": json.dumps("No command found"),
        }

    print("Step 4")

    # Game Controller STARTS
    command = event_body["command"]
    print(command)

    # Start_game
    if command == "start_game":
        # start_game(gatewayapiClient, connection_id, guest_connection_id)
        display_status(game_data, gatewayapiClient, connection_id)
        post_message(gatewayapiClient, connection_id, "")

    # handling if message does not exist
    return {
        "statusCode": 200,
        "body": json.dumps("Worked"),
    }
