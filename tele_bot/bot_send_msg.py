import requests, os, time
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def sendMessage(message):
    URL = f"""https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"""
    PARAMS = {"chat_id": CHAT_ID, "text": message, "parse_mode": "MarkdownV2"}

    return requests.get(url=URL, params=PARAMS).json()


if __name__ == "__main__":
    while True:
        print(sendMessage("Hello Jii"))
        time.sleep(2)
