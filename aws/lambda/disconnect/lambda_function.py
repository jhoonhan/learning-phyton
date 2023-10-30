import json
import boto3


def lambda_handler(event, context):
    client = boto3.client("dynamodb")

    # Delets connection ID
    client.delete_item(
        TableName="ticTacToe-connections",
        Key={"connectionId": {"S": event["requestContext"].get("connectionId")}},
    )
    # Deletes game
    client.delete_item(
        TableName="ticTacToe-games",
        Key={"connectionId": {"S": event["requestContext"].get("connectionId")}},
    )

    # TODO implement
    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
