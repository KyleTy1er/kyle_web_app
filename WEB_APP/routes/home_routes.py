

from flask import Blueprint, render_template, jsonify


home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def front_page():
    return render_template("home.html")

@home_routes.route("/about")
def about():
    return "About me"
