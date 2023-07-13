from flask import Blueprint, request, render_template, session, redirect, url_for

from internal.app.services import survey_service
from pkg.helpers import login_required

survey_blueprint = Blueprint("survey", __name__)


@survey_blueprint.route("/")
@login_required
def list_surveys():
    if request.method == "GET":
        page = request.args.get("page", 1, type=int)
        data, total_pages = survey_service.get_survey_list_data(page)
        return render_template("survey.html", data=data, total_pages=total_pages)


@survey_blueprint.route("/<int:pk>/", methods=["GET", "POST"])
@login_required
def start_survey(pk):
    page = request.args.get("page", 1, type=int)
    if request.method == "GET":
        survey = survey_service.get_survey(pk)
        if not survey:
            return redirect(url_for("survey.list_surveys"))
        question = survey_service.get_question(pk, page)
        if not question:
            return redirect(url_for("result"))
        return render_template("question.html", data=question)
    if request.method == "POST":
        answer = request.form.get("answer")
        if not answer:
            return render_template("question.html", error="Выберите один вариант")
        if survey_service.check_answer(pk, page, answer):
            process = session.get("process")
            if not process:
                session["process"] = 1
            else:
                session["process"] += 1
        return redirect(f"page={page + 1}")


@survey_blueprint.route("/create/", methods=["GET", "POST"])
@login_required
def create_survey():
    if request.method == "GET":
        return render_template("create_survey.html")
    if request.method == "POST":
        uid = session.get("user_id")
        survey_service.create_survey(uid, request.form)
        return redirect(url_for("list_surveys"))
