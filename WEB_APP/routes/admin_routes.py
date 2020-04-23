# web_app/routes/admin_routes.py

from flask import Blueprint, jsonify, request, render_template, flash, redirect

from web_app.models import db

admin_routes = Blueprint("admin_routes", __name__)

@admin_routes.route("/reset", methods=['GET', 'POST'])
def reset_db():
    print("RESET ROUTE...")
    print("FORM DATA:", dict(request.form))
    print(type(db))
    db.drop_all()
    db.create_all()
    return render_template("reset_db.html", db=db)