import data_managment_olhcv as dm
import pandas as pd


class Indicators:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db = dm.data_managment_olhcv(db_name)

    def ma(self, period):
        # get the whole column of closed price form database
        ts = 0
        # ts should be in minutes
        arr_1 = self.db.get_unprocessed(ts)
        ## handle the edge cases like is no record found
        # if arr_1['ma'] is not null then dont do the calculation
        arr_2 = self.db.get_unprocessed(ts - period)
        arr_3 = self.db.get_unprocessed(ts - 1)
        df_1 = pd.DataFrame(arr_1)
        df_2 = pd.DataFrame(arr_2)
        df_3 = pd.DataFrame(arr_3)
        # set the p_key as index
        for index, row in df_1.iterrows():
            ma = (
                df_3[row["p_key"]]["ma"] * period
                - df_2[row["p_key"]]["close"]
                + df_1[row["p_key"]]["close"]
            ) / period
            df_1[row["p_key"]]["ma"] = ma
        return "done"
