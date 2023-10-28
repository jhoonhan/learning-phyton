import json
from GameLogic import GameLogic
from Test import Test


# connection URL (i.e. backend URL)


def lambda_handler(event, context):
    functionName = event["functionName"]
    testStr = Test().tester()
    # Get host and guest connectionIds
    connectionId = event["requestContext"].get("connectionId")
    event_body = json.loads(event["body"])
    host_connection_id = event_body["host_connection_id"]

    # handling if message does not exist
    return {
        "statusCode": 200,
        "body": json.dumps({"result": testStr}),
        # "body": functionName
    }
