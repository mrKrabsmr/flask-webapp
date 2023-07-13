from flask import Blueprint, request, render_template, redirect, url_for

from internal.app.services import registration_service

registration_blueprint = Blueprint("registration", __name__)


@registration_blueprint.route("/", methods=["GET", "POST"])
def registration():
    if request.method == "GET":
        return render_template("registration.html")
    if request.method == "POST":
        success = registration_service.create_user(request.form)
        if not success:
            return render_template("registration.html", error="Поля не соответствуют требованиям")
        return redirect(url_for("profile.profile"))


