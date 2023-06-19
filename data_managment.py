import sqlite3
import traceback

# edge cases to handel
# 1- if table is not present
# 2- if table is present after deleting
# 3- if data is not present
# 4- if data is present(primary key errror)
# 5- if data is not in correct format


class data_managment:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        print("connection established")
        self.cursor = self.conn.cursor()
        # creating the table
        i_qur = """
            CREATE TABLE stocks
            (exchange_type INTEGER,
            token INTEGER,
            sequence_number INTEGER,
            exchange_timestamp INTEGER,
            last_traded_price INTEGER,
            last_traded_quantity INTEGER,
            average_traded_price INTEGER,
            volume_trade_for_the_day INTEGER,
            total_buy_quantity INTEGER,
            total_sell_quantity INTEGER,
            open_price_of_the_day INTEGER,
            high_price_of_the_day INTEGER,
            low_price_of_the_day INTEGER,
            closed_price INTEGER
            )
            """
        # self.cursor.execute(i_qur)
        try:
            self.cursor.execute(i_qur)
            print("new table created")
        except:
            print("table already present")

    def add_data(self, data):
        # print("adding data " + data["symbol"])
        # print(data["fycode"]) # the programe was not able to move beyond this because this was not even defined. Resercch abou it more and impreove this function in python
        data_parms = [
            data["exchange_type"],
            data["token"],
            data["sequence_number"],
            data["exchange_timestamp"],
            data["last_traded_price"],
            data["last_traded_quantity"],
            data["average_traded_price"],
            data["volume_trade_for_the_day"],
            data["total_buy_quantity"],
            data["total_sell_quantity"],
            data["open_price_of_the_day"],
            data["high_price_of_the_day"],
            data["low_price_of_the_day"],
            data["closed_price"],
        ]

        qur = """INSERT INTO stocks (
            exchange_type,
            token,
            sequence_number,
            exchange_timestamp,
            last_traded_price,
            last_traded_quantity,
            average_traded_price,
            volume_trade_for_the_day,
            total_buy_quantity,
            total_sell_quantity,
            open_price_of_the_day,
            high_price_of_the_day,
            low_price_of_the_day,
            closed_price)
            VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        # write a querry to insert data
        # print(qur)
        try:
            self.cursor.execute(qur, data_parms)
            self.conn.commit()
            print("data added")
        except sqlite3.IntegrityError:
            print("data already present")
            print(traceback.format_exc())
            # print(traceback.print_exc())
        except:
            print("data not in correct format")
            print(traceback.format_exc())
            print(traceback.print_exc())
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
    data["exchange_timestamp"] = 1
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

    db = data_managment("test.db")
    db.add_data(data)
    db.get_data()
    db.close_connection()
