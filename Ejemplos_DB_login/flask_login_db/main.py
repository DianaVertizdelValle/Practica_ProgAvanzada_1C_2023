from flask import render_template, redirect, url_for, flash, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, current_user, logout_user

from functools import wraps
from modules.forms import LoginForm, RegisterForm
from modules.config import app, db, login_manager
from modules.databases import User


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods= ["GET", "POST"])
def login():      
    return render_template('login.html')


@app.route("/register", methods= ["GET", "POST"])
def register():
    return render_template('register.html')


@app.route("/welcome")
def welcome():           
    return render_template('welcome.html')


if __name__ == '__main__':
    app.run(debug=True)