# config.py

import os

class BaseConfig:
	"""
	Base Config
	"""
	DEBUG = False
	TESTING = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = 'its_a_secret'

class DevelopmentConfig(BaseConfig):
	"""
	Development config
	"""
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestingConfig(BaseConfig):
	"""
	Tsting config
	"""
	DEBUG = True
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')

class ProductionConfig(BaseConfig):
	"""
	Production config
	"""
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
