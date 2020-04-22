

from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def front_page():
    return f"FRONT PAGE Y DID U CLICK THAT THO"

@home_routes.route("/about")
def about():
    return "About me"
