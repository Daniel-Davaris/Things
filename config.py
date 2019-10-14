"""Configuration for flask app."""
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
	"""Object containing all of the config data for the app"""
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key'


	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'dev.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	
	# ! DISABLE IN PROD
	DEBUG = True
