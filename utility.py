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

class Utility():
    
    def getFlightsByMonth(carrier, month, airport = None):
        if(not (month is None) and month == "None"):
            month = None
        cancelled = 0
        delayed = 0
        ontime = 0
        diverted = 0
        total = 0
        if(airport is None):
            if(month is None):
                times = Time.query.all()
            else:
                times = Time.query.filter_by(month = month).all() 
            
            for t in times:
                relations = Relation_table.query.filter_by(carrierID = carrier.id, timeID = t.id).all()
                for r in relations:
                    statistics = Statistics.query.filter_by(relationID = r.id).first()
                    flights = Flights.query.filter_by(id = statistics.flightID).first()
                    
                    cancelled = cancelled + flights.getCancelled()
                    ontime = ontime + flights.getOnTime()
                    delayed = delayed + flights.getDelayed()
                    diverted = diverted + flights.getDiverted()
                    total = total + flights.getTotal()
        else:
            times = []
            if(month is None):
                times = Time.query.all()
            else:
                times = Time.query.filter_by(month = month).all()

            for t in times:
                relation = Relation_table.query.filter_by(airportID = airport.id, carrierID = carrier.id, timeID = t.id).first()
                if(not (relation is None)):
                    statistics = Statistics.query.filter_by(relationID = relation.id).first()
                    flights = Flights.query.filter_by(id = statistics.flightID).first()
                    
                    cancelled = cancelled + flights.getCancelled()
                    ontime = ontime + flights.getOnTime()
                    delayed = delayed + flights.getDelayed()
                    diverted = diverted + flights.getDiverted()
                    total = total + flights.getTotal()
                
            
        dict = {
            "cancelled" : cancelled,
            "ontime" : ontime,
            "delayed" : delayed,
            "diverted" : diverted,
            "total" : total
        }
        
        if(month is None):
            return {"month" : "all", "flights-data" : dict}
        return {"month" : Time.getMonthText(month), "flights-data" : dict}
        
     
    def getMinutesByMonth(carrier, month, airport = None):
        realCarrier = carrier  ## because carrier is a variable in minutes.
        if(not (month is None) and month == "None"):
            month = None
        lateAircraft = 0
        carrier = 0
        security = 0
        weather = 0
        nationalAviationSystem = 0
        total = 0
        
        
        if(airport is None):
            times = []
            if(month is None):
                times = Time.query.all()
            else:
                times = Time.query.filter_by(month = month).all()
            for t in times:
                #print(str(airport.id) + "  " + str(carrier.id) + "  ")
                relations = Relation_table.query.filter_by(carrierID = realCarrier.id, timeID = t.id).all()
                for r in relations:
                    statistics = Statistics.query.filter_by(relationID = r.id).first()
                    delay = Delays.query.filter_by(id = statistics.delayID).first()
                    minutes = Delays_minutes.query.filter_by(id = delay.getMinutesID()).first()
                    
                    lateAircraft = lateAircraft + minutes.getLateAircraft()
                    carrier = carrier + minutes.getCarrier()
                    security = security + minutes.getSecurity()
                    weather = weather + minutes.getWeather()
                    nationalAviationSystem = nationalAviationSystem + minutes.getNationalAviationSystem()
                    total = total + minutes.getTotal()
        else:
            times = []
            if(month is None):
                times = Time.query.all()
            else:
                times = Time.query.filter_by(month = month).all()
            for t in times:
                #print(str(airport.id) + "  " + str(carrier.id) + "  ")
                relation = Relation_table.query.filter_by(airportID = airport.id, carrierID = realCarrier.id, timeID = t.id).first()
                if(not (relation is None)):
                    statistics = Statistics.query.filter_by(relationID = relation.id).first()
                    delay = Delays.query.filter_by(id = statistics.delayID).first()
                    minutes = Delays_minutes.query.filter_by(id = delay.getMinutesID()).first()
                    
                    lateAircraft = lateAircraft + minutes.getLateAircraft()
                    carrier = carrier + minutes.getCarrier()
                    security = security + minutes.getSecurity()
                    weather = weather + minutes.getWeather()
                    nationalAviationSystem = nationalAviationSystem + minutes.getNationalAviationSystem()
                    total = total + minutes.getTotal()
            
        
        dict = {
            "late-aircraft" : lateAircraft,
            "carrier" : carrier,
            "security" : security,
            "weather" : weather,
            "nas" : nationalAviationSystem,
            "total" : total
        }
        if(month is None):
            return {"month" : "all", "flights-data" : dict}
        return {"month" : Time.getMonthText(month), "flights-data" : dict}
        
    def getAmountByMonth(carrier, month, airport = None):
        realCarrier = carrier  ## because carrier is a variable in minutes.
        if(not (month is None) and month == "None"):
            month = None
        lateAircraft = 0
        carrier = 0
        security = 0
        weather = 0
        nationalAviationSystem = 0
        total = 0


        if(airport is None):
            times = []
            if(month is None):
                times = Time.query.all()
            else:
                times = Time.query.filter_by(month = month).all()
            for t in times:
                #print(str(airport.id) + "  " + str(carrier.id) + "  ")
                relations = Relation_table.query.filter_by(carrierID = realCarrier.id, timeID = t.id).all()
                for r in relations:
                    statistics = Statistics.query.filter_by(relationID = r.id).first()
                    delay = Delays.query.filter_by(id = statistics.delayID).first()
                    amount = Delays_amount.query.filter_by(id = delay.getMinutesID()).first()
                    
                    lateAircraft = lateAircraft + amount.getLateAircraft()
                    carrier = carrier + amount.getCarrier()
                    security = security + amount.getSecurity()
                    weather = weather + amount.getWeather()
                    nationalAviationSystem = nationalAviationSystem + amount.getNationalAviationSystem()
                   
        else:
            times = []
            if(month is None):
                times = Time.query.all()
            else:
                times = Time.query.filter_by(month = month).all()
            for t in times:
                #print(str(airport.id) + "  " + str(carrier.id) + "  ")
                relation = Relation_table.query.filter_by(airportID = airport.id, carrierID = realCarrier.id, timeID = t.id).first()
                if(not (relation is None)):
                    statistics = Statistics.query.filter_by(relationID = relation.id).first()
                    delay = Delays.query.filter_by(id = statistics.delayID).first()
                    amount = Delays_amount.query.filter_by(id = delay.getMinutesID()).first()
                    
                    lateAircraft = lateAircraft + amount.getLateAircraft()
                    carrier = carrier + amount.getCarrier()
                    security = security + amount.getSecurity()
                    weather = weather + amount.getWeather()
                    nationalAviationSystem = nationalAviationSystem + amount.getNationalAviationSystem()
                   
            

        dict = {
            "late-aircraft" : lateAircraft,
            "carrier" : carrier,
            "security" : security,
            "weather" : weather,
            "nas" : nationalAviationSystem,
        }
        if(month is None):
            return {"month" : "all", "flights-data" : dict}
        return {"month" : Time.getMonthText(month), "flights-data" : dict}