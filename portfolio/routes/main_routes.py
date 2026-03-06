from flask import Blueprint, current_app, render_template

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    return render_template(
        "index.html",
        profile=current_app.config["PROFILE"],
        skills=current_app.config["SKILLS"],
        highlights=current_app.config["KEY_HIGHLIGHTS"],
        featured_projects=current_app.config["PROJECTS"][:2],
    )


@main_bp.route("/resume")
def resume():
    return render_template(
        "resume.html",
        profile=current_app.config["PROFILE"],
        skills=current_app.config["SKILLS"],
        highlights=current_app.config["KEY_HIGHLIGHTS"],
        experience=current_app.config["EXPERIENCE"],
    )


@main_bp.route("/projects")
def projects():
    return render_template("projects.html", projects=current_app.config["PROJECTS"])


@main_bp.route("/contact")
def contact():
    return render_template("contact.html")
