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

def insert_all(x):
    print(x[0] + " " + x[1] + " " + x[2])
    add_details = register(name=x[0], password=x[1], secret_key=x[2])
    db.session.add(add_details)
    db.session.commit()
    print("-------- ADD SUCCESSFUL ----------")
