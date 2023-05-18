from flask import Flask
from flask_bootstrap import Bootstrap #1) https://pythonhosted.org/Flask-Bootstrap/basic-usage.html
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask("main")
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Bootstrap(app)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)