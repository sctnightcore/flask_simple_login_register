from flask import Flask
from router import router_blueprint
from views.api import api_blueprint
#from views.auth import auth_blueprint
app = Flask(__name__)
app.secret_key = "sctnightcore"
#router 
app.register_blueprint(router_blueprint, url_prefix="/")
#auth

#api
app.register_blueprint(api_blueprint, url_prefix="/api")


if __name__ == "__main__":
	app.run(debug=True)
