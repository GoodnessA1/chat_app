from flask import Blueprint, render_template, redirect, url_for, request, flash
from model import *

auth_bp = Blueprint("auth_bp", __name__,
                    template_folder="templates",
                    static_folder="static")

@auth_bp.route("/", methods=('GET', 'POST'))
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        login_details = load_all()
        error = None
        print("<<<<<<<<<<<<<<DONE>>>>>>>>>>>>>>>" + username + "  " + password)
        for data in login_details:
            n = data.name
            p = data.password

        if n != username:
            error = "INVALID USERNAME OR PASSWORD"

        elif p != password:
            error = "INVALID USERNAME OR PASSWORD"
        
        if error == None:
            return redirect(url_for("home_bp.index"))

        flash(error)
    return render_template("login.html")

@auth_bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        secret_key = request.form['secret_key']
        print(username + " " + password + " " + secret_key)
        add_details = [username, password, secret_key]
        try:
            insert_all(add_details)
            return redirect(url_for("index"))
        except:
            flash("USER ALREADY EXISTS")
    return render_template("register.html")
