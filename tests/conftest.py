import pytest
from app import create_app
from flask import url_for

@pytest.fixture
def app():
	app = create_app()
	app.debug = True
	return app
 
 
