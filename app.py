import flask
from flask import Flask
from home.home import home_bp
from auth.auth import auth_bp

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)

app.add_url_rule("/", endpoint="index")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
