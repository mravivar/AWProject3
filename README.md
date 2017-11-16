# AWProject3

## Database
Python version: 3.5.1 (3.x should work fine)

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

Database:awproject3 and Collection:table1 are created in mongodb  

## Flask server:  
1. To install the needed python packages  
$ cd awproject3  
$ pip install -r requirements.txt  

2. To start flask server  
$ cd awproject3  
$ python server.py  

3. In browser, goto: http://localhost:5000/  
You will see some output.  

## Frontend 
1. run `npm install` inside the `frontend` folder
2. run `npm run build` for production build or `npm run dev` for development server.

