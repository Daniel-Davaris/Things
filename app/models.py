import hashlib
from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Person(db.Model, UserMixin):
    __tablename__ = 'person'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    pass_hash = db.Column(db.String(128))
    joined = db.Column(db.DateTime, default=datetime.utcnow)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def setPass(self, password):
        self.pass_hash = generate_password_hash(str(password))

    def checkPass(self, password):
        return check_password_hash(self.pass_hash, password)

class Item(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Blob)
    title = db.Column(db.String(50))
    desc = db.Column(db.String(300))


