import logging
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
def send_notification(text, channel_id):

    if isinstance(text, str):

        client = WebClient(token=os.getenv('APITOKEN'))
        channel_id = channel_id
        try:
            result = client.chat_postMessage(
                channel=channel_id,
                text=text
            )

            print(result)

        except SlackApiError as e:
            print(f"Error: {e}")
    else:
        print("Element is not a string.")
