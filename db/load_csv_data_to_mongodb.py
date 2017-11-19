import os
import json
import csv
from pymongo import MongoClient

client = MongoClient()
db = client.awproject3
db.table1.delete_many({})

# update your path to utf8 folder
path_to_csv_files = './utf8/'

files = os.listdir(path_to_csv_files)
for file in files:
    file1 = path_to_csv_files + file
    print(file1)
    f = open(file1, "r")
    csv_reader = csv.reader(f)

    for line in csv_reader:
        # print(len(arr))
        dict1 = {
            "type": line[0],
            "title": line[1],
            "content": line[2],
            "text": line[3],
            "code": line[4],
            "user_id": line[5],
            "time": line[6],
            "vote": line[7],
            "reputation": line[8],
            "accept_rate": line[9],
            "tag": line[10].split()
        }

        res = db.table1.insert_one(dict1)

    f.close()

# to delete rows that contains the headers itself
res = db.table1.remove({"accept_rate": "accept_rate"})
