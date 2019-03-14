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
    
    def getFlightsByMonth(airport, carrier, month):
        cancelled = 0
        delayed = 0
        ontime = 0
        diverted = 0
        total = 0
    
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
        return {"month" : Time.getMonthText(month), "flights-data" : dict}
    
     
    def getMinutesByMonth(airport, carrier, month):
        realCarrier = carrier  ## because carrier is a variable in minutes.
        print(airport)
        print(carrier)
        lateAircraft = 0
        carrier = 0
        security = 0
        weather = 0
        nationalAviationSystem = 0
        total = 0

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
        return {"month" : Time.getMonthText(month), "flights-data" : dict}