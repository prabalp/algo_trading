import data_managment_olhcv as dm
import pandas as pd


class signals:
    def __init__(self, db_name, timestamp, table_name):
        db = dm.data_managment_olhcv(db_name)
        self.db = db
        self.t = timestamp
        self.table_name = table_name

    def _ma_signal(self):
        qur = f"""select * from {self.table_name} where ma is not null and exchange_timestamp>{self.t}"""
        res = self.db.querry(qur)
        df = pd.DataFrame(res)
        for index, row in df.iterrows():
            if row["ma"] > row["close"]:
                # register these signals in a separate db names signals
                # and send a notification through telegram
                # timestamp , token, indecator, signal,
                print("sell")
            elif row["ma"] < row["close"]:
                print("buy")
