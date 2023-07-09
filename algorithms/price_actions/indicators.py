import data_managment_olhcv as dm
import pandas as pd
from datetime import datetime

# dont use class here


class Indicators:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db = dm.data_managment_olhcv(db_name)
        self.conn = self.db.conn

    def ma(self, period):
        ts_h = period["hr"]
        ts_m = period["min"]
        arr_1 = self.db.get_unprocessed(ts_h, ts_m)
        df_1 = pd.DataFrame(arr_1)
        # use roleback here
        for index, row in df_1.iterrows():
            # removed code from here
            self.db.update(index, row[0])
            # print(index)
            ts_h = df_1.loc[df_1[0] == row[0], 12]
            ts_m = df_1.loc[df_1[0] == row[0], 13]

        # updating the db

        return ts_h, ts_m

    def rsi(self, ts_h_m, period):
        # use of rolling function
        df = pd.DataFrame(self.db.get_unprocessed(ts_h_m))
        if len(df) == 0:
            print("Waiting for recent data")
            return ts_h_m
        col_name = [
            "p_key",
            "exchange_type",
            "token",
            "open",
            "low",
            "high",
            "close",
            "volume",
            "total_buy_quantity",
            "total_sell_quantity",
            "date_time",
            "date",
            "hour",
            "minute",
        ]
        col_name_dict = {}
        for i, n in enumerate(col_name):
            col_name_dict[i] = n
        df = df.rename(columns=col_name_dict)
        df = df.sort_values(by=["hour_min"])
        df["change"] = (df["close"] - df["open"]) / df["open"]
        # df["change"] = (
        #     df.groupby("token")["close"] - df.groupby("token")["open"]
        # ) / df.groupby("token")["open"]

        create_table = """
        create table rsi 
        (p_key STRING,
        change INTEGER
        
        )
        """
        try:
            self.db.querry(create_table)
        except:
            print("table already present")

        df_e = df.loc[:, ["p_key", "change"]]
        ts_h_m = df["hour_min"].iloc[-1]
        print(df["hour"].iloc[-1])

        df_e.to_sql("rsi", self.conn, if_exists="append", index=False)

        return ts_h_m
        # print(df_e)


# print("row", row)
# x = df_3.loc[df_3[0] == row[0], 14]
# if x.empty:
#     x = 0
# ma = (
#     x * period["min"]
#     - df_2.loc[df_2[0] == row[0], 6]
#     + df_1.loc[df_1[0] == row[0], 6]
# ) / period["min"]
# print(x)
# print(df_2.loc[df_2[0] == row[0], 6])
# print(df_1.loc[df_1[0] == row[0], 6])

# print("moving average", ma)
# df_1.loc[df_1[0] == row[0], 14] = index
# print("row", row[0])
# key = string(row[0])
# qur = f"""update stocks set ma = {index} where p_key = {str(row[0])}"""
# self.db.querry(qur)


if __name__ == "__main__":
    ind = Indicators("test")
    timestamp = {"hr": 0, "min": 5}
    period = 14
    ind.rsi(timestamp, period)
