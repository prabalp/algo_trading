import smartApiFunctions
import os
import stocks_symbol
from dotenv import load_dotenv
import threading

load_dotenv()

api_key = os.getenv("API_KEY")
username = os.getenv("USER_NAME")
pwd = os.getenv("PASSWORD")
token = os.getenv("TOKEN")

arr = stocks_symbol.stock_symbol()[:10]

socket_obj = smartApiFunctions.smartApiFunctions(api_key, username, pwd, token)

# thread 1
socket_obj._socket_connect(
    stocks_symbol=arr, exchange_type=1, correlation_id="dfttest_1", action=1, mode=2
)


# thread 2
# update the algo values in the database


# thread 3
# get signals using trading bot
