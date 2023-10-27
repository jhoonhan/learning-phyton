import json


def lambda_handler(event, context):
    functionName = event["functionName"]

    # handling if message does not exist
    return {
        "statusCode": 200,
        "body": json.dumps({"result": functionName}),
        # "body": functionName
    }
