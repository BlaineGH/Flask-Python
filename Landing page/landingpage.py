from flask import Flask, render_templete, 

app = flask(__name__)

@app.route('/')
def landing page():
	return render_templete('index.html')

@app.route('/ninjas')
def ninjas():
	return render_templete('ninjas.html')

@app.route('/dojo/news')
def dojos():
	return render_templete('dojos.html')

app.run(debug=True)


# @app.route('/')
# def index():
# 	return render_template('index.html')

# @app.route('/ninjas')
# def ninja():
# 	return render_template('ninja.html')

# @app.route('/dojo/new')
# def ninja():
# 	return render_template('new.html')