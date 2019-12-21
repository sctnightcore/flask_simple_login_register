from flask import Blueprint, render_template, url_for, request, redirect, flash

api_blueprint = Blueprint("api", __name__)

@api_blueprint.route("/", methods=["POST"])
def index():
	return "Api Server"
