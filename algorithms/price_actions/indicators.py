import data_managment_olhcv as dm
import pandas as pd
from datetime import datetime


class Indicators:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db = dm.data_managment_olhcv(db_name)

    def ma(self, period):
        # get the whole column of closed price form database
        # ts_h = datetime.now().hour
        # ts_m = datetime.now().minute
        print(period)
        ts_h = 0
        ts_m = 0
        # ts should be in minutes
        arr_1 = self.db.get_unprocessed(ts_h, ts_m)
        ## handle the edge cases like is no record found
        # if arr_1['ma'] is not null then dont do the calculation
        arr_2 = self.db.get_unprocessed(ts_h - period["hr"], ts_m - period["min"])
        arr_3 = self.db.get_unprocessed(ts_h, ts_m - 1)
        df_1 = pd.DataFrame(arr_1)
        df_2 = pd.DataFrame(arr_2)
        df_3 = pd.DataFrame(arr_3)
        # set the p_key as index
        # df_1 = df_1.set_index(0)
        # df_2 = df_2.set_index(0)
        # df_3 = df_3.set_index(0)
        p_key = 0
        close = 6
        ma = 14
        print(df_1)
        # print(df_1, df_2, df_3)
        # use roleback here
        for index, row in df_1.iterrows():
            # removed code from here
            self.db.update(index, row[0])
            print(index)
            ts_h = df_1.loc[df_1[0] == row[0], 12]
            ts_m = df_1.loc[df_1[0] == row[0], 13]

        # updating the db

        return ts_h, ts_m


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
