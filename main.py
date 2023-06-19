import smartApiFunctions
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
username = os.getenv("USER_NAME")
pwd = os.getenv("PASSWORD")
token = os.getenv("TOKEN")
# arr = [
#     "24948",
#     "5258",
#     "9819",
#     "1660",
#     "772",
#     "14592",
#     "15355",
#     "312",
#     "14299",
#     "17094",
#     "685",
#     "11723",
#     "11184",
#     "881",
#     "18652",
#     "11262",
#     "8479",
#     "23650",
#     "17903",
#     "1922",
#     "11915",
#     "8075",
#     "2303",
#     "19913",
#     "10099",
#     "3426",
#     "16675",
#     "13538",
#     "1330",
#     "3103",
#     "10440",
#     "3456",
#     "3499",
#     "13404",
#     "4503",
#     "3506",
#     "17875",
#     "4684",
#     "6656",
#     "3150",
#     "4963",
#     "11536",
#     "19943",
#     "18011",
#     "910",
#     "7929",
#     "21238",
#     "335",
#     "11703",
# ]

arr = ["250179", "257986", "254474", "256829"]

socket_obj = smartApiFunctions.smartApiFunctions(api_key, username, pwd, token)
socket_obj._socket_connect(stocks_symbol=arr, exchange_type=5)
