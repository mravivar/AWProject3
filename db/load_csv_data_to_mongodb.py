import os
import json
from pymongo import MongoClient

client = MongoClient()
db = client.awproject3

# update your path to utf8 folder
path_to_csv_files = '/Users/murali/Documents/github/AWProject3/db/utf8/'

files = os.listdir(path_to_csv_files)
for file in files:
    file1 = path_to_csv_files + file
    print(file1)
    f = open(file1, "r")
    lines = f.readlines()

    for line in lines:
        str = json.dumps(line)
        arr = str.split(',')
        # print(len(arr))
        dict1 = {
            "type": arr[0],
            "title": arr[1],
            "content": arr[2],
            "text": arr[3],
            "code": arr[4],
            "user_id": arr[5],
            "time": arr[6],
            "vote": arr[7],
            "reputation": arr[8],
            "accept_rate": arr[9],
            "tag": arr[10]
        }
        res = db.table1.insert_one(dict1)

    f.close()

# to delete rows that contains the headers itself
res = db.table1.remove({"accept_rate": "accept_rate"})