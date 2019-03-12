from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
print(SQLALCHEMY_DATABASE_URI)
#SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)

db = SQLAlchemy(app)