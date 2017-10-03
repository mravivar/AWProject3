from flask import Flask, render_template,request,redirect,url_for # For flask implementation
from pymongo import MongoClient # Database connector

client = MongoClient('localhost', 27017)    #Configure the connection to the database
db = client.awproject3    #Select the database
table = db.table1 #Select the collection

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	#Display the all Tasks
	tuple = table.find_one()
	#data = tuple['Name'] +" "+ tuple['Address'] +" "+ tuple['City'] +" "+ tuple['State'] +" "+ str(tuple['ZIP'])
	data=tuple['type']+ " " +tuple['title']+ " "+tuple['content']+ " "+tuple['text']+ " "+tuple['code']+ " "+tuple['user_id']+ " "+tuple['time']+ " "+tuple['vote']+ " "+tuple['reputation']+ " "+tuple['accept_rate']+ " "+tuple['tag']

	return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
# Careful with the debug mode..