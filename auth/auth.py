from flask import Blueprint, render_template, redirect, url_for, request, flash
from model import db, register, load_all

auth_bp = Blueprint("auth_bp", __name__,
                    template_folder="templates", url_prefix=('/auth'),
                    static_folder="static")

@auth_bp.route("/login", methods=('GET', 'POST'))
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        login_details = load_all()
        for data in login_details:
            print(data.name)
            print(data.password)
    return render_template("login.html")

@auth_bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        secret_key = request.form['secret_key']

        add_details = register(name=username, password=password, secret_key=secret_key)
        try:
            db.session.add(add_details)
            db.session.commit()
            return redirect(url_for("auth.login"))
        except:
            error = "USERNAME OR PASSWORD EXISTS"
            flash(error)
    return render_template("register.html")
