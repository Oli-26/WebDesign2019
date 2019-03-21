import csv
import json
import flask
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from __init__ import app, db

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

db.create_all()
db.session.commit()
i = 0
with open("airlines.json") as f:
    data = json.load(f)
    dataLength = len(data)
    for index in data:
        airportId = None
        carrierId = None
        timeId = None
        minsId = None
        amountId = None
        flightsId = None
        relationId = None
        delayId = None
        
        #print("looping(" + str(round(1000*i/dataLength)/10) +"%)")
        i = i + 1
        if i % 50 == 0:
            print(str(round(1000*i/dataLength/10)) + "%")
         #   break
        try:
            instance = Airport.query.filter_by(name=index["airport"]["name"]).first()
            if instance is not None:
                airportId = instance.id
                #print("Loaded airport with id " + str(airportId))
            else:
                newAirport = Airport(c = index["airport"]["code"], n = index["airport"]["name"])
                db.session.add(newAirport)
              
                db.session.commit()
                airportId = newAirport.id
                #print("Added airport with id " + str(airportId))
            
        except:
            print("airport add failed")
            db.session.rollback()

        try:
            instance = Carrier.query.filter_by(code=(index["carrier"]["code"]), name=(index["carrier"]["name"])).first()
            if instance is not None:
                carrierId = instance.id
                # print("Loaded carrier with id " + str(carrierId))
            else:
                newCarrier = Carrier(c=index["carrier"]["code"], n=index["carrier"]["name"])
                db.session.add(newCarrier)
                db.session.commit()
                carrierId = newCarrier.id
                # print("newCarrier code: " + newCarrier.code + "     name: " + newCarrier.name)
                # print("Added carrier with id " + str(carrierId))
        except:
            print("Adding new carrier failed! " + index["carrier"]["code"])
            db.session.rollback()
                #session.query(User).filter(User.name == 'fred')

        try:        
            instance = Time.query.filter_by(month = index["time"]["month"], year = index["time"]["year"]).first()
            if instance is not None:
                timeId = instance.id
                #print("Loaded time with id " + str(timeId))
                #print("Skipping!")
            else:
                newTime = Time(m = index["time"]["month"], y= index["time"]["year"])
                db.session.add(newTime)
              
                db.session.commit()
                
                timeId = newTime.id
                #print("Added time with id " + str(timeId))
        except:
            print("adding time failed")
            db.session.rollback()
        
        if airportId is not None and carrierId is not None and timeId is not None:
                # Add relation
            try:
                #print("relation found!" + str(airportId) + "   " + str(carrierId) + "     " + str(timeId))
                newRelation = Relation_table(aID = airportId, cID = carrierId, tID = timeId)
                db.session.add(newRelation)
                db.session.commit()
                relationId = newRelation.id
            except:
                print("adding relation failed")
                db.session.rollback()
                    
        try:
          
            cancelled = index["statistics"]["flights"]["cancelled"]
            ontime = index["statistics"]["flights"]["on time"]
            total = index["statistics"]["flights"]["total"]
            delayed = index["statistics"]["flights"]["delayed"]
            diverted = index["statistics"]["flights"]["diverted"]
                
            newFlights = Flights(cancel = cancelled, onTime = ontime, t = total, delay = delayed, divert = diverted)
            db.session.add(newFlights)
            db.session.commit()
            flightsId = newFlights.id
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
            minsId = newMinsDelay.id
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
            amountId = newAmountDelay.id
        except:
            print("amount delayed add failed")
            db.session.rollback()
        
        if minsId is not None and amountId is not None:
            try:
                newDelayRelation = Delays(mID = minsId, aID = amountId)
                db.session.add(newDelayRelation)
                db.session.commit()
                delayId = newDelayRelation.id
            except:
                db.session.rollback()
                print("delay relation failed")
          
        if relationId is not None and delayId is not None and flightsId is not None:
            try:
                newStatistics = Statistics(rID = relationId, fID = flightsId, dID = delayId)
                db.session.add(newStatistics)
                db.session.commit()
            except:
                db.session.rollback()
                print("statistics add failed")
        