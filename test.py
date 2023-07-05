from smartapi import SmartConnect
from SmartWebSocketV2 import SmartWebSocketV2
import threading
import pyotp, time, os

from dotenv import load_dotenv

load_dotenv()

apiKey = os.getenv("API_KEY")
username = os.getenv("USER_NAME")
pwd = os.getenv("PASSWORD")
token = os.getenv("TOKEN")

obj = SmartConnect(api_key=apiKey)
data = obj.generateSession(username, pwd, pyotp.TOTP(token).now())

AUTH_TOKEN = data["data"]["jwtToken"]
refreshToken = data["data"]["refreshToken"]
FEED_TOKEN = obj.getfeedToken()
res = obj.getProfile(refreshToken)
print(res)


# -----web-socket connection
correlation_id = "dfttest_1"
action = 1
mode = 2

arr = [
    "24948",
    "5258",
    "9819",
    "1660",
    "772",
    "14592",
    "15355",
    "312",
    "14299",
    "17094",
    "685",
    "11723",
    "11184",
    "881",
    "18652",
    "11262",
    "8479",
    "23650",
    "17903",
    "1922",
    "11915",
    "8075",
    "2303",
    "19913",
    "10099",
    "3426",
    "16675",
    "13538",
    "1330",
    "3103",
    "10440",
    "3456",
    "3499",
    "13404",
    "4503",
    "3506",
    "17875",
    "4684",
    "6656",
    "3150",
    "4963",
    "11536",
    "19943",
    "18011",
    "910",
    "7929",
    "21238",
    "335",
    "11703",
]

tokenList = [
    {"exchangeType": 1, "tokens": arr},
    # {"exchangeType": 5, "tokens": ["250179", "257986", "254474", "256829"]},
]
# token = "mcx_fo|257273"
# task = 'mw'
sws = SmartWebSocketV2(AUTH_TOKEN, apiKey, username, FEED_TOKEN)


def on_data(wsapp, message):
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
