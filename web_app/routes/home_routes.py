

from flask import Blueprint, render_template, jsonify


home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("VISITED THE HOME PAGE")
    return render_template("prepare_to_predict.html")

@home_routes.route("/about")
def about():
    return "About me"
