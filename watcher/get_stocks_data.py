import os
from fyers_api.Websocket import ws
import data_managment
import datetime
from time import sleep

curr_wd = os.getcwd()

# fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,log_path="/home/Desktop/apiV2") ----this part will be provided


# data managment codes
db_name = "nifty200_" + datetime.datetime.now().strftime("%x") + ".db"
db = data_managment.data_managment("test.db")


# def get_hist_data(fyers, year, stock_ticker_symbol):
#   # year = "2021"
#   time_range = [["01-01", "03-31"], ["04-01","06-30"], ["07-01","09-30"], ["10-01","12-31"]]
#   # stock_ticker_symbol = "NSE:SBIN-EQ"

#   i = 0
#   for x in time_range:
#     date_from = year +"-"+x[0]
#     date_to = year +"-" + x[1]
#     ticker = {"symbol":stock_ticker_symbol,"resolution":"1","date_format":"1","range_from":date_from,"range_to":date_to,"cont_flag":"1"}
#     print(ticker)
#     data = fyers.history(ticker)
#     if(data['s'] == "no_data"):
#       no_data.append(stock_ticker_symbol+ date_from + date_to)
#       continue
#     output = pd.DataFrame(data['candles'])
#     output.columns = ['epoch_time', 'open_value', 'highest_value', 'lowest_value', 'close_value', 'volume_traded']
#     dir = "data" + "/" +stock_ticker_symbol + "/" + year
#     output_location =dir + "/" + date_from + "to" + date_to + ".csv"
#     if(i == 0):
#       os.makedirs(dir)
#     output.to_csv(output_location)
#     i = i+1


def custom_message(msg):
    print("..................................")
    # change msg in perfect format
    db.add_data(msg[0])
    print(msg[0]["symbol"])
    # print("Custome Message " + str(msg))


def get_live_data(client_id, access_token, symbol, data_type="symbolData"):
    # ws.websocket_data = custom_message
    fyersSocket = ws.FyersSocket(
        access_token=client_id + ":" + access_token,
        run_background=False,
        log_path=curr_wd  + "/socket_logs/",
    )

    fyersSocket.websocket_data = custom_message
    # fyersSocket = ws.FyersSocket(access_token="KPQVRS7JKZ-100",run_background=True,log_path=curr_wd)
    fyersSocket.subscribe(symbol=symbol, data_type=data_type)
    fyersSocket.keep_running()
