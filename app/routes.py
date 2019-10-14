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




