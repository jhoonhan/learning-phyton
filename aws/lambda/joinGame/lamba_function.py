import json
import boto3

URL = "https://r9mzbnosmd.execute-api.us-east-1.amazonaws.com/dev"
gatewayapiClient = boto3.client("apigatewaymanagementapi", endpoint_url=URL)
dynamoDbClient = boto3.client("dynamodb")


# Join Game
def lambda_handler(event, context):
    connectionId = event["requestContext"].get("connectionId")
    event_body = json.loads(event["body"])

    if "host_connection_id" in event_body:
        return {
            "statusCode": 200,
            "body": json.dumps(f"HOST CONNECTION: {event_body['host_connection_id']}."),
        }
    else:
        return {
            "statusCode": 404,
            "body": json.dumps(f"NO GAME FOUND"),
        }
