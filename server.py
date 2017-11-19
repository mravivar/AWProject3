from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
from pymongo import MongoClient # Database connector
from flask_cors import CORS
import json
from bson.json_util import dumps

client = MongoClient('localhost', 27017)    #Configure the connection to the database
db = client.awproject3    #Select the database
table = db.table1 #Select the collection
user_table = db.table2
PER_PAGE_DEFAULT = 20


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
    	tuple = user_table.find_one({"user_id": request.form['username']})
        if request.form['username'] != tuple['user_id'] or request.form['password'].encode('utf8') != str(tuple['password']):
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            session['user_id'] = tuple['user_id']
            flash('You were logged in.')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('You were logged out.')
	return redirect(url_for('login'))

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
@login_required
def catch_all(path):
    return render_template("index.html")


@app.route('/api/questions', methods=['GET'])
def getQuestions():
	page_number = int(request.args['page'])
	if 'per_page' in request.args:
		per_page = int(request.args['per_page'])
	else:
		per_page = PER_PAGE_DEFAULT
	
	if not session['logged_in']:
		res = {'code': 401, 'message':'User not logged in'}
		return json.dumps(res)

	user_id = session['user_id']
	
	user_tuple = user_table.find_one({'user_id': user_id})
	user_tags = user_tuple['tag'].split()

	query_results = table.find({'type': 'question', 'tag': {'$in': user_tags}}).skip((page_number-1)*per_page).limit(per_page)
	total_results_count = table.count({'type': 'question', 'tag': {'$in': user_tags}})

	return_result = {'code': 200, 'message': 'success'}
	page_context = {'page': page_number, 'per_page': per_page,'total_pages': total_results_count/per_page}

	questions = []
	for result in query_results:
		per_question = {'id': str(result['_id']), 'description': result['title'].replace("&quot;", "'"), 'tags': result['tag']}
		question_user_tuple = user_table.find_one({'user_id': result['user_id']})
		user_details = {'id': result['user_id'], 'name': question_user_tuple['user_name'], 'ratings': question_user_tuple['reputation']}
		per_question['user'] = user_details
		answer_count = table.count({'title': result['title'], 'type': {'$in': ['answer', 'accepted-answer']}})
		per_question['stats'] = {'votes': result['vote'], 'answer_count': answer_count}
		questions.append(per_question)

	return_result['page_context'] = page_context
	return_result['questions'] = questions
	return json.dumps(return_result)


if __name__ == "__main__":
    app.run(debug=True)
# Careful with the debug mode..
