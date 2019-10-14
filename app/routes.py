from app import app, db
from keys import api_key
from datetime import datetime
from werkzeug.urls import url_parse
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required


@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    return render_template('index.html', title='home')

@app.route('/category')
def category():
    page = request.args.get('page', 1, type=int)
    return render_template('category.html', title='category')

@app.route('/checkout')
def checkout():
    page = request.args.get('page', 1, type=int)
    return render_template('checkout.html', title='checkout')

@app.route('/cart')
def cart():
    page = request.args.get('page', 1, type=int)
    return render_template('cart.html', title='cart')

@app.route('/contact')
def contact():
    page = request.args.get('page', 1, type=int)
    return render_template('contact.html', title='contact')

@app.route('/login')
def login():
    page = request.args.get('page', 1, type=int)
    return render_template('login.html', title='login')

@app.route('/single_product')
def single_product():
    page = request.args.get('page', 1, type=int)
    return render_template('single-product.html', title='single product')

@app.route('/confirmation')
def confirmation():
    page = request.args.get('page', 1, type=int)
    return render_template('confirmation.html', title='confirmation')






