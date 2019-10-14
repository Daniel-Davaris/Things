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
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(20))
    title = db.Column(db.String(50))
    desc = db.Column(db.String(300))
    bullets = db.Column(db.String(100))
    old_price = db.Column(db.Integer)
    new_price = db.Column(db.Integer)



class Image(db.Model):
    __tablename__ = 'image'

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer)
    img_url = db.Column(db.String(100))
    is_primary = db.Column(db.Boolean)


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(100)


class Category_Item(db.Model):
    __tablename__ = 'category_item'
    item_id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, primary_key=True)


class Brand(db.Model):
    __tablename__ = 'brand'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(100)


class Brand_Item(db.Model):
    __tablename__ = 'brand_item'

    item_id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, primary_key=True)


class Details(db.Model):
    __tablename__ = 'details'

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer)
    text = db.Column(db.String(200))
