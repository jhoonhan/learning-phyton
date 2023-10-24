import json
import boto3

# connection URL (i.e. backend URL)
URL = "https://r9mzbnosmd.execute-api.us-east-1.amazonaws.com/dev"
gatewayapi = boto3.client("apigatewaymanagementapi", endpoint_url=URL)


def lambda_handler(event, context):
    # fetching connectionId from event
    connectionId = event["requestContext"].get("connectionId")

    # loading JSON message
    msg = json.loads(event["body"])
    cmd = json.loads(event["body"])

    # Logic Allocation
    if "command" in cmd:
        cmd = cmd["command"]

        if cmd.lower() == "checkWon":
            r_msg = "checking if won"
            post_message(connectionId, r_msg)
            return {"statusCode": 200}
        elif cmd.lower() == "aaang":
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

    # check if message key exist in payload
    if "message" in msg:
        # fetching client message
        msg = msg["message"]

        if msg.lower() == "hello":
            # response from server
            r_msg = "Hello from server!"
            # posts message to connected client
            post_message(connectionId, r_msg)
            # return statuscode
            return {"statusCode": 200}

        elif msg.lower() == "how are you":
            r_msg = "Server is fine! How are you?"
            post_message(connectionId, r_msg)
            return {"statusCode": 200}

        elif msg.lower() == "good":
            r_msg = "Great! It's nice talking to you"
            post_message(connectionId, r_msg)
            # closing the connection from server
            response = gatewayapi.delete_connection(ConnectionId=connectionId)
            return {"statusCode": 200}
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
