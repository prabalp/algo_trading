import sqlite3
import traceback
from datetime import datetime, timedelta, date

# edge cases to handel
# 1- if table is not present
# 2- if table is present after deleting
# 3- if data is not present
# 4- if data is present(primary key errror)
# 5- if data is not in correct format

# find out how much dely does the pushing causes


class data_managment_olhcv:
    def __init__(self, db_name):
        self.m_db_name = db_name + "_" + "olhcv" + "_" + str(date.today()) + ".db"
        self.conn = sqlite3.connect(self.m_db_name, check_same_thread=False)
        print("connection established")
        self.cursor = self.conn.cursor()
        # creating the table
        i_qur = """
            CREATE TABLE stocks
            (p_key STRING PRIMARY KEY,
            exchange_type INTEGER,
            token INTEGER,
            open INTEGER,
            low INTEGER,
            high INTEGER,
            close INTEGER,
            volume INTEGER,
            total_buy_quantity INTEGER,
            total_sell_quantity INTEGER,
            date_time STRING,
            date STRING,
            hour STRING,
            minute STRING
            )
            """
        # self.cursor.execute(i_qur)
        try:
            self.cursor.execute(i_qur)
            print("new table created")
        except:
            print("table already present")

    def add_data(self, data):
        # the programe was not able to move beyond this because this was not even defined. Resercch abou it more and impreove this function in python
        dt = datetime.fromtimestamp(data["exchange_timestamp"] / 1000)
        date_time = dt.strftime("%Y-%m-%d %H:%M:%S")
        date = dt.strftime("%Y-%m-%d")
        hour = dt.strftime("%H")
        minute = dt.strftime("%M")
        p_key = date + "_" + hour + "/" + minute + "_" + str(data["token"])
        open = data["last_traded_price"]
        low = data["last_traded_price"]
        high = data["last_traded_price"]
        close = data["last_traded_price"]
        volume = data["last_traded_quantity"]

        rec = self.querry('select * from stocks where p_key = "' + p_key + '"')
        # rec = self.querry("select * from stocks")
        print(rec)
        if rec != []:
            print("changing parameters")
            low = min(rec[0][4], low)
            high = max(rec[0][5], high)
            volume += rec[0][7]

        data_parms = [
            p_key,
            data["exchange_type"],
            data["token"],
            open,
            low,
            high,
            close,
            volume,
            data["total_buy_quantity"],
            data["total_sell_quantity"],
            date_time,
            date,
            hour,
            minute,
        ]

        qur = """INSERT INTO stocks (
            p_key,
            exchange_type,
            token,
            open,
            low,
            high,
            close,
            volume,
            total_buy_quantity,
            total_sell_quantity,
            date_time,
            date,
            hour,
            minute)
            VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        # write a querry to insert data
        # print(qur)
        try:
            self.cursor.execute(qur, data_parms)
            self.conn.commit()
            print("data added")

        except sqlite3.IntegrityError:
            print("data already present")
            print("data updating")
            qur = """UPDATE stocks SET
            low= ?,
            high= ?,
            close= ?,
            volume= ?
            WHERE p_key = ?"""
            data_parms = [low, high, close, volume, p_key]
            try:
                self.cursor.execute(qur, data_parms)
                self.conn.commit()
                print("data updated")
            except:
                print("data not updated")

            # print(traceback.format_exc())
            # print(traceback.print_exc())
        except:
            print("data not in correct format")
            # print(traceback.format_exc())
            # print(traceback.print_exc())
        return 0

    def get_data(self):
        qur = """ SELECT * FROM stocks"""
        self.cursor.execute(qur)
        self.conn.commit()
        res = self.cursor.fetchall()
        # self.conn.commit()
        print(res)

    def close_connection(self):
        self.conn.close()
        print("connection closed-1")

    def querry(self, qur):
        self.cursor.execute(qur)
        self.conn.commit()
        res = self.cursor.fetchall()
        return res

    def get_unprocessed(self, timestamp):
        q = f""" SELECT * FROM stocks WHERE exchange_timestamp > {timestamp} """
        self.cursor.execute(q)
        self.conn.commit()
        res = self.cursor.fetchall()
        return res


# join two list in python
# a = [1,2,3]
# b = [4,5,6]
# c = a + b
# print(c)

if __name__ == "__main__":
    data = {}
    data["exchange_type"] = 1
    data["token"] = "1232"
    data["sequence_number"] = 1
    data["exchange_timestamp"] = 1641181510
    data["last_traded_price"] = 1
    data["last_traded_quantity"] = 1
    data["average_traded_price"] = 1
    data["volume_trade_for_the_day"] = 1
    data["total_buy_quantity"] = 1
    data["total_sell_quantity"] = 1
    data["open_price_of_the_day"] = 1
    data["high_price_of_the_day"] = 1
    data["low_price_of_the_day"] = 1
    data["closed_price"] = 1
    # print(data)

    {
        "subscription_mode": 2,
        "exchange_type": 5,
        "token": "256829",
        "sequence_number": 654293,
        "exchange_timestamp": 1687759144000,
        "last_traded_price": 0,
        "subscription_mode_val": "QUOTE",
        "last_traded_quantity": 0,
        "average_traded_price": 0,
        "volume_trade_for_the_day": 0,
        "total_buy_quantity": 0.0,
        "total_sell_quantity": 1.0,
        "open_price_of_the_day": 0,
        "high_price_of_the_day": 0,
        "low_price_of_the_day": 0,
        "closed_price": 159400,
    }

    db = data_managment_olhcv("test")
    db.add_data(data)
    db.get_data()
    # r = db.get_unprocessed(1641181505)
    # print(len(r))
    db.close_connection()
    # print(str(date.today()))


# def mod_data(self, data):
#         dt = datetime.fromtimestamp(data["exchange_timestamp"] / 1000)
#         date_time = dt.strftime("%Y-%m-%d %H:%M")
#         date = dt.strftime("%Y-%m-%d")
#         hour = dt.strftime("%H")
#         minute = dt.strftime("%M")

#         if self.hr != 0 and self.min < minute:
#             data_mod = {
#                 "exchange_type": self.exchange_type,
#                 "token": self.token,
#                 "open": self.open,
#                 "low": self.low,
#                 "high": self.high,
#                 "close": self.close,
#                 "volume": self.volume,
#                 "date_time": date_time,
#                 "date": date,
#                 "hour": self.hr,
#                 "minute": self.min,
#             }
#             self.add_data(data_mod)
#             self.hr = hour
#             self.min = minute
#             self.st = 1

#         self.hr = hour
#         self.min = minute
#         if self.st == 1:
#             self.open = data["last_traded_price"]
#             self.st = 0
#         self.low = min(data["last_traded_price"], self.low)
#         self.high = max(data["last_traded_price"], self.high)
#         self.close = data["last_traded_price"]
#         self.volume += data["last_traded_quantity"]
#         self.exchange_type = data["exchange_type"]
#         self.token = data["token"]
