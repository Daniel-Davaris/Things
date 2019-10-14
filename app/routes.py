from app import app
from flask import render_template
from keys import api_key

from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
# from app.forms import LoginForm, RegistrationForm, EditProfileForm, PostForm, \
#     ResetPasswordRequestForm, ResetPasswordForm
# from app.models import User, Post
# from app.email import send_password_reset_email



@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    # posts = Post.query.order_by(Post.timestamp.desc()).paginate(
    #     page, app.config['POSTS_PER_PAGE'], False)
    # next_url = url_for('explore', page=posts.next_num) \
    #     if posts.has_next else None
    # prev_url = url_for('explore', page=posts.prev_num) \
    #     if posts.has_prev else None
    return render_template('index.html', title='home')


