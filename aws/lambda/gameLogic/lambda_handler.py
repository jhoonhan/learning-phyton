import json
import boto3

from start_game import start_game
from display_status import display_status
from post_message import post_message
from User_input import User_input
from Messages import Messages
from Game_logic import Game_logic


# connection URL (i.e. backend URL)
URL = "https://r9mzbnosmd.execute-api.us-east-1.amazonaws.com/dev"
gatewayapiClient = boto3.client("apigatewaymanagementapi", endpoint_url=URL)
dynamoDbClient = boto3.client("dynamodb")


# Game Controller
def lambda_handler(event, context):
    Messages_Class = Messages()
    # Get host and guest connectionIds
    connection_id = event["requestContext"].get("connectionId")

    # State declaration
    game_table = dynamoDbClient.get_item(
        TableName="ticTacToe-games",
        Key={
            "connectionId": {"S": connection_id},
        },
    )
    state = game_table["Item"]
    print("Step 2")

    # Finds guest connection ID
    guest_connection_id = state["guestConnectionId"]["S"]

    #
    #
    # Finds command and execute
    event_body = json.loads(event["body"])
    ## Guard clause
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
        display_status(state, gatewayapiClient, connection_id)
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

        # Data Validation
        validated_row_data = User_input(
            Messages_Class.SELECT_COL,
        ).validation(data_row)
        validated_col_data = User_input(
            Messages_Class.SELECTED_ROW(validated_row_data["value"]),
            validated_row_data["value"],
        ).validation(data_col)

        ## Check if any of input is -1
        if validated_row_data["value"] == -1 or validated_col_data["value"] == -1:
            post_message(gatewayapiClient, connection_id, validated_row_data["message"])
            pass

        # Data in process:
        # validated_row_data["value"]
        # validated_col_data["value"]

        # Check if loggable

        # Log to table

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
