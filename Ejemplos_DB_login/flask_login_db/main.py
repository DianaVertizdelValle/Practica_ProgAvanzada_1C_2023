from flask import render_template, redirect, url_for, flash, abort
from werkzeug.security import generate_password_hash, check_password_hash #https://werkzeug.palletsprojects.com/en/2.3.x/utils/
from flask_login import login_user, login_required, current_user, logout_user #https://flask-login.readthedocs.io/en/latest/#configuring-your-application

from functools import wraps
from modules.forms import LoginForm, RegisterForm
from modules.config import app, db, login_manager
from modules.databases import User

admin_list = [1]

with app.app_context():
    db.create_all()

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


def is_admin():
    if current_user.is_authenticated and current_user.id in admin_list:
        return True
    else:
        return False

#https://flask.palletsprojects.com/en/2.3.x/patterns/viewdecorators/
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.id not in admin_list:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods= ["GET", "POST"])
def login():
    login_form = LoginForm()
   
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data

        user = User.query.filter_by(email=email).first()
        if not user:
            flash("That email does not exist, please try again")
            return redirect(url_for("login"))
        elif not check_password_hash(user.password, password):
            flash("Password incorrect, please try again.")
            return redirect(url_for("login"))
        else:
            login_user(user)
            print(current_user)
            if is_admin():
                return redirect(url_for('admin')) 
            else:
                return redirect(url_for('welcome'))        
    return render_template('login.html', form=login_form)


@app.route("/register", methods= ["GET", "POST"])
def register():
    register_form = RegisterForm()

    if register_form.validate_on_submit():
        if User.query.filter_by(email=register_form.email.data).first():
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        encripted_pass = generate_password_hash(
            password= register_form.password.data,
            method= 'pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email = register_form.email.data,
            password = encripted_pass,
            username = register_form.username.data
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template('register.html', form=register_form)

@app.route("/welcome")
@login_required
def welcome():           
    return render_template('welcome.html')

@app.route("/admin")
@admin_only
def admin():           
    return render_template('admin.html')

@app.route("/logout")
def logout():   
    print(current_user)  
    logout_user()      
    print(current_user)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)