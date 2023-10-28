import json
import boto3

URL = "https://r9mzbnosmd.execute-api.us-east-1.amazonaws.com/dev"
gatewayapiClient = boto3.client("apigatewaymanagementapi", endpoint_url=URL)
dynamoDbClient = boto3.client("dynamodb")


# Join Game
def lambda_handler(event, context):
    connectionId = event["requestContext"].get("connectionId")
    try:
        # Locating connecting user's conenctionId and the given host connectionId
        event_body = json.loads(event["body"])
        host_connection_id = event_body["host_connection_id"]

        # Finds table based on the conenction ID and update the guestConenctionID
        dynamoDbClient.update_item(
            TableName="ticTacToe-games",
            Key={
                "connectionId": {"S": host_connection_id},
            },
            UpdateExpression="SET guestConnectionId = :newGuestConnectionId",
            ExpressionAttributeValues={":newGuestConnectionId": {"S": connectionId}},
            ReturnValues="UPDATED_NEW",
        )

        msg = f"The guest[{connectionId}] has joined. Start the game by typing in the action, 'startGame'"
        post_message(host_connection_id, msg)

        return {
            "statusCode": 200,
            "body": json.dumps(
                f"200: Connected to Game with Host ID: {host_connection_id}. \nWaiting on the host to start the game."
            ),
        }
    except:
        return {
            "statusCode": 404,
            "body": json.dumps(f"404: No game found. Please check host id."),
        }


def post_message(connectionId, msg):
    gateway_resp = gatewayapiClient.post_to_connection(
        ConnectionId=connectionId, Data=json.dumps({"data": msg})
    )
