from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from auth.forms import LoginForm
from flask_login import login_required
from flask_login import LoginManager


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html',form = form)

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/<name>')
def user(name):
	return render_template('user.html',name=name)