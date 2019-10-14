from app import app
from flask import render_template


@app.route('/')
def category():
    return render_template('') # Caterogyr html