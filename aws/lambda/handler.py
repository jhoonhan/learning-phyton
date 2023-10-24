import json
import boto3

# connection URL (i.e. backend URL)
URL = "https://r9mzbnosmd.execute-api.us-east-1.amazonaws.com/dev"
gatewayapi = boto3.client("apigatewaymanagementapi", endpoint_url=URL)
lambdaClient = boto3.client("lambda")


# Invoke other lambda
def invokeGameLogic(functionName: str, params):
    combinedParams = {**params, functionName: functionName}
    response = lambdaClient.invoke(
        FunctionName="arn:aws:lambda:us-east-1:254832711870:function:ticTacToeWebsocket-gameLogic",
        InvocationType="RequestResponse",
        Payload=json.dumps(combinedParams),
    )
    res = json.load(response["Payload"])

    return res


def lambda_handler(event, context):
    # fetching connectionId from event
    # connectionId = event["requestContext"].get("connectionId")
    connectionId = "NUwHXe17oAMCEow="

    # loading JSON message
    msg = json.loads(event["body"])
    cmd = json.loads(event["body"])

    # Logic Allocation
    if "command" in cmd:
        command = cmd["command"]

        if command == "checkWon":
            r_msg = "checking if won"
            post_message(connectionId, r_msg)
            return {"statusCode": 200}
        elif command == "aaang":
            r_msg = "aaang"
            post_message(connectionId, r_msg)
        else:
            r_msg = "Thanks!"
            post_message(connectionId, r_msg)
            # closing the connection from server
            response = gatewayapi.delete_connection(ConnectionId=connectionId)
            return {"statusCode": 200}

    else:
        # handling if message does not exist
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Message does not exist!"}),
        }


def post_message(connectionId, msg):
    gateway_resp = gatewayapi.post_to_connection(
        ConnectionId=connectionId, Data=json.dumps({"message": msg})
    )
