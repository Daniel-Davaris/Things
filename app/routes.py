from app import app, db
from keys import api_key
from datetime import datetime
from werkzeug.urls import url_parse
from flask import render_template, flash, redirect, url_for, request, json
from flask_login import login_user, logout_user, current_user, login_required
import os


@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
def home():
    
    return render_template('index.html', title='home')

@app.route('/category')
def category():
    title = "Categories"
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static\\data", "test_data.json")
    data = json.load(open(json_url))
    # for product in range(len(data)):
        
        # ea = data[product]
        # id = ea["id"]
        # product_id = product["product_id"]
        # title = ea["title"]
        # desc = ea["desc"]
        # details = ea["details"]
        # bullets = ea["bullets"]
        # brand = ea["brand"]
        # imgs = product["imgs"]
        # categories = ea["categories"]
        # old_price = ea["old_price"]
        # new_price = ea["new_price"]

    # print(first["title"])
    return render_template('category.html', data=data, title=title)
    


@app.route('/checkout')
def checkout():
    
    return render_template('checkout.html', title='checkout')

@app.route('/cart')
def cart():
    
    return render_template('cart.html', title='cart')

@app.route('/contact')
def contact():
    
    return render_template('contact.html', title='contact')

@app.route('/login')
def login():
    
    return render_template('login.html', title='login')

@app.route('/single_product')
def single_product():
    
    return render_template('single-product.html', title='single product')

@app.route('/confirmation')
def confirmation():
    
    return render_template('confirmation.html', title='confirmation')






