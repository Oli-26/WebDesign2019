import csv
import json
import flask
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from __init__ import app, db


#### CORE
from Core.airport import Airport
from Core.time import Time 
from Core.carrier import Carrier
from Core.flights import Flights
from Core.delays_minutes import Delays_minutes
from Core.delays_amount import Delays_amount
from Core.delays import Delays
from Core.relation_table import Relation_table
from Core.statistics import Statistics



#airport1 = Airport(c = "AAA", n = "American Airlines Air")
#db.session.add(airport1)
#db.session.commit()


airports = Airport.query.all()
for a in airports:
    #db.session.delete(a);
    print(str(a.id) + "  |  " + a.getName() + "  |  " + a.getCode())



carriers = Carrier.query.all()
for c in carriers:
    #db.session.delete(a);
    print(str(c.id) + "  |  " + c.getName() + "  |  " + c.getCode())

times = Time.query.all()
for t in times:
    db.session.delete(t)
    print(t.getLabel(t.getId()))
db.session.commit()
    


    #Load Json dictionary
    # in each instance, check if time, airport or carrier exists
    # if they do, get primary id, otherwise create new instance and get primary id
    # next create relation between the three ids
def Populate():
    with open("airlines.json") as f:
        data = json.load(f)
        for index in data:
            airportId = -1
            carrierId = -1
            timeId = -1
            print("looping")
        
            try:
                instance = Airport.query.filter_by(name=index["airport"]["name"]).first()
                if(instance != None):
                    airportId = instance.id
                else:
                    newAirport = Airport(c = index["airport"]["code"], n = index["airport"]["name"])
                    db.session.add(newAirport)
                    airportId = newAirport.id
                    db.session.commit()
            except:
                print("airport add failed")
                db.session.rollback()
            
            try:
                instance = Carrier.query.filter_by(name=index["carrier"]["name"]).first()
                if(instance != None):
                    carrierId = instance.id
                else:
                    newCarrier = Carrier(c = index["carrier"]["code"], n = index["carrier"]["name"])
                    db.session.add(newCarrier)
                    carrierId = newCarrier.id
                    db.session.commit()
            except:
                print("Adding new carrier failed! " + index["carrier"]["code"])
                db.session.rollback()
                    #session.query(User).filter(User.name == 'fred')
            try:        
                instance = Time.query.filter_by(month = index["time"]["month"], year = index["time"]["year"]).first()
                if(instance != None):
                    timeId = instance.id
                    #print("Skipping!")
                else:
                    newTime = Time(m = index["time"]["month"], y= index["time"]["year"])
                    db.session.add(newTime)
                    timeId = newTime.id
                    db.session.commit()
            except:
                print("adding time failed")
                db.session.rollback()
            
            if(airportId != -1 and carrierId != -1 and timeId != -1):
                # Add relation 
                print("relation found!")
                 
            
            
            
            
            
            
            
            
#Populate()            
            
#app.run(port='5002', ssl_context='adhoc')  


