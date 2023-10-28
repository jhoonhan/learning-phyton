import json
import boto3

URL = "https://r9mzbnosmd.execute-api.us-east-1.amazonaws.com/dev"
gatewayapiClient = boto3.client("apigatewaymanagementapi", endpoint_url=URL)
dynamoDbClient = boto3.client("dynamodb")


# Join Game
def lambda_handler(event, context):
    connectionId = event["requestContext"].get("connectionId")

    try:
        host_connection_id = json.loads(event["body"]["host_connection_id"])
        print(host_connection_id)

        response = dynamoDbClient.get_item(
            TableName="ticTacToe-games",
            Key={
                "connectionId": {"S": "NhsENdDMoAMCL0Q="},
                "guestConnectionId": {"S": "null"},
            },
        )

    except:
        return {
            "statusCode": 404,
            "body": json.dumps(
                f"404: NO GAME FOUND. Please check the host connection ID"
            ),
        }
