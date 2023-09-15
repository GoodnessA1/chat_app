import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from home.home import home_bp
from auth.auth import auth_bp
from model import db, register

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "Random strings"
db.init_app(app)

app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)

app.add_url_rule("/", endpoint="index")
if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=8080)
