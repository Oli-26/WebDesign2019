import csv
import json
import flask
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from __init__ import app, db
import math

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
    
    def getFlightsByMonth(realCarrier, month, airport = None):
        if month is not None and month == "None":
            month = None
        cancelled = 0
        delayed = 0
        ontime = 0
        diverted = 0
        total = 0

        if month is None:
            times = Time.query.all()
        else:
            times = Time.query.filter_by(month=month).all()

        if airport is None:
            for t in times:
                relations = Relation_table.query.filter_by(carrierID = realCarrier.id, timeID = t.id).all()
                for r in relations:
                    statistics = Statistics.query.filter_by(relationID = r.id).first()
                    flights = Flights.query.filter_by(id = statistics.flightID).first()
                    
                    cancelled = cancelled + flights.getCancelled()
                    ontime = ontime + flights.getOnTime()
                    delayed = delayed + flights.getDelayed()
                    diverted = diverted + flights.getDiverted()
                    total = total + flights.getTotal()
        else:
            for t in times:
                relation = Relation_table.query.filter_by(airportID = airport.id, carrierID = realCarrier.id, timeID = t.id).first()
                if relation is not None:
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
        
        if month is None:
            return {"month": "all", "flights-data": dict}
        return {"month": Time.getMonthText(month), "flights-data": dict}

    def getMinutesByMonth(realCarrier, month, airport = None):
        if month is not None and month == "None":
            month = None

        lateAircraft = 0
        carrier = 0
        security = 0
        weather = 0
        nationalAviationSystem = 0
        total = 0

        if month is None:
            times = Time.query.all()
        else:
            times = Time.query.filter_by(month=month).all()
        
        if airport is None:
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
            for t in times:
                #print(str(airport.id) + "  " + str(carrier.id) + "  ")
                relation = Relation_table.query.filter_by(airportID = airport.id, carrierID = realCarrier.id, timeID = t.id).first()
                if relation is not None:
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
        if month is None:
            return {"month" : "all", "minutes-data" : dict}
        return {"month" : Time.getMonthText(month), "minutes-data" : dict}
        
    def getAmountByMonth(realCarrier, month, airport = None):
        if month is not None and month == "None":
            month = None
        lateAircraft = 0
        carrier = 0
        security = 0
        weather = 0
        nationalAviationSystem = 0

        if month is None:
            times = Time.query.all()
        else:
            times = Time.query.filter_by(month=month).all()

        if airport is None:
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
            for t in times:
                #print(str(airport.id) + "  " + str(carrier.id) + "  ")
                relation = Relation_table.query.filter_by(airportID = airport.id, carrierID = realCarrier.id, timeID = t.id).first()
                if relation is not None:
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
            "nas" : nationalAviationSystem
        }
        if month is None:
            return {"month" : "all", "amount-data" : dict}
        return {"month" : Time.getMonthText(month), "amount-data" : dict}
        
        
    def getMean(airport1, airport2, realCarrier, month):
        if month == "None":
            month = None
    
        lateAircraft = 0
        carrier = 0
        security = 0
        weather = 0
        nationalAviationSystem = 0
        total = 0
        i = 0

        if month is None:
            times = Time.query.all()
        else:
            times = Time.query.filter_by(month = month).all()

        for t in times:
            #print(str(airport.id) + "  " + str(carrier.id) + "  ")
            relation1 = Relation_table.query.filter_by(airportID = airport1.id, carrierID = realCarrier.id, timeID = t.id).first()
            relation2 = Relation_table.query.filter_by(airportID = airport2.id, carrierID = realCarrier.id, timeID = t.id).first()
            if relation1 is not None and relation2 is not None:
                statistics1 = Statistics.query.filter_by(relationID = relation1.id).first()
                statistics2 = Statistics.query.filter_by(relationID = relation2.id).first()
                delay1 = Delays.query.filter_by(id = statistics1.delayID).first()
                minutes1 = Delays_minutes.query.filter_by(id = delay1.getMinutesID()).first()
                delay2 = Delays.query.filter_by(id = statistics2.delayID).first()
                minutes2 = Delays_minutes.query.filter_by(id = delay2.getMinutesID()).first()
                
                lateAircraft = lateAircraft + minutes1.getLateAircraft() + minutes2.getLateAircraft()
                carrier = carrier + minutes1.getCarrier() + minutes2.getCarrier()
                security = security + minutes1.getSecurity() + minutes2.getSecurity()
                weather = weather + minutes1.getWeather() + minutes2.getWeather()
                nationalAviationSystem = nationalAviationSystem + minutes1.getNationalAviationSystem() + minutes2.getNationalAviationSystem()
                total = total + minutes1.getTotal() + minutes2.getTotal()
                i = i + 2
        dict = {}
        if i == 0:
            dict = {
                "late-aircraft" : 0,
                "carrier" : 0,
                "security" : 0,
                "weather" : 0,
                "nas" : 0,
                "total": 0
            }
        else:    
            dict = {
                "late-aircraft" : lateAircraft/i,
                "carrier" : carrier/i,
                "security" : security/i,
                "weather" : weather/i,
                "nas" : nationalAviationSystem/i,
                "total": total/i
            }
        if month is None:
            return {"month" : "all", "minutes-data-mean" : dict}
        return {"month" : Time.getMonthText(month), "minutes-data-mean" : dict}
        
    def getStandardDeviation(airport1, airport2, realCarrier, month, meanDictionary):
        if month == "None":
            month = None
        if meanDictionary == "None":
            return None

        meanDictionary = meanDictionary["minutes-data-mean"]    
        print(meanDictionary)
        lateAircraft = 0
        carrier = 0
        security = 0
        weather = 0
        nationalAviationSystem = 0
        total = 0
        i = 0

        if month is None:
            times = Time.query.all()
        else:
            times = Time.query.filter_by(month = month).all()

        for t in times:
            #print(str(airport.id) + "  " + str(carrier.id) + "  ")
            relation1 = Relation_table.query.filter_by(airportID = airport1.id, carrierID = realCarrier.id, timeID = t.id).first()
            relation2 = Relation_table.query.filter_by(airportID = airport2.id, carrierID = realCarrier.id, timeID = t.id).first()
            if relation1 is not None and relation2 is not None:
                statistics1 = Statistics.query.filter_by(relationID = relation1.id).first()
                statistics2 = Statistics.query.filter_by(relationID = relation2.id).first()
                delay1 = Delays.query.filter_by(id = statistics1.delayID).first()
                minutes1 = Delays_minutes.query.filter_by(id = delay1.getMinutesID()).first()
                delay2 = Delays.query.filter_by(id = statistics2.delayID).first()
                minutes2 = Delays_minutes.query.filter_by(id = delay2.getMinutesID()).first()

                lateAircraft = lateAircraft + pow(minutes1.getLateAircraft() - meanDictionary["late-aircraft"], 2) 
                lateAircraft = lateAircraft + pow(minutes2.getLateAircraft() - meanDictionary["late-aircraft"], 2) 
                carrier = carrier + pow(minutes1.getCarrier() - meanDictionary["carrier"], 2)
                carrier = carrier + pow(minutes2.getCarrier() - meanDictionary["carrier"], 2)
                security = security + pow(minutes1.getSecurity() - meanDictionary["security"], 2)
                security = security + pow(minutes2.getSecurity() - meanDictionary["security"], 2)
                weather = weather + pow(minutes1.getWeather() - meanDictionary["weather"], 2)
                weather = weather + pow(minutes2.getWeather() - meanDictionary["weather"], 2)
                nationalAviationSystem = nationalAviationSystem + pow(minutes1.getNationalAviationSystem()- meanDictionary["nas"], 2)
                nationalAviationSystem = nationalAviationSystem + pow(minutes2.getNationalAviationSystem()- meanDictionary["nas"], 2)

                total = total + pow(minutes1.getTotal()-meanDictionary["total"], 2)
                total = total + pow(minutes2.getTotal()-meanDictionary["total"], 2)
                i = i + 2
        
        dict = {}
        if i == 0:
            dict = {
                "late-aircraft" : 0,
                "carrier" : 0,
                "security" : 0,
                "weather" : 0,
                "nas" : 0,
                "total": 0
            }
        else:
            dict = {
                "late-aircraft" : math.sqrt(lateAircraft/i),
                "carrier" : math.sqrt(carrier/i),
                "security" :  math.sqrt(security/i),
                "weather" :  math.sqrt(weather/i),
                "nas" :  math.sqrt(nationalAviationSystem/i),
                "total":  math.sqrt(total/i)
            }
        if month is None:
            return {"month" : "all", "flights-data-standard-deviation" : dict}
        return {"month" : Time.getMonthText(month), "standard-data" : dict}
