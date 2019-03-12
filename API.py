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
#from Core.delays import Delays
#from Core.relation_table import Relation_table
#from Core.statistics import Statistics
db.init_app(app)

#try:
db.create_all()
db.session.commit()
#except:
    #print("Create all failed")
    #db.session.rollback()
    #print("ff")



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
    print(t.getLabel(t.getId()))
db.session.commit()
    

#relations = Relation_table.query.all()
#for r in relations:
#    print(t.getAirportID() + " -- " + t.getCarrierID() + " -- " + t.getTimeID())

    #Load Json dictionary
    # in each instance, check if time, airport or carrier exists
    # if they do, get primary id, otherwise create new instance and get primary id
    # next create relation between the three ids
def Populate():
    i = 0
    with open("airlines.json") as f:
        data = json.load(f)
        for index in data:
            airportId = -1
            carrierId = -1
            timeId = -1
            print("looping(" + i +")")
            i = i + 1
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
                try:
                    print("relation found!")
                    newRelation = Relation_table(aID = airportId, cID = carrierId, tID = timeId)
                except:
                    print("adding relation failed")
                    db.session.rollback()
                    
            try:
                #instance = Flights.query.filter_by(name=index["airport"]["name"]).first()
                
                cancelled = index["statistics"]["flights"]["cancelled"]
                ontime = index["statistics"]["flights"]["on time"]
                total = index["statistics"]["flights"]["total"]
                delayed = index["statistics"]["flights"]["delayed"]
                diverted = index["statistics"]["flights"]["diverted"]
                    
                newFlights = Flights(cancel = cancelled, onTime = ontime, t = total, delay = delayed, divert = diverted)
                db.session.add(newFlights)
                db.session.commit()
            except:
                print("flights add failed")
                db.session.rollback()
            
            try:
                #instance = Flights.query.filter_by(name=index["airport"]["name"]).first()
                lateAircraft =  index["statistics"]["minutes delayed"]["late aircraft"]
                weather =  index["statistics"]["minutes delayed"]["weather"]
                security =  index["statistics"]["minutes delayed"]["security"]
                nas =  index["statistics"]["minutes delayed"]["national aviation system"]
                carrier = index["statistics"]["minutes delayed"]["carrier"]
                t =  index["statistics"]["minutes delayed"]["total"]
                newMinsDelay = Delays_minutes(la=lateAircraft, c=carrier, s=security, w=weather, nas = nas, t = t)
                db.session.add(newMinsDelay)
                db.session.commit()
            except:
                print("minutes delayed add failed")
                db.session.rollback()
            
            
            try:
                lateAircraft =  index["statistics"]["# of delays"]["late aircraft"]
                weather =  index["statistics"]["# of delays"]["weather"]
                security =  index["statistics"]["# of delays"]["security"]
                nas =  index["statistics"]["# of delays"]["national aviation system"]
                carrier = index["statistics"]["# of delays"]["carrier"]
                    
                newAmountDelay = Delays_amount(la=lateAircraft, c=carrier, s=security, w=weather, nas = nas)
                db.session.add(newAmountDelay)
                db.session.commit()
            except:
                print("amount delayed add failed")
                db.session.rollback()
            
            
            
            
            
            
#Populate()            
            
#app.run(port='5002', ssl_context='adhoc')  


