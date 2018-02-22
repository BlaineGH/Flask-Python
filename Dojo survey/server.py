from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

app.secret_key = 'thisissecret'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods =['POST'])
def result():
	session['name']=request.form['name']
	session['location']=request.form['location']
	session['language']=request.form['language']
	session['comment']=request.form['comment']
	return redirect('/endresult')

@app.route('/endresult')
def endresult():
	return render_template('endresult.html')

app.run(debug=True)