import data_managment_olhcv
import datetime

db = data_managment_olhcv.data_managment_olhcv("test")  # make the name dynamic
db.create_table()


data = {}
while True:
    db.add_data(data)
