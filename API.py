import csv
import json
import flask
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from __init__ import app, db


## INIT and UPDATE core objects

from Core.airport import Airport
from Core.time import Time 
from Core.carrier import Carrier
from Core.flights import Flights
from Core.delays_minutes import Delays_minutes
from Core.delays_amount import Delays_amount
from Core.delays import Delays
from Core.relation_table import Relation_table
from Core.statistics import Statistics
db.init_app(app)


#db.create_all()
#db.session.commit()





airports = Airport.query.all()
for a in airports:
    print(str(a.id) + "  |  " + a.getName() + "  |  " + a.getCode())



carriers = Carrier.query.all()
for c in carriers:
    #db.session.delete(a);
    print(str(c.id) + "  |  " + c.getName() + "  |  " + c.getCode())

times = Time.query.all()
for t in times:
    print(t.getLabel(t.getId()))
   

relations = Relation_table.query.all()
j = 0
for r in relations:
    j = j + 1
    if(j > 100):
        break;
    print(str(r.getAirportID()) + " -- " + str(r.getCarrierID()) + " -- " + str(r.getTimeID()))

        
#print("statistics")
#statistics = Statistics.query.all()
#for s in statistics:
 #   print(str(s.relationID) + " -- " + str(s.flightID) + " -- " + str(s.delayID))

#app.run(port='5002', ssl_context='adhoc')  


