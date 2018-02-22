from flask import Flask, session, render_template, redirect, request

import random

app = Flask(__name__)

app.secret_key='thisissecret'

@app.route('/')
def index():
	session['result'] 
	
	return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
	x=random.randrange(0, 101)
	if int(request.form['guess']) > x:
		session['result'] ='Too High!'
	elif int(request.form['guess']) < x:
		session['result']='Too Low!'
	elif int(request.form['guess']) == x:
		session['result']='You got it!'
	return redirect('/')

app.run(debug=True)