from app import app as application

# here we have the import statments for the project app and database as will is the database sections from our models 
# from app import app, db
# from app.models import User, Post


# this peice of code here sets up the python shell so then if we want to test/ run commands on our database it is quicker and we int have to type configuration variiables everytime

# @app.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'User': User, 'Post': Post}

# import os
# import sys


# sys.path.insert(0, os.path.dirname(__file__))


# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/plain')])
#     message = 'It works!\n'
#     version = 'Python %s\n' % sys.version.split()[0]
#     response = '\n'.join([message, version])
#     return [response.encode()]
