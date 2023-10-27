import json
import boto3

URL = "https://r9mzbnosmd.execute-api.us-east-1.amazonaws.com/dev"
gatewayapiClient = boto3.client("apigatewaymanagementapi", endpoint_url=URL)
dynamoDbClient = boto3.client("dynamodb")


def post_message(connectionId, msg):
    gateway_resp = gatewayapiClient.post_to_connection(
        ConnectionId=connectionId, Data=json.dumps({"data": msg})
    )


def lambda_handler(event, context):
    connectionId = event["requestContext"].get("connectionId")
    dynamoDbClient.put_item(
        TableName="ticTacToe-connections",
        Item={"connectionId": {"S": connectionId},
    )

    post_message(connectionId, "You are connected")

    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
