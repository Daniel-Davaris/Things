from config import Config

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
cors = CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

from app.api import api
app.register_blueprint(api, url_prefix='/api/')


login.login_view = 'auth.login'
login.login_message = ('Please log in to access this page.')

from app import models, routes
