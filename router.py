from flask import Blueprint, render_template, redirect, url_for, request
from forms import LoginForm, RegisterForm
router_blueprint = Blueprint("router", __name__)

@router_blueprint.route("/", methods=["GET"])
def index():
	return render_template("index.html")

@router_blueprint.route("/login", methods=["GET"])
def login():
	form = LoginForm()
	return render_template("login.html",form=form)

@router_blueprint.route("/register", methods=["GET"])
def register():
	form = RegisterForm()
	return render_template("register.html", form=form)