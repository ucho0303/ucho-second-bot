from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os

YOUR_CHANNEL_ACCESS_TOKEN = os.environ['YOUR_CHANNEL_ACCESS_TOKEN']

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)


def main():
    user_id = os.environ['YOUR_USER_ID']

    messages = TextSendMessage(text="こんにちは")
    line_bot_api.push_message(user_id, messages=messages)


if __name__ == "__main__":
    main()
