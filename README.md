# Recommendation System
Since discussion forums have been increasingly used over the recent years, the data in the forum keeps booming which leads to information deluge. Users have to go through lots of content before finding the required information. This is unnecessary and time consuming. The solution to this problem and objective of this poject is to develop a system that provides adaptive navigation support, using a content-based recommendation engine, for discussion forum posts.

## Database
Python version: 3.5.2 (3.x should work fine)

1. To install mongodb (v3.4)  
$ brew install mongodb

2. To install brew services   
$ brew tap homebrew/services

3. Start mongodb service  
$ brew services start mongodb

4. Verify the version  
$ mongo --version  
MongoDB shell version v3.4.7 (3.4.x should work fine)  

5. Load all csv data to mongodb  
$ cd awproject3/db  
$ python load_csv_data_to_mongodb.py  

6. Load user collection data
db.createCollection("table2")

db.table1.find({},{tag:1,reputation:1,user_id:1,_id:0}).forEach(function(doc){ db.table2.insert(doc); });

db.table2.updateMany({},{$set:{"password":NumberInt(123)}},false,false)

Database:awproject3 and Collection:table1 are created in mongodb  

## Python Flask server:  
1. To install the needed python packages  
$ cd awproject3  
$ pip install -r requirements.txt  

2. To start flask server  
$ cd awproject3  
$ python server.py  

3. In browser, goto: http://localhost:5000/  
You will see the output.  

## Frontend 
1. run `npm install` inside the `frontend` folder
2. run `npm run build` for production build or `npm run dev` for development server.

