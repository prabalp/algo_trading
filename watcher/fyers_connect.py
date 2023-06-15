from fyers_api import fyersModel
import os, threading, time
import get_stocks_data, nifty200, gsheet_connect, profile_info

client_id = "KPQVRS7JKZ-100"

# getting this token from the google sheets
acss_tok_sheet = gsheet_connect.gsheet_connect(
    "creds.json", "1rZUkl8o04L-Qst2X-HMh1SoSpJ1xWnZclg2ZybKnH1I"
)
g_access_token = acss_tok_sheet.read("Important_data!B1")["values"][0][0]

access_token = g_access_token


def generate_auth_code():
    # access_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2NzY0NDI1ODksImV4cCI6MTY3NjUwNzQ0OSwibmJmIjoxNjc2NDQyNTg5LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCajdIdmQ3M1RqYWNOR3BVTVJpczJZUWhleDBvZ0wydWNRMktYNVBxMTFsYlpjS2JlMVp5dUFySVZ4TGwwNmtJbXE0WUFzRjZOdlZKUzJwaTVjLUlvdjh0dHVBUWRSMU5zck1nWHQ4RlhsMklOTjdPcz0iLCJkaXNwbGF5X25hbWUiOiJQUkFCQUwgUEFOREEiLCJvbXMiOm51bGwsImZ5X2lkIjoiWFAyNjExNCIsImFwcFR5cGUiOjEwMCwicG9hX2ZsYWciOiJOIn0.VVtIfq2pnVh1SZZCd8Mzdfr9JDiKMHCxilu5DW7zz4M"
    print(access_token + " used")
    fyers = fyersModel.FyersModel(
        client_id=client_id, token=access_token, log_path=os.getcwd()
    )
    return fyers


if __name__ == "__main__":
    print(profile_info.get_profile_info(generate_auth_code()))
    tickers = nifty200.get_nifty200()
    # print(tickers[:50])
    t1 = threading.Thread(
        target=get_stocks_data.get_live_data,
        args=(client_id, access_token, tickers[:50], "symbolData"),
    )
    t2 = threading.Thread(
        target=get_stocks_data.get_live_data,
        args=(client_id, access_token, tickers[:50], "symbolData"),
    )

    # juggle between the threads
    # while True:
    #     t1.start()
    #     time.sleep(10)
    #     t2.start()

    # t1.start()
    # time.sleep(10)
    # t2.start()

    get_stocks_data.get_live_data(
        client_id,
        access_token,
        [
            "MCX:GOLD23AUGFUT",
            "MCX:GOLD23OCTFUT",
            "MCX:GOLD23DECFUT",
            "MCX:GOLD24FEBFUT",
            "MCX:GOLD24APRFUT",
        ],
        "symbolData",
    )
    # get_stocks_data.get_live_data(client_id, access_token, tickers[:50], "symbolData")
    # get_stocks_data.get_live_data(client_id, access_token, tickers[50:100], "symbolData")
    # get_stocks_data.get_live_data(client_id, access_token, tickers[100:150], "symbolData")
    # get_stocks_data.get_live_data(client_id, access_token, tickers[150:201], "symbolData")


# 'MCX:GOLD23AUGFUT',
# 'MCX:GOLD23OCTFUT',
# 'MCX:GOLD23DECFUT',
# 'MCX:GOLD24FEBFUT',
# 'MCX:GOLD24APRFUT',
#
