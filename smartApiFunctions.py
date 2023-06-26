from smartapi import SmartConnect
from SmartWebSocketV2 import SmartWebSocketV2
import data_managment
import threading
import pyotp, time, os, datetime

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
username = os.getenv("USER_NAME")
pwd = os.getenv("PASSWORD")
token = os.getenv("TOKEN")


db = data_managment.data_managment("realtime_ticks_data")  # make the name dynamic


# 1. Implement stop connection function
#
class smartApiFunctions:
    def __init__(self, api_key, username, pwd, token) -> None:
        self.api_key = api_key
        self.username = username
        obj = SmartConnect(api_key=self.api_key)
        data = obj.generateSession(self.username, pwd, pyotp.TOTP(token).now())
        self.AUTH_TOKEN = data["data"]["jwtToken"]
        self.REFRESH_TOKEN = data["data"]["refreshToken"]
        self.FEED_TOKEN = obj.getfeedToken()
        res = obj.getProfile(self.REFRESH_TOKEN)
        print(res)

    # now this function is a bit hardcoded ...make it short and more dynamic
    def _socket_connect(
        self,
        stocks_symbol,
        exchange_type,
        correlation_id,
        action,
        mode,
    ) -> None:
        print("socket connect")
        tokenList = [
            {"exchangeType": exchange_type, "tokens": stocks_symbol},
            # {"exchangeType": 5, "tokens": ["257273"]},
        ]
        print(tokenList)
        sws = SmartWebSocketV2(
            self.AUTH_TOKEN, self.api_key, self.username, self.FEED_TOKEN
        )

        def on_data(wsapp, message):
            db.add_data(message)

            print("Ticks: {}".format(message))

        def on_open(wsapp):
            print("on open")
            sws.subscribe(correlation_id, mode, tokenList)

        def on_error(wsapp, error):
            print(error)

        def on_close(wsapp):
            print("Close")

        # Assign the callbacks.
        sws.on_open = on_open
        sws.on_data = on_data
        sws.on_error = on_error
        sws.on_close = on_close

        sws.connect()


if __name__ == "__main__":
    arr = ["250179", "257986", "254474", "256829"]
    sc = smartApiFunctions(api_key, username, pwd, token)
    sc._socket_connect(
        stocks_symbol=arr,
        exchange_type=5,
        correlation_id="dfttest_1",
        action=1,
        mode=2,
    )
