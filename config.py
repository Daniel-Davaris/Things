"""Configuration for flask app."""
import os
import creds
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
	"""Object containing all of the config data for the app"""
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key'

	SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s'\
		% creds.POSTGRES
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
	# ! DISABLE IN PROD
	DEBUG = True