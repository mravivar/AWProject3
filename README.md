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
MongoDB shell version v3.4.7  

5. Load data to mongodb  
$ cd awproject3/db  
$ mongoimport --db awproject3 --collection table1 --file 01_01_2014-12_31_2014[1].json --jsonArray  

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
