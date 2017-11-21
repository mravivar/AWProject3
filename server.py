from flask import Flask, render_template, redirect, url_for, request, session, flash, send_from_directory
from functools import wraps
from pymongo import MongoClient # Database connector
from flask_cors import CORS
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import copy
import re
import nltk
from nltk.corpus import stopwords
import time
from rake_nltk import Rake

nltk.download('stopwords')

client = MongoClient('localhost', 27017)    #Configure the connection to the database
db = client.awproject3    #Select the database
questions_table = db.table1 #Select the collection
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

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        tuple=user_table.find_one({"user_id":request.form["username"]})
        if tuple is None:
            user_table.insert({"user_id":request.form["username"], "password":request.form["password"].encode('utf8'), "tag":request.form["interests"]})
            return redirect(url_for('login'))
        else:
            flash('The user already exists')
    return render_template('register.html', error=error)

#@login_required
@app.route('/api/questions/<question_id>', methods=['GET'])
def getQuestionDetails(question_id):

	# fill question details
	question_details = questions_table.find({'_id': ObjectId(question_id)})
	return_result = {}
	question = {}
	for ques in question_details:
		for key, value in ques.iteritems():
			if key != '_id':
				question[key] = value
			else:
				question[key] = str(value)

	return_result['question'] = question

	# fill answers
	answer_details = questions_table.find({'type': {'$in': ['answer', 'accepted-answer']}, 'title': question['title']})
	answers = []
	accepted_answer = {}
	for answer in answer_details:
		if answer['type'] == 'answer':
			answers.append(answer)
		else:
			accepted_answer = copy.deepcopy(answer)
	return_result['answers'] = answers
	return_result['accepted_answer'] = accepted_answer

	return dumps(return_result)

@login_required
@app.route('/api/search', methods=['GET'])
def searchText():
	if 'page' in request.args:
		page_number = int(request.args['page'])
	else:
		page_number = 1
	if 'per_page' in request.args:
		per_page = int(request.args['per_page'])
	else:
		per_page = PER_PAGE_DEFAULT
	query_string = request.args['query']
	s=set(stopwords.words('english'))
	word_array = filter(lambda w: not w in s,query_string.split())
	search_text = '|'.join(word_array)
	regex = re.compile('.*'+search_text+'.*', re.IGNORECASE)

	query_results = questions_table.find({'type': 'question', 'title': regex}).skip((page_number-1)*per_page).limit(per_page)
	total_results_count = questions_table.count({'type': 'question', 'title': regex})

	return_result = {'code': 200, 'message': 'success'}
	page_context = {'page': page_number, 'per_page': per_page,'total_pages': total_results_count/per_page}

	questions = []
	for result in query_results:
		per_question = {'id': str(result['_id']), 'description': result['title'].replace("&quot;", "'"), 'tags': result['tag']}
		question_user_tuple = user_table.find_one({'user_id': result['user_id']})
		user_details = {'id': result['user_id'], 'name': question_user_tuple['user_name'], 'ratings': question_user_tuple['reputation']}
		per_question['user'] = user_details
		answer_count = questions_table.count({'title': result['title'], 'type': {'$in': ['answer', 'accepted-answer']}})
		per_question['stats'] = {'votes': result['vote'], 'answer_count': answer_count}
		questions.append(per_question)

	return_result['page_context'] = page_context
	return_result['questions'] = questions
	return json.dumps(return_result)


def get_tags(content):
	r = Rake()
	r.extract_keywords_from_text(content)
	phrases = r.get_ranked_phrases()
	number_of_words = min(3, len(phrases))
	return phrases[0:number_of_words]
  
@login_required
@app.route('/api/questions', methods=['POST'])
def addQuestion():
	input_text = request.get_json()
	insert_record = {}
	user_id = session['user_id']
	user_tuple = user_table.find_one({'user_id': user_id})

	insert_record['code'] = input_text['code']
	insert_record['text'] = input_text['text']
	insert_record['vote'] = 0
	insert_record['user_id'] = user_id
	insert_record['title'] = input_text['title']
	insert_record['content'] = input_text['content']
	insert_record['reputation'] = user_tuple['reputation']
	insert_record['accept_rate'] = user_tuple['accept_rate']
	insert_record['type'] = 'question'
	insert_record['time'] = str(int(time.time()))

	insert_record['tag'] = get_tags(input_text['title']+' '+input_text['text'])
	questions_table.insert_one(insert_record)

	return dumps(insert_record)


@app.route('/api/questions', methods=['GET'])
def getQuestions():
	if 'page' in request.args:
		page_number = int(request.args['page'])
	else:
		page_number = 1
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

	query_results = questions_table.find({'type': 'question', 'tag': {'$in': user_tags}}).skip((page_number-1)*per_page).limit(per_page)
	total_results_count = questions_table.count({'type': 'question', 'tag': {'$in': user_tags}})

	return_result = {'code': 200, 'message': 'success'}
	page_context = {'page': page_number, 'per_page': per_page,'total_pages': total_results_count/per_page}

	questions = []
	for result in query_results:
		per_question = {'id': str(result['_id']), 'description': result['title'].replace("&quot;", "'"), 'tags': result['tag']}
		question_user_tuple = user_table.find_one({'user_id': result['user_id']})
		user_details = {'id': result['user_id'], 'name': question_user_tuple['user_name'], 'ratings': question_user_tuple['reputation']}
		per_question['user'] = user_details
		answer_count = questions_table.count({'title': result['title'], 'type': {'$in': ['answer', 'accepted-answer']}})
		per_question['stats'] = {'votes': result['vote'], 'answer_count': answer_count}
		questions.append(per_question)

	return_result['page_context'] = page_context
	return_result['questions'] = questions
	return json.dumps(return_result)

@app.route('/api/userprofile', methods=['GET'])
def userprofile():	
	if not session['logged_in']:
		res = {'code': 401, 'message':'User not logged in'}
		return json.dumps(res)

	user_id = session['user_id']
	query_results = table.find({'user_id': user_id})
	return_result = {'code': 200, 'message': 'success'}
	user_tuples = []

	# future enhancements: separate the results into questions and answers
	for result in query_results:
		per_tuple = {'id': str(result['_id']), 'type': result['type'], 'title': result['title'].replace("&quot;", "'"), 'content': result['content'], 'text': result['text'], 'code': result['code'], 'time': result['time'], 'vote': result['vote'], 'reputation': result['reputation'], 'accept_rate': result['accept_rate'], 'tags': result['tag']}
		user_tuples.append(per_tuple)
	
	return_result['user_tuples'] = user_tuples
	return json.dumps(return_result)


# to serve static css files  
@app.route('/public/<path:filename>')
def custom_static(filename):
    return send_from_directory("frontend/public/", filename)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
#@login_required
def catch_all(path):
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
# Careful with the debug mode..
