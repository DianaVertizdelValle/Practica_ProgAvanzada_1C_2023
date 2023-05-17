from modules.config import db
from sqlalchemy import Column, Integer, Numeric, String, ForeignKey 
from sqlalchemy.orm import relationship
from flask_login import UserMixin


##CREATE TABLE IN DB
class Book(db.Model):
    __tablename__ = 'books'
    id = Column(Integer(), primary_key=True)
    nombre = Column(String(1000), nullable=False, unique=True)
    autor = Column(String(1000), nullable=False)
    puntaje = Column(Numeric(2,1))

    def to_dict(self): 
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary