from slack import WebClient
from slack.errors import SlackApiError
from argparse import ArgumentParser
import csv
import os
import sys
import time

WAIT_TIME_SECONDS = 2


def get_user_id_from_email(client: WebClient, email: str) -> str:
    """
    Return a Slack user ID From a user's email.
    Print an error in case of failure.
    """
    try:
        response = client.users_lookupByEmail(email=email)
        return response.data["user"]["id"]
    except SlackApiError as e:
        print(f"Could not fetch ID for {email}: {e.response['error']}")


def message_user(client: WebClient, id: str, text: str):
    """
    Send a private message to the user defined by id.
    Print an error in case of failure.
    """
    try:
        client.chat_postMessage(channel=id, text=text)
        print(f"Message ok: {id}")
    except SlackApiError as e:
        print(f"Message fail: {e.response['error']} {id}")


def bulk_message(client: WebClient, users: list, message: str):
    for email in users:
        id = get_user_id_from_email(client=client, email=email)
        if id is not None:
            message_user(client=client, id=id, text=message)
        time.sleep(WAIT_TIME_SECONDS)


def parse_user_list(users_csv: str) -> list:
    """
    Parse the csv file and return a list with the emails
    """
    result = []
    with open(users_csv, newline="\n") as f:
        for row in csv.reader(f):
            result.append(row[0])
    return result


def parse_message(text_file: str) -> str:
    """
    Parse the message in the text file and return a string with it.
    """
    f = open(text_file, "r")
    return "".join(f.readlines())


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("csv", help="A csv file containing a list of user emails.")
    parser.add_argument(
        "message", help="A text file containing the message we want to send via slack."
    )
    parser.add_argument(
        "--token",
        help="The slack api token the script will use to connect to Slack. Can also set it as an environment variable SLACK_API_TOKEN.",
    )
    args = parser.parse_args()

    token = args.token or os.getenv("SLACK_API_TOKEN")
    if not token:
        sys.exit("No token provided")

    users = parse_user_list(args.csv)
    message = parse_message(args.message)

    client = WebClient(token=token)
    bulk_message(
        client=client,
        users=users,
        message=message,
    )
