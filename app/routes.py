from flask import Blueprint, render_template, request
from .services.db import insert_project_update

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        data = {
            "project_id": request.form["project_id"],
            "status": request.form["status"]
        }
        insert_project_update(data)
        return "Update submitted!"
    return render_template("form.html")