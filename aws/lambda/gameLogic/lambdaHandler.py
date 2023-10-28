import json
import boto3


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
    game_data = game_table["Item"]
    guest_connection_id = game_data["guestConnectionId"]["S"]

    # Starts game
    post_message(connectionId, "Game started. You are Player 0")
    post_message(guest_connection_id, "Game started. You are Player 1")

    # handling if message does not exist
    return {
        "statusCode": 200,
        "body": json.dumps("workx"),
        # "body": functionName
    }


def post_message(connectionId, msg):
    gateway_resp = gatewayapiClient.post_to_connection(
        ConnectionId=connectionId, Data=json.dumps(msg)
    )
