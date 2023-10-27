import json
import GameLogic


# connection URL (i.e. backend URL)


def lambda_handler(event, context):
    functionName = event["functionName"]

    # handling if message does not exist
    return {
        "statusCode": 200,
        "body": json.dumps({"result": functionName}),
        # "body": functionName
    }
