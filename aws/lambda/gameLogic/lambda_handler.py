import json
import boto3

from start_game import start_game
from display_status import display_status
from post_message import post_message
from UserInput import UserInput
from Messages import Messages


# connection URL (i.e. backend URL)
URL = "https://r9mzbnosmd.execute-api.us-east-1.amazonaws.com/dev"
gatewayapiClient = boto3.client("apigatewaymanagementapi", endpoint_url=URL)
dynamoDbClient = boto3.client("dynamodb")


# Game Controller
def lambda_handler(event, context):
    Messages_Class = Messages()
    print("Step 1")

    # Get host and guest connectionIds
    connection_id = event["requestContext"].get("connectionId")

    game_table = dynamoDbClient.get_item(
        TableName="ticTacToe-games",
        Key={
            "connectionId": {"S": connection_id},
        },
    )
    print("Step 2")
    # Finds guest connection ID
    game_data = game_table["Item"]
    guest_connection_id = game_data["guestConnectionId"]["S"]

    # Finds command and execute
    event_body = json.loads(event["body"])
    # Guard clause
    print("Step 3")
    if "command" not in event_body:
        return {
            "statusCode": 404,
            "body": json.dumps("No command found"),
        }

    print("Step 4")

    #########################
    # Game Controller STARTS
    command = event_body["command"]

    # Start_game
    if command == "start_game":
        # start_game(gatewayapiClient, connection_id, guest_connection_id)
        # Displays game
        display_status(game_data, gatewayapiClient, connection_id)
        post_message(gatewayapiClient, connection_id, "")

    # Game progresses
    if command == "progress_game":
        # Ask for input
        post_message(gatewayapiClient, connection_id, "What's your move? ex:'1,2'.")

        # Log that into the table

        # Display status

    if command == "log_progress":
        # Chekcs if data was provided
        if "data_row" not in event_body or "data_col" not in event_body:
            return {
                "statusCode": 404,
                "body": json.dumps("No data was provided"),
            }

        data_row = event_body["data_row"]
        data_col = event_body["data_col"]
        print(data_row)
        print(data_col)

        # Data Validation

        validated_row_data = UserInput(Messages_Class.SELECT_COL).validation(data_row)
        validated_row_value = validated_row_data["data"]

        validated_selected_col = UserInput(
            Messages_Class.SELECTED_ROW(validated_row_value),
            validated_row_value,
        ).validation(data_col)

        # Log to table
        # log_to_table(connection_id, json_data)

    # handling if message does not exist
    return {
        "statusCode": 200,
        "body": json.dumps("Worked"),
    }


def log_to_table(connection_id: str, input):
    print(input)

    # Get current row data
    game_table = dynamoDbClient.get_item(
        TableName="ticTacToe-games",
        Key={
            "connectionId": {"S": connection_id},
        },
    )
    rows = game_table["rows"]
    print(rows["L"])

    # row_number = input["row"]
    # col_number = input["col"]
    # dynamoDbClient.update_item(
    #     TableName="ticTacToe-games",
    #     Key={
    #         "connectionId": {"S": connection_id},
    #     },
    #     UpdateExpression="SET guestConnectionId = :newGuestConnectionId",
    #     ExpressionAttributeValues={":newGuestConnectionId": {"S": connection_id}},
    #     ReturnValues="UPDATED_NEW",
    # )
