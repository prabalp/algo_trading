import smartApiFunctions
import os
import stocks_symbol
from dotenv import load_dotenv
import threading
from algorithms.price_actions import indicators

load_dotenv()

api_key = os.getenv("API_KEY")
username = os.getenv("USER_NAME")
pwd = os.getenv("PASSWORD")
token = os.getenv("TOKEN")

arr = stocks_symbol.stock_symbol()[:10]

socket_obj = smartApiFunctions.smartApiFunctions(api_key, username, pwd, token)


# thread 1
def start_socket():
    socket_obj._socket_connect(
        stocks_symbol=arr, exchange_type=1, correlation_id="dfttest_1", action=1, mode=2
    )


# t1 = threading.Thread(target=start_socket)\

# start_socket()


# thread 2
# update the algo values in the database
def start_algo():
    indi = indicators.Indicators("realtime_ticks_data")
    period = {"hr": 0, "min": 5}
    indi.ma(period)


start_algo()


# thread 3
# get signals using trading bot
