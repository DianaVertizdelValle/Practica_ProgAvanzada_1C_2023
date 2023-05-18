from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask("server")

#indicar la ubicación de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
#La instancia de la clase SQLAlchemy permite que la aplicación interactúe con la base de datos
db = SQLAlchemy(app)

