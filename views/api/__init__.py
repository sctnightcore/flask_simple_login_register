from flask import Blueprint, render_template, url_for, request, redirect, flash

api_blueprint = Blueprint("api", __name__)

@api_blueprint.route("/", methods=["POST"])
def index():
	return "Api Server"

@api_blueprint.route("/login", methods=["POST"])
def login():
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]

	return redirect(url_for("router.login"))

@api_blueprint.route("/register", methods=["POST"])
def register():
	if request.method == "POST":
		email = request.form["email"]
		username = request.form["username"]
		password = request.form["password"]
		confirm_password = request.form["confirm_password"]

	return redirect(url_for("router.register"))

