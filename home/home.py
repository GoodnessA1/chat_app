from flask import Blueprint, render_template, redirect

home_bp = Blueprint('home_bp', __name__,
                    template_folder="templates", static_folder="static")

@home_bp.route('/')
def index():
    return render_template("index.html")
