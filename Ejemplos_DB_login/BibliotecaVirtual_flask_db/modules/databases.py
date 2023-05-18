#2) importamos el objeto db y creamos los modelos de nuestras bases de datos
# definiendo clases
from modules.config import db
from sqlalchemy import Column, Integer, String, Float

#https://sqlitebrowser.org/dl/
class Book(db.Model):
    __tablename__ = 'books'
    id = Column(Integer(), primary_key=True)
    nombre = Column(String(1000), nullable=False, unique=True)
    autor = Column(String(1000), nullable=False)
    puntaje = Column(Float())

    # def to_dict(self): 
    #     dictionary = {}
    #     for column in self.__table__.columns:
    #         dictionary[column.name] = getattr(self, column.name)
    #     return dictionary

#db.Model es una clase base de SQLAlchemy que se utiliza para definir modelos
#de datos en una aplicación Flask. 
#Esta clase proporciona una interfaz para interactuar con la base de datos utilizando 
#objetos Python que representan las tablas y columnas de la base de datos.

#__tablename__ corresponde al nombre de la tabla SQL dentro de la base de datos

#primary_key es un campo o conjunto de campos que identifica de manera única cada registro en una tabla.
#suele ser un campo numérico autoincremental que no permite valores duplicados y que se utiliza como 
#índice para acceder a los registros de la tabla de forma rápida y eficiente