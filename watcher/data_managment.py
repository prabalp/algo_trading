import sqlite3
import traceback

#edge cases to handel
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
            (timestamp INTEGER,
            symbol TEXT,
            fycode INTEGER,
            fyFlag INTEGER,
            pktLen INTEGER,
            ltp INTEGER,
            open_price INTEGER,
            high_price INTEGER,
            low_price INTEGER,
            close_price INTEGER,
            min_open_price INTEGER,
            min_high_price INTEGER,
            min_low_price INTEGER,
            min_close_price INTEGER,
            min_volume INTEGER,
            last_traded_qty INTEGER,
            last_traded_time INTEGER,
            avg_trade_price INTEGER,
            vol_traded_today INTEGER,
            tot_buy_qty INTEGER,
            tot_sell_qty INTEGER
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
        data_parms = [data["timestamp"],
                        data["symbol"],
                        data["fyCode"],
                        data["fyFlag"],
                        data["pktLen"],
                        data["ltp"],
                        data["open_price"],
                        data["high_price"],
                        data["low_price"],
                        data["close_price"],
                        data["min_open_price"],
                        data["min_high_price"],
                        data["min_low_price"],
                        data["min_close_price"],
                        data["min_volume"],
                        data["last_traded_qty"],
                        data["last_traded_time"],
                        data["avg_trade_price"],
                        data["vol_traded_today"],
                        data["tot_buy_qty"],
                        data["tot_sell_qty"]]
        
        qur = """INSERT INTO stocks (
            timestamp,
            symbol, 
            fyCode, 
            fyFlag, 
            pktLen, 
            ltp, 
            open_price, 
            high_price, 
            low_price, 
            close_price, 
            min_open_price, 
            min_high_price, 
            min_low_price, 
            min_close_price, 
            min_volume, 
            last_traded_qty, 
            last_traded_time, 
            avg_trade_price, 
            vol_traded_today, 
            tot_buy_qty, 
            tot_sell_qty)
            VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
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
    data["timestamp"] = 1
    data["symbol"] = "testy"
    data["fycode"] = 1
    data["fyFlag"] = 1
    data["pktLen"] = 1
    data["ltp"] = 1
    data["open_price"] = 1
    data["high_price"] = 1
    data["low_price"] = 1
    data["close_price"] = 1
    data["min_open_price"] = 1
    data["min_high_price"] = 1
    data["min_low_price"] = 1
    data["min_close_price"] = 1
    data["min_volume"] = 1
    data["last_traded_qty"] = 1
    data["last_traded_time"] = 1
    data["avg_trade_price"] = 1
    data["vol_traded_today"] = 1
    data["tot_buy_qty"] = 1
    data["tot_sell_qty"] = 1
    # print(data)
    
    db = data_managment("test.db")
    db.add_data(data)
    db.get_data()
    db.close_connection()



