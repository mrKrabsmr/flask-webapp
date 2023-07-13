from flask import Blueprint, request, render_template, redirect, session, url_for

from internal.app.services import login_service
from pkg.helpers import login_required

login_blueprint = Blueprint("login", __name__)


@login_blueprint.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        if not login_service.login_user(request.form):
            return render_template("login.html", error="Неверная пара login - password")
        return redirect(url_for("profile"))


@login_blueprint.route("/logout/")
@login_required
def logout():
    session.clear()
    return redirect(url_for("login.login"))
