from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja')
def ninja():
	return render_template('ninja.html')

@app.route('/ninja/<username>')
def show_user_profile(username):
    print(username)
    if(username=='blue'):
        return render_template("blue.html")
    elif(username=='red'):
        return render_template("red.html")
    elif(username=='orange'):
        return render_template("orange.html")
    elif(username=='purple'):
        return render_template("purple.html")
    else:
        return render_template("april.html")

app.run(debug=True)