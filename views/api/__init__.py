from flask import Blueprint, render_template, url_for, request, redirect, flash

api_blueprint = Blueprint("api", __name__)

@api_blueprint.route("/", methods=["POST"])
def index():
	return "Api Server"

@api_blueprint.route("/register", methods=["GET","POST"])
def register():
	if request.method == "POST":
		email = request.form["email"]
		username = request.form["username"]
		password = request.form["password"]
		confirm_password = request.form["confirm_password"]
		if password != confirm_password:
			print("Password != confirm password")
	return redirect(url_for("router.register"))

@api_blueprint.route("/login", methods=["GET","POST"])
def login():
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		flash('You were successfully logged in')
		return redirect(url_for("router.index"))
	return redirect(url_for("router.login"))



