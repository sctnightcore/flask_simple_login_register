from flask import Blueprint, render_template

auth_blueprint = Blueprint("auth", __name__)

@auth_blueprint.route("/", methods=["GET"])
def index():
	return "index"


