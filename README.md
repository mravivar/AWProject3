# AWProject3

## Database
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
update the absolute path to your utf8 folder in load_csv_data_to_mongodb.py and run it  
$ chmod 777 load_csv_data_to_mongodb.py  
$ ./load_csv_data_to_mongodb.py  

Database:awproject3 and Collection:table1 are created in mongodb  

## Flask server:  
1. To install the needed python packages  
$ cd awproject3  
$ pip install -r requirements.txt  

2. To start flask server  
$ cd awproject3  
$ python server.app  

3. In browser, goto: http://localhost:5000/  
You will see some output.  
