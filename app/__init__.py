from config import Config
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,static_folder=os.path.abspath('static'))
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)


login.login_view = 'auth.login'
login.login_message = ('Please log in to access this page.')

from app import models, routes