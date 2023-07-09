import smartApiFunctions
import os, time
import stocks_symbol
from dotenv import load_dotenv
import threading
from algorithms.price_actions import indicators
from algorithms.price_actions import signals

# import centralState
import data_test

load_dotenv()

api_key = os.getenv("API_KEY")
username = os.getenv("USER_NAME")
pwd = os.getenv("PASSWORD")
token = os.getenv("TOKEN")

arr = stocks_symbol.stock_symbol()[:10]

db_name = "realtime_ticks_data"
ticks_table = "stocks_realtime"
# algo_table = ''
oldest_time = ""
newest_time = ""


def getTime():
    # Get the current timestamp
    current_timestamp = time.time()
    current_struct_time = time.localtime(current_timestamp)
    # formatted_datetime = time.strftime("%Y-%m-%d %H:%M:%S", current_struct_time)
    formatted_datetime = time.strftime("%H%M", current_struct_time)
    return int(formatted_datetime)


# cs = centralState.CentralState(1985)
# cs.addValue("o_time", 0)
# cs.addValue("l_time", 0)

socket_obj = smartApiFunctions.smartApiFunctions(api_key, username, pwd, token)


# thread 1
def start_socket():
    socket_obj._socket_connect(
        stocks_symbol=arr, exchange_type=1, correlation_id="dfttest_1", action=1, mode=2
    )


t1 = threading.Thread(target=start_socket)

t1_1 = threading.Thread(target=data_test.test_data)

# t1.start()
t1_1.start()

# start_socket()


# thread 2
# update the algo values in the database
def start_algo():
    indi = indicators.Indicators("test")
    timestamp = 0005
    period = 14
    for i in range(1000):
        timestamp = indi.rsi(timestamp, period)


t2 = threading.Thread(target=start_algo)
start_algo()

# t2.start()


# thread 3
# get signals using trading bot
def signal_algo():
    signal = signals.signals("realtime_ticks_data", 0, "stocks")
    signal.test_signal()


# signal_algo()
