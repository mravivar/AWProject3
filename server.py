from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
from pymongo import MongoClient # Database connector
from flask_cors import CORS

client = MongoClient('localhost', 27017)    #Configure the connection to the database
db = client.awproject3    #Select the database
table = db.table1 #Select the collection
table2 = db.table2

app = Flask(__name__,
            static_folder = "frontend/dist",
            template_folder = "frontend")
CORS(app)

# config
app.secret_key = 'aw project'

# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

# use decorators to link the function to a url
@app.route('/')
@login_required
def home():
    return render_template('index.html')  # render a template
    # return "Hello, World!"  # return a string

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
    	tuple = table2.find_one({"user_id": request.form['username']})
    	#print("#################################################")
    	#print(request.form['username'])
    	#print(request.form['password'])
    	#print(tuple)
    	#print(tuple['user_id'])
    	#print(tuple['password'])
    	#print("#################################################")
        #if request.form['password'] != tuple['password']:
        user_id = tuple['user_id']
        if request.form['username'] != tuple['user_id']: #or request.form['password'] != tuple['password']:
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            session['user_id'] = user_id
            flash('You were logged in.')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
	#print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
	#print(session['user_id'])
	session.pop('logged_in', None)
	flash('You were logged out.')
	return redirect(url_for('login'))

@app.route('/api/questions')
def list():
	tuple = table.find_one()
	noOfDocuments = table.count()
	data=tuple['type']+ " " +tuple['title']+ " "+tuple['content']+ " "+tuple['text']+ " "+tuple['code']+ " "+tuple['user_id']+ " "+tuple['time']+ " "+tuple['vote']+ " "+tuple['reputation']+ " "+tuple['accept_rate']+ " "+tuple['tag']
	return data

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
# Careful with the debug mode..
