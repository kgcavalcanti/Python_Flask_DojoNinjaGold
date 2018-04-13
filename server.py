from flask import Flask, render_template, redirect, session, request
from datetime import datetime	
app = Flask(__name__)
app.secret_key = 'ieswaur85rr4390583irrfesfrpa'


@app.route('/')
def index():
	if "pocket" not in session:
		session['pocket'] = 0
	if "activities" not in session:
		session['activities'] = []

	return render_template ('index.html')

@app.route('/resetgame', methods=['POST'])
def reset():
	session['activities'] = []
	return redirect ('/')
	

@app.route('/process_money', methods=['POST'])
def findGold():
	import random
	if "activities" not in session:
		session['activities'] = []
	if request.form['building'] == 'farm':
		session['gold'] = random.randrange(10, 21)
		session['pocket'] = session['pocket'] + session['gold'] 
		session['now'] = datetime.now().strftime('%Y/%m/%d %I:%M %p')
		transactions = {
			'gold': session['gold'],
			'from': request.form['building'],
			'operation' : 'none',
			'operationTime': session['now']
		}

		session['activities'].append(transactions)

	elif request.form['building'] == 'cave':
		session['gold'] = random.randrange(5, 11)
		session['pocket'] = session['pocket'] + session['gold']
		session['now'] = datetime.now().strftime('%Y/%m/%d %I:%M %p') 
		transactions = {
			'gold': session['gold'],
			'from': request.form['building'],
			'operation' : 'none',
			'operationTime': session['now']
		}
		session['activities'].append(transactions)
	elif request.form['building'] == 'house':
		session['gold'] = random.randrange(2, 6)
		session['pocket'] = session['pocket'] + session['gold'] 
		session['now'] = datetime.now().strftime('%Y/%m/%d %I:%M %p') 
		transactions = {
			'gold': session['gold'],
			'from': request.form['building'],
			'operation' : 'none',
			'operationTime': session['now']			
		}
		session['activities'].append(transactions)
	elif request.form['building'] == 'casino':
		session['gold'] = random.randrange(0, 51)
		session['winOrLose'] = random.randint(0, 1)
		if session['winOrLose'] == 0:
			session['pocket'] = session['pocket'] - session['gold'] 
		elif session['winOrLose'] == 1:
			session['pocket'] = session['pocket'] + session['gold'] 
		session['now'] = datetime.now().strftime('%Y/%m/%d %I:%M %p')
		transactions = {
			'gold': session['gold'],
			'from': request.form['building'],
			'operation': session['winOrLose'],
			'operationTime': session['now']
		}
		session['activities'].append(transactions)
	print session['activities']
	print session['pocket'], type(session['pocket'])
	return redirect	 ('/')





app.run(debug=True)