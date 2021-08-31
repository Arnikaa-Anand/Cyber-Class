from flask import Flask, render_template, session, redirect
from functools import wraps
import pymongo

app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

# Database
client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system

# Decorators
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')

  return wrap

# Routes
from user import routes

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/dashboard/')
@login_required
def dashboard():
  return render_template('dashboard.html')

@app.route('/dashboard/subjects/')
@login_required
def subjects():
  return render_template('subjects.html')

@app.route('/dashboard/assignments/')
@login_required
def assignments():
  return render_template('assignments.html')

@app.route('/dashboard/calendar/')
@login_required
def calendar():
  return render_template('calendar.html')

@app.route('/dashboard/account/')
@login_required
def account():
  return render_template('account.html')

@app.route('/dashboard/tests/')
@login_required
def tests():
  return render_template('tests.html')

@app.route('/dashboard/assignments/viewall/')
@login_required
def viewall():
  return render_template('assignments view all.html')

@app.route('/dashboard/assignments/submit/')
@login_required
def submit():
  return render_template('assignments submission.html')

@app.route('/dashboard/viewall')
@login_required
def dashboardviewall():
  return render_template('dashboard view all.html')

@app.route('/dashboard/joinclass')
@login_required
def join_class():
  return render_template('join class form.html')