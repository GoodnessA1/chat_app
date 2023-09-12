from flask import Blueprint, render_template, redirect, url_for, request, flash

auth_bp = Blueprint("auth_bp", __name__,
                    template_folder="templates", url_prefix=('/auth'),
                    static_folder="static")

@auth_bp.route("/login", methods=('GET', 'POST'))
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        error = None
        if password == "goodness":
            return redirect(url_for("index"))
        else:
            error = "Invalid password"

        flash(error)
    return render_template("login.html")

@auth_bp.route("/register", methods=("GET", "POST"))
def register():
    return render_template("register.html")
