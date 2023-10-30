import json
import boto3


def lambda_handler(event, context):
    client = boto3.client("dynamodb")
    client.delete_item(
        TableName="ticTacToe-connections",
        Key={"connectionId": {"S": event["requestContext"].get("connectionId")}},
    )
    client.delete_item(
        TableName="ticTacToe-games",
        Key={"connectionId": {"S": event["requestContext"].get("connectionId")}},
    )

    # TODO implement
    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
