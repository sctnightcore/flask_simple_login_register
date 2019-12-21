from flask import Flask

def create_app():
	app = Flask(__name__)
	app.config.from_object("settings.Config")

	with app.app_context():
		from router import router_blueprint
		from views.api import api_blueprint
		#router
		app.register_blueprint(router_blueprint, url_prefix="/")
		#api
		app.register_blueprint(api_blueprint, url_prefix="/api")
		return app


if __name__ == "__main__":
	app = create_app()
	app.run(debug=True)
