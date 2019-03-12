from flask import Flask
import sqlalchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

print(SQLALCHEMY_DATABASE_URI)
SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

#migrate = Migrate(app, db)


## INIT and UPDATE core objects
from Core.airport import Airport
from Core.time import Time 
from Core.carrier import Carrier
from Core.flights import Flights
#from Core.delays_minutes import Delays_minutes
#from Core.delays_amount import Delays_amount
#from Core.delays import Delays
from Core.relation_table import Relation_table
#from Core.statistics import Statistics

db.init_app(app)
try:
    db.create_all()
    db.session.commit()
except:
    db.session.rollback()

    
    
    
