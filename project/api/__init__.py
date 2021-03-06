# project/api/__init__.py

import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from project.api.views import users_blueprint

db = SQLAlchemy()

def create_app():
	app = Flask(__name)
	app_settings = os.getenv('APP_SETTINGS')
	app.config.from_object(app_settings)

	db.init_app(app)
	app.register_blueprint(users_blueprint)

	return app
