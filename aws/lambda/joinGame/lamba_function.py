import json
import boto3

URL = "https://r9mzbnosmd.execute-api.us-east-1.amazonaws.com/dev"
gatewayapiClient = boto3.client("apigatewaymanagementapi", endpoint_url=URL)
dynamoDbClient = boto3.client("dynamodb")


# Join Game
def lambda_handler(event, context):
    connectionId = event["requestContext"].get("connectionId")

    host_connection_id = input("Type Host's connection ID")
    print(host_connection_id)

    # dynamoDbClient.put_item(
    #     TableName="ticTacToe-games",
    #     Item=game_state,
    # )

    return {
        "statusCode": 200,
        "body": json.dumps(f"HOST CONNECTION: {host_connection_id}."),
    }
