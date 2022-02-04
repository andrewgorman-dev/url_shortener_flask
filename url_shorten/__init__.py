# from email.policy import default
from flask import Flask
# from url_shorten.forms import UrlForm
from flask_sqlalchemy import SQLAlchemy
# import string
# import random


app = Flask(__name__)
app.config['SECRET_KEY'] = '2ae4b2ffdc1ce77936d991b3daa8d6ce'
# SQLLITE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
# MySQL
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/short_urls'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


@app.before_first_request
def create_tables():
    db.create_all()

from url_shorten import routes