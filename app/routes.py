from app import app
from flask import render_template
from keys import api_key


@app.route('/')
def category():
    return render_template('') # Caterogyr html