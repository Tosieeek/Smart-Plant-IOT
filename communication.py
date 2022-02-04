import logging
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
def send_notification(text, channel_id):

    if isinstance(text, str):

        client = WebClient(token="xoxp-3013417715795-2998770285223-3006782068934-2bd11ba36c634a9fa5ef4390a6d08ec7")
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
