from flask import Flask, render_template, request, redirect, session, flash
import re
emailRegEx = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    error = None
    session['firstName'] = request.form['firstName']
    session['lastName'] = request.form['lastName']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    session['confirmPassword'] = request.form['confirmPassword']

    if len(session['firstName']) < 1:
      flash("first name cannot be empty!", 'error')
      error = True
      return redirect('/')
    elif session['firstName'].isalpha() == False :
      flash("First name must contain only alphabetic characters!", 'error')
      error = True
    
    if len(session['lastName']) < 1:
      flash("Last name cannot be empty!", 'error')
      error = True
    elif session['lastName'].isalpha() == False :
      flash("Last name must contain only alphabetic characters!", 'error')
      error = True

    if len(session['email']) < 1:
      flash("email cannot be empty!", 'error')
      error = True
    elif not emailRegEx.match(request.form['email']):
      flash("Invalid Email Address!")
      error = True   

    if len(session['password']) < 1 :
      flash("Password cannot be empty!", 'error')
      error = True
    elif len(session['password']) < 8:
      flash("Password must be longer than 8 characters")
      error = True

    if len(session['confirmPassword']) < 1 :
      flash("Password confirmation cannot be empty!", 'error')
      error = True
    elif session['password'] != session['confirmPassword'] :
      flash("Password confirmation and password entries must match!", 'error')
      error = True

    if error == True :
      return redirect('/')

    return render_template('result.html')
app.run(debug=True) # run our server
