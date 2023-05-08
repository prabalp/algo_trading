import sqlite3


class data_managment():
    def __init__(self, db_name):
        conn = sqlite3.connect(db_name)
        self.cursor = conn.cursor()
        # creating the table
        i_qur = '''
            CREATE TABLE stocks
            (timestamp INTEGER PRIMARY KEY,
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
            '''
        # self.cursor.execute(i_qur)    
        try:
            self.cursor.execute(i_qur)
            print('new table created')
        except:
            print('table already present')
        
    def add_data(self, data):
        # print('adding data '+data['symbol'])
        # qur = '''INSERT INTO stocks (
        #     timestamp,
        #     symbol, 
        #     fycode, 
        #     fyFlag, 
        #     pktLen, 
        #     ltp, 
        #     open_price, 
        #     high_price, 
        #     low_price, 
        #     close_price, 
        #     min_open_price, 
        #     min_high_price, 
        #     min_low_price, 
        #     min_close_price, 
        #     min_volume, 
        #     last_traded_qty, 
        #     last_traded_time, 
        #     avg_trade_price, 
        #     vol_traded_today, 
        #     tot_buy_qty, 
        #     tot_sell_qty)
        #     VALUES (
        #         {},
        #         {}, 
        #         {}, 
        #         {}, 
        #         {}, 
        #         {}, 
        #         {}, 
        #         {}, 
        #         {}, 
        #         {}, 
        #         {}, 
        #         {}, 
        #         {}, 
        #         {}, 
        #         {}, 
        #         {}, 
        #         {}, 
        #         {}, 
        #         {}, 
        #         {}, 
        #         {}
        #     )'''.format(data['timestamp'],
        #                 data['symbol'], 
        #                 data['fycode'], 
        #                 data['fyFlag'], 
        #                 data['pktLen'], 
        #                 data['ltp'], 
        #                 data['open_price'], 
        #                 data['high_price'], 
        #                 data['low_price'], 
        #                 data['close_price'], 
        #                 data['min_open_price'], 
        #                 data['min_high_price'], 
        #                 data['min_low_price'], 
        #                 data['min_close_price'], 
        #                 data['min_volume'], 
        #                 data['last_traded_qty'], 
        #                 data['last_traded_time'], 
        #                 data['avg_trade_price'], 
        #                 data['vol_traded_today'], 
        #                 data['tot_buy_qty'], 
        #                 data['tot_sell_qty']) # write a querry to insert data
        # print(qur)
        self.cursor.execute(qur)
        print('done')
        
    def view_data(self):
        # qur = """ SELECT * FROM stocks"""
        # self.cursor.execute(qur)
        res = self.cursor.fetchall()
        print(res)







