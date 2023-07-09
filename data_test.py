import data_managment_olhcv
import time, random

db = data_managment_olhcv.data_managment_olhcv("test")  # make the name dynamic
db.create_table()


data = {}


def test_data():
    while True:
        data["exchange_timestamp"] = int(time.time())
        data["last_traded_price"] = random.randint(10000, 99999)
        data["last_traded_price"] = random.randint(10000, 99999)
        data["last_traded_price"] = random.randint(10000, 99999)
        data["last_traded_price"] = random.randint(10000, 99999)
        data["last_traded_quantity"] = random.randint(10000, 99999)
        data["total_buy_quantity"] = random.randint(500, 10000)
        data["total_sell_quantity"] = random.randint(500, 10000)
        data["exchange_type"] = 1
        data["token"] = random.randint(9900, 9999)
        db.add_data(data)


if __name__ == "__main__":
    test_data()
