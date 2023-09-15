#This is for database modelling

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class register(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False, unique=True)
    secret_key = db.Column(db.Integer, nullable=False, unique=True)

def load_all():
    data = register.query.all()
    return data
