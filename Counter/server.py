from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

app.secret_key='thisissecret'


@app.route('/')
def index():
	count = session['count'] + 1
	session['count'] = count
	return render_template('index.html')

@app.route('/plustwo', methods=['POST'])
def plustwo():
	session['count'] += 1
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session['count'] = 0
	return redirect('/')



app.run(debug=True)