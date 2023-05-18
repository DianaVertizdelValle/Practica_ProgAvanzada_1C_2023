from flask import render_template, request, redirect, url_for, flash, abort
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from functools import wraps
from modules.config import app, db, login_manager
from modules.databases import Book, User
from modules.forms import LoginForm, RegisterForm

admin_list = [1]

with app.app_context():
    db.create_all()

def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated and current_user.id not in admin_list:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function

def is_admin():
    if current_user.is_authenticated and current_user.id in admin_list:
        return True
    else:
        return False


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

#Muestra todos los libros de todos los usuarios
@app.route("/", methods=['GET', 'POST'])
def home():    
    lista_libros = Book.query.all()
    if len(lista_libros) == 0:
        return render_template("home.html", esta_vacia=True)
    else:
        return render_template("home.html", esta_vacia=False, lista_libros=lista_libros )

#Muestra los libros filtrados por usuario excepto admin
@app.route("/my_books", methods=['GET', 'POST'])
@login_required
def my_books():    
    if request.args.get('del'):
        id = request.args.get('id')
        db.session.delete(Book.query.get(id))
        db.session.commit()

    if is_admin():
        lista_libros = Book.query.all()
    else:
        lista_libros = Book.query.filter_by(user_id =current_user.id).all()

    if len(lista_libros) == 0:
        return render_template(
                                "home.html", esta_vacia=True, 
                                logged_in=current_user.is_authenticated
                              )
    else:
        return render_template(
                                    "home.html", esta_vacia=False, lista_libros=lista_libros ,
                                    logged_in=current_user.is_authenticated 
                              )
    

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
            return redirect(url_for('my_books'))        
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
            name = register_form.username.data
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template('register.html', form=register_form)


@app.route("/add", methods=['GET', 'POST'])
@login_required
def agregar():
    if request.method == 'POST':
        if Book.query.filter_by(nombre=request.form["titulo"]).first() == None:
            libro = Book(
                nombre = request.form["titulo"],
                autor = request.form["autor"],
                puntaje = float(request.form["puntaje"]),
                user_id = current_user.id
            )
            db.session.add(libro)
            db.session.commit()
        else:
            flash("El libro ya está agregado a la biblioteca")
        return redirect(url_for('my_books'))
    return render_template("add.html")

@app.route("/edit", methods=['GET', 'POST'])
@login_required
def edit():
    if request.method == 'POST':
        id = request.form['id']
        libro_a_editar = db.session.query(Book).get(id)
        libro_a_editar.nombre = request.form["titulo"]
        libro_a_editar.autor = request.form["autor"]
        libro_a_editar.puntaje = float(request.form["puntaje"])
        db.session.commit()
        return redirect(url_for('my_books'))       
    id = request.args.get('id')
    libro_a_editar = Book.query.get(id)
    
    return render_template("edit.html", libro=libro_a_editar)

@app.route("/logout")
def logout():   
    print(current_user)  
    logout_user()      
    print(current_user)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)