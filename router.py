from flask import Blueprint, render_template, redirect, url_for, request
from forms import LoginForm, RegisterForm

router_blueprint = Blueprint("router", __name__)

@router_blueprint.route("/", methods=["GET", "POST"])
def index():
	return render_template("index.html")

@router_blueprint.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		# login to web
		return redirect(url_for(".dashboard"))
	return render_template("login.html",form=form)

@router_blueprint.route("/register", methods=["GET", "POST"])
def register():
	form = RegisterForm()
	return render_template("register.html", form=form)

@router_blueprint.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    return render_template("dashboard.html")

@router_blueprint.route("/logout", methods=["GET", "POST"])
def logout():
	return redirect(url_for(".index"))