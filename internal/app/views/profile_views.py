from flask import Blueprint, request, render_template, session, redirect, url_for

from internal.app.services import profile_service
from pkg.helpers import login_required

profile_blueprint = Blueprint("profile", __name__)


@profile_blueprint.route("/", methods=["GET", "PATCH"])
@login_required
def profile():
    uid = session.get("user_id")
    if request.method == "GET":
        data = profile_service.get_profile_info(uid)
        return render_template("profile.html", data=data)
    if request.method == "PATCH":
        success = profile_service.partial_update(uid, request.form)
        if not success:
            return render_template("profile.html", error="Поле не соответствует требованиям")
        return redirect(url_for("profile.profile"))


@profile_blueprint.route("surveys/", methods=["GET"])
@login_required
def user_surveys():
    uid = session.get("user_id")
    user_surveys = profile_service.all_user_surveys(uid)
    return render_template("profile_surveys.html", surveys=user_surveys)


