from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_paginate import Pagination
from flask import Flask

DEBUG = False
SCHEMA_NAME = 'world_cities_test'
# DBHOST = 'ksl' # '127.0.0.1'
DBHOST = '127.0.0.1' 
DBUNAME = 'dbadmin'
PASSWORD = 'mysecret_password'
PORT = '3306'

# configure the SQLite database, relative to the app instance folder
app = Flask(__name__, template_folder='templates')   # this is referenced from the WSGI webserver waitress, 
                        # either from from outside via filename:app
                        # or from webserving python main() mfa_server.py
                        # this definition has to be before the routes
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DBUNAME}:{PASSWORD}@{DBHOST}:{PORT}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy()
db.__init__(app)


