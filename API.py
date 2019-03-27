import csv
import json
import flask
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

## INIT and UPDATE core objects
from __init__ import app, db
from utility import Utility
from CSVHandler import CSVHandler
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



 
 


@app.route("/airports", methods=["GET"])  
@app.route("/airports/<code>", methods=["GET"])  
def getAirport(code = None):
    """
        Takes: airport code (str)
        Query variables: content-type (str)
        Returns:  (airportName (str), airportURI (str)) or list(airportName (str), airportURI (str))
    """
    
    ## Load args ##
    month = request.args.get("month")
    contentType = request.args.get("content-type")
    airportCode = request.args.get("airport-code")
    if(contentType == "None" or contentType is None):
        contentType = "application/json"
    queryString =  "?content-type=" + str(contentType) + "&month=" + str(month) 
    ###############
    
    ## Logic     ##
    if(code is None):
        # return all airport URIs + airport names.
        allAirports = Airport.query.all()
        dataList = []
        for a in allAirports:
            dict = {
                "name" : a.getName(),
                "uri" : "/airports/" + a.getCode() + queryString
            }
            dataList.append(dict)
            
        
    else:
        # return all carrier URIs with airport + airport name
        airport = Airport.query.filter_by(code = code).first()
        if(not (airport is None)):
            queryString =  "?airport-code=" + str(airport.getCode()) + "&content-type=" + str(contentType) + "&month=" + str(month) 
            relations = Relation_table.query.filter_by(airportID = airport.id)
            dataList = []

            for r in relations:
                carriers = Carrier.query.filter_by(id = r.getCarrierID())
                for c in carriers:
                    uri = "/carriers/" + c.getCode() + queryString
                    name = c.getName()
                    dict = {
                        "uri" : uri,
                        "carrier-name" : name,
                        "carrier-code" : c.getCode()
                    }
                    if(not dict in dataList):
                        dataList.append(dict)
                    
            dict = {
                "name" : airport.getName(),
                "uri-list" : dataList
                
            }
            
        else:
            flask.abort(400, "400(invalid paramater): airport code invalid")

    if(contentType == "text/csv"):
        if(code is None):
            return CSVHandler.getAirportCSV(dataList = dataList)
        else:
            return CSVHandler.getAirportCSV(dictionary = dict)
       
    else:
        if(code is None):
            return json.dumps(dataList)
        else:
            return json.dumps(dict)
            
            

@app.route("/carriers", methods=["GET"])  
@app.route("/carriers/<code>", methods=["GET"])  
def getCarrier(code = None):
    """
        Takes: carrier code (str)
        Query variables: airport-code (str), content-type (str)
        Returns:  (carrierName (str), statisticsURI (str)) or list(carrierName (str), carrierURI (str))
    """
    
    ## Load args ##
    month = request.args.get("month")
    contentType = request.args.get("content-type")
    airportCode = request.args.get("airport-code")
    if(contentType == "None" or contentType is None):
        contentType = "application/json"
    queryString =  "?airport-code=" + str(airportCode) + "&content-type=" + str(contentType) + "&month=" + str(month)  
    ###############
    
    ## Logic     ##
    if(code is None):
        # return all carrier URIs + carrier names.
        dataList = []
        if(airportCode is None):
            allCarriers = Carrier.query.all()
   
            for c in allCarriers:
                dict = {
                    "name" : c.getName(),
                    "uri" : "/carriers/" + c.getCode()+"?content-type="+str(contentType),
                    "code" : c.getCode()
                }
                dataList.append(dict)
        else:
            airport = Airport.query.filter_by(code = airportCode).first()
            if(airport is None):
                flask.abort(400, "400(invalid parameter): airport code invalid")
            else:
                relations = Relation_table.query.filter_by(airportID = airport.id).all()
                for r in relations:
                    carrier = Carrier.query.filter_by(id = r.getCarrierID()).first()
                    dict = {
                        "name" : carrier.getName(),
                        "uri" : "/carriers/"+carrier.getCode()+queryString,
                        "code" : carrier.getCode()
                        
                    }
                    if(not (dict in dataList)):
                        dataList.append(dict)
                
      
        
    else:
        # return specific statistics URI + carrier name.
        carrier = Carrier.query.filter_by(code=code).first()
        if(not (carrier is None)):
            relations = Relation_table.query.filter_by(carrierID = carrier.id).all()
            airportURIs = []
            for r in relations:
                airport = Airport.query.filter_by(id = r.getAirportID()).first()
                queryString2 =  "?content-type=" + str(contentType) + "&month=" + str(month)  
                uri = "/airports/" + str(airport.getCode()) + queryString2
                if(not uri in airportURIs):
                    airportURIs.append(uri)
                
            dict = {
                "name" : carrier.getName(),
                
                "statistics-uri" : "/carriers/" + carrier.getCode() + "/statistics"+queryString,
                "airport-uris" : airportURIs
            }
            
        else:
            flask.abort(400, "400(invalid paramater): carrier code invalid")  

    if(contentType == "text/csv"):
        if(code is None):
            return CSVHandler.getCarrierCSV(dataList = dataList)
        else:
            return CSVHandler.getCarrierCSV(dictionary = dict)
       
    else:
        if(code is None):
            return json.dumps(dataList)
        else:
            return json.dumps(dict)
 
 
@app.route("/carriers/<code>/statistics", methods=["GET"])
def getStatistics(code = None):
    """
        Takes: carrier code (str)
        Query variables: month (str), content-type (str), airportCode (str)
        Returns:  flights-uri, minutes-uri, amount-uri
    """
    
    ## Load args ##
    month = request.args.get("month")
    contentType = request.args.get("content-type")
    airportCode = request.args.get("airport-code")
    if(contentType == "None" or contentType is None):
        contentType = "application/json"
        
    print(str(month))    
    queryString =  "?airport-code=" + str(airportCode) + "&content-type=" + str(contentType) + "&month=" + str(month) 
    ###############
    
    
    ## Logic     ##
    if(code is None):
        flask.abort(400, "400(invalid paramater): carrier code invalid(None)")
    else:
        carrier = Carrier.query.filter_by(code = code).first()
        if(carrier is None):
            flask.abort(400, "400(invalid paramater): carrier code invalid")
        else:
            if(airportCode is None):
                dict = {
                    "flights-uri" : "/carriers/"+code+"/statistics/flights" + queryString,
                    "minutes-uri" : "/carriers/"+code+"/statistics/delays/minutes" + queryString,
                    "amount-uri" : "/carriers/"+code+"/statistics/delays/amount" + queryString
                }
                
            else:
                ## Same as above
                dict = {
                    "flights-uri" : "/carriers/"+code+"/statistics/flights" + queryString,
                    "minutes-uri" : "/carriers/"+code+"/statistics/delays/minutes" + queryString,
                    "amount-uri" : "/carriers/"+code+"/statistics/delays/amount" + queryString    
                }
    if(contentType == "text/csv"):
        return CSVHandler.getStatisticsCSV(dictionary = dict)
       
    else: 
        return json.dumps(dict)            

@app.route("/carriers/<code>/statistics", methods=["PUT"])
def setStatistics(code = None):

    """
        Takes: carrier code(str)
        form variables: (minutes-late-aircraft, minutes-late-carrier, minutes-late-security, minutes-late-weather, minutes-late-nas, minutes-late-total) + (amount-late-aircraft, amount-late-carrier, amount-late-security, amount-late-weather, amount-late-nas) + (flights-cancelled, flights-on-time, flights-delayed, flights-diverted, flights-total)
        Query variables: month (int), airport-code (str), content-type (str), year (int)
        returns Success
    """
    
    minutesFlag = 1
    amountFlag = 1
    flightsFlag = 1
    ## Load form ##
    try:
        minutesLateAircraft = request.form['minutes-late-aircraft']
        minutesLateCarrier = request.form['minutes-late-carrier']
        minutesLateSecurity = request.form['minutes-late-security']
        minutesLateWeather = request.form['minutes-late-weather']
        minutesLateNAS  = request.form['minutes-late-nas']
        minutesLateTotal = request.form['minutes-late-total']
    except:
        minutesFlag = 0
        
    try:    
        amountLateAircraft = request.form['amount-late-aircraft'] 
        amountLateCarrier = request.form['amount-late-carrier']
        amountLateSecurity = request.form['amount-late-security']
        amountLateWeather = request.form['amount-late-weather']
        amountLateNAS = request.form['amount-late-nas']
    except:
        amountFlag = 0
        
    try:    
        flightsCancelled = request.form['flights-cancelled']
        flightsOnTime = request.form['flights-on-time']
        flightsDelayed = request.form['flights-delayed']
        flightsDiverted = request.form['flights-diverted']
        flightsTotal = request.form['flights-total']
    except:
        flightsFlag = 0
        
        
    ## Load args ##
    month = request.args.get("month")
    contentType = request.args.get("content-type")
    airportCode = request.args.get("airport-code")
    year = request.args.get("year")
    if(contentType == "None" or contentType is None):
        contentType = "application/json"

    
    
    airport = Airport.query.filter_by(code = airportCode).first()
    time = Time.query.filter_by(month = month, year = year).first()
    carrier = Carrier.query.filter_by(code = code).first()

    if(airport is None):
        flask.abort(400, "400(invalid paramater): airport code invalid")
    if(time is None):
        flask.abort(400, "400(invalid paramater): time is invalid")
    if(carrier is None):
        flask.abort(400, "400(invalid paramater): carrier code invalid")
    
    
    relation = Relation_table.query.filter_by(airportID = airport.id, carrierID = carrier.id, timeID = time.id).first()
    if(relation is None):
        flask.abort(400, "Something went wrong, no relation found with input values.")
    
    statistics = Statistics.query.filter_by(relationID = relation.id).first()
    flights = Flights.query.filter_by(id = statistics.getFlightID()).first()
    
    delays = Delays.query.filter_by(id = statistics.getDelayID()).first()
    minutes = Delays_minutes.query.filter_by(id = delays.getMinutesID()).first()
    amount = Delays_amount.query.filter_by(id = delays.getAmountID()).first()
    
    if(minutesFlag == 1):
        try:
            minutes.lateAircraft = minutesLateAircraft
            minutes.carrier = minutesLateCarrier
            minutes.security = minutesLateSecurity
            minutes.weather = minutesLateWeather
            minutes.nationalAviationSystem = minutesLateNAS
            minutes.total = minutesLateTotal
            db.session.commit()
        except:
            flask.abort(500, "Updating minutes failed")
    if(amountFlag == 1):
        try:
            amount.lateAircraft = amountLateAircraft
            amount.carrier = amountLateCarrier
            amount.security = amountLateSecurity
            amount.weather = amountLateWeather
            amount.nationalAviationSystem = amountLateNAS
            db.session.commit()
        except:
            flask.abort(500, "Updating amount failed")
    if(flightsFlag == 1):
        try:
            flights.cancelled = flightsCancelled
            flights.onTIme = flightsOnTime
            flights.delayed = flightsDelayed
            flights.diverted = flightsDiverted
            flights.total = flightsTotal
            db.session.commit()
        except:
            flask.abort(500, "Updating flights failed")
    return "success"
    
    
@app.route("/carriers/<code>/statistics", methods=["POST"])
def addStatistics(code = None):

    """
        Takes: carrier code(str)
        form variables: (minutes-late-aircraft, minutes-late-carrier, minutes-late-security, minutes-late-weather, minutes-late-nas, minutes-late-total) + (amount-late-aircraft, amount-late-carrier, amount-late-security, amount-late-weather, amount-late-nas) + (flights-cancelled, flights-on-time, flights-delayed, flights-diverted, flights-total)
        Query variables: month (int), airport-code (str), content-type (str), year (int)
        returns: Success
    """
    
    minutesFlag = 1
    amountFlag = 1
    flightsFlag = 1
    ## Load form ##
    try:
        minutesLateAircraft = request.form['minutes-late-aircraft']
        minutesLateCarrier = request.form['minutes-late-carrier']
        minutesLateSecurity = request.form['minutes-late-security']
        minutesLateWeather = request.form['minutes-late-weather']
        minutesLateNAS  = request.form['minutes-late-nas']
        minutesLateTotal = request.form['minutes-late-total']
    except:
        minutesFlag = 0
        
    try:    
        amountLateAircraft = request.form['amount-late-aircraft'] 
        amountLateCarrier = request.form['amount-late-carrier']
        amountLateSecurity = request.form['amount-late-security']
        amountLateWeather = request.form['amount-late-weather']
        amountLateNAS = request.form['amount-late-nas']
    except:
        amountFlag = 0
        
    try:    
        flightsCancelled = request.form['flights-cancelled']
        flightsOnTime = request.form['flights-on-time']
        flightsDelayed = request.form['flights-delayed']
        flightsDiverted = request.form['flights-diverted']
        flightsTotal = request.form['flights-total']
    except:
        flightsFlag = 0
        
        
    ## Load args ##
    month = request.args.get("month")
    contentType = request.args.get("content-type")
    airportCode = request.args.get("airport-code")
    year = request.args.get("year")
    if(contentType == "None" or contentType is None):
        contentType = "application/json"

    
    
    airport = Airport.query.filter_by(code = airportCode).first()
    time = Time.query.filter_by(month = month, year = year).first()
    carrier = Carrier.query.filter_by(code = code).first()

    if(airport is None):
        flask.abort(400, "400(invalid paramater): airport code invalid")
    if(time is None):
        flask.abort(400, "400(invalid paramater): time is invalid")
    if(carrier is None):
        flask.abort(400, "400(invalid paramater): carrier code invalid")
    
    oldRelation = Relation_table.query.filter_by(airportID = airport.id, carrierID = carrier.id, timeID = time.id).first()
    if(not oldRelation is None):
        flask.abort(400, "Relation already exists")
        
    relation = Relation_table(aID = airport.id, cID = carrier.id, tID = time.id)
    
    minutes = Delays_minutes(la = minutesLateAircraft, c = minutesLateCarrier, s = minutesLateSecurity, w = minutesLateWeather, t = minutesLateTotal)
    amount = Delays_amount(la = amountLateAircraft, c = amountLateCarrier, s = amountLateSecurity, w = amountLateWeather)
    flights = Flights(cancel = flightsCancelled, onTime = flightsOnTime, delay = flightsDelayed, divert = flightsDiverted, t = flightsTotal)
    
    
    db.session.add(minutes)
    db.session.add(amount)
    db.session.add(flights)
    db.session.add(relation)
    
    db.session.commit()
    
    
    
    delays = Delays(mID = minutes.id, aID = amount.id)
    statistics = Statistics(rID = relation.id, fID = flights.id, dID = delays.id )
    
    db.session.add(delays)
    db.sessions.add(statistics)
    

    return "success" 
    
@app.route("/carriers/<code>/statistics", methods=["DELETE"])
def removeStatistics(code = None):
    """
        Takes: carrier code (str)
        Query variables: month (int), content-type (str), airport-code (str), year (int)
        returns: Success
    """
    ## Take Args ##    
    month = request.args.get("month")
    contentType = request.args.get("content-type")
    airportCode = request.args.get("airport-code")
    year = request.args.get("year")
    if(contentType == "None" or contentType is None):
        contentType = "application/json"
        
     
    airport = Airport.query.filter_by(code = airportCode).first()
    time = Time.query.filter_by(month = month, year = year).first()
    carrier = Carrier.query.filter_by(code = code).first()

    if(airport is None):
        flask.abort(400, "400(invalid paramater): airport code invalid")
    if(time is None):
        flask.abort(400, "400(invalid paramater): time is invalid")
    if(carrier is None):
        flask.abort(400, "400(invalid paramater): carrier code invalid")
    
    
    relation = Relation_table.query.filter_by(airportID = airport.id, carrierID = carrier.id, timeID = time.id).first()   
    if(relation is None):
        flask.abort(400, "Something went wrong, no relation found with input values.")
    
    statistics = Statistics.query.filter_by(relationID = relation.id).first()
    flights = Flights.query.filter_by(id = statistics.getFlightID()).first()
    
    delays = Delays.query.filter_by(id = statistics.getDelayID()).first()
    minutes = Delays_minutes.query.filter_by(id = delays.getMinutesID()).first()
    amount = Delays_amount.query.filter_by(id = delays.getAmountID()).first()
    
    
    db.session.delete(statistics)
    db.session.delete(flights)
    db.session.delete(relation)
    db.session.delete(delays)
    db.session.delete(minutes)
    db.session.delete(amount)
    
    return "success"
    

@app.route("/carriers/<code>/statistics/flights", methods=["GET"])  
def getFlights(code = None):
    """
        Takes: carrier code (str)
        Query variables: month (str), content-type (str)
        Returns:  Dictionary of flights + month + carrier URI
    """
    
    ## Load args ##
    month = request.args.get("month")
    contentType = request.args.get("content-type")
    airportCode = request.args.get("airport-code")
    if(contentType == "None" or contentType is None):
        contentType = "application/json"
    queryString =  "?airport-code=" + str(airportCode) + "&content-type=" + str(contentType) + "&month=" + str(month) 
    
    ## Logic     ##
    if(code is None):
        flask.abort(400, "400(invalid paramater): airport code invalid")
    else:
        if(airportCode is None):
           
            carrier = Carrier.query.filter_by(code = code).first()
            if(carrier is None):
                flask.abort(400, "400(invalid paramter): carrier code invalid")
            dictionary = Utility.getFlightsByMonth(realCarrier = carrier, month = month)
            dictionary["carrier-uri"] = "/carriers/"+code+queryString
            
        else:
   
            carrier = Carrier.query.filter_by(code = code).first()
            airport = Airport.query.filter_by(code = airportCode).first()
            if(carrier is None or airport is None):
                flask.abort(400, "400(invalid paramater): airport/carrier code invalid")
            dictionary = Utility.getFlightsByMonth(realCarrier = carrier, airport = airport, month = month)
            dictionary["carrier-uri"] = "/carriers/"+code+queryString
           
                
    if(contentType == "text/csv"):
        return CSVHandler.getFlightsCSV(dictionary)
    else:
        return json.dumps(dictionary)
        


    
@app.route("/carriers/<code>/statistics/delays/minutes", methods=["GET"])  
def getMinutes(code = None):
    """
        Takes: carrier code (str)
        Query variables: month (str), content-type (str), delay (str)
        Returns:  Dictionary of minutes + month + carrier URI.
    """
    
    ## Load args ##
    month = request.args.get("month")
    contentType = request.args.get("content-type")
    airportCode = request.args.get("airport-code")
    if(contentType == "None" or contentType is None):
        contentType = "application/json"
    queryString =  "?airport-code=" + str(airportCode) + "&content-type=" + str(contentType) + "&month="  + str(month) 
    
    # Extra args functionality
    delayType = request.args.get("delay")
    if(airportCode == "None"):
        airportCode = None
    ###############
    
     ## Logic     ##
    if(code is None):
        flask.abort(400, "400(invalid paramater): carrier code invalid")
    else:
        if(airportCode is None):
                carrier = Carrier.query.filter_by(code = code).first()
                
                if(carrier is None):
                    flask.abort(400, "400(invalid paramter): carrier code invalid")
                dictionary = Utility.getMinutesByMonth(realCarrier= carrier, month = month)
                dictionary["carrier-uri"] = "/carriers/"+code+queryString
                
        else:
                carrier = Carrier.query.filter_by(code = code).first()
                airport = Airport.query.filter_by(code = airportCode).first()
                if(carrier is None or airport is None):
                    flask.abort(400, "400(invalid paramater): airport/carrier code invalid")
                dictionary = Utility.getMinutesByMonth(realCarrier = carrier, airport = airport, month = month)
                dictionary["carrier-uri"] = "/carriers/"+code+queryString
                
                
    if(contentType == "text/csv"):
        return CSVHandler.getMinutesCSV(dictionary)
    else:
        return json.dumps(dictionary)
        
        
@app.route("/carriers/<code>/statistics/delays/minutes/averages", methods=["GET"])  
def getMinutesAverage(code = None):
    """
        Takes: carrier code (str)
        Query variables: month (str), content-type (str), delay (str), airport-code1 (str), airportcode2 (str)
        Returns:  ?
    """
    
    ## Load args ##
    month = request.args.get("month")
    contentType = request.args.get("content-type")
    delayType = request.args.get("delay")
    airportCode1 = request.args.get("airport-code1")
    airportCode2 = request.args.get("airport-code2")
    
    if(contentType == "None" or contentType is None):
        contentType = "application/json"
    queryString =  "?airport-code1=" + str(airportCode1) + "&content-type=" + str(contentType) + "&month="  + str(month) 
    ###############
    
    ## Logic     ##
    carrier = Carrier.query.filter_by(code = code).first()
    airport1 = Airport.query.filter_by(code = airportCode1).first()
    airport2 = Airport.query.filter_by(code = airportCode2).first()
    if(carrier is None or airport1 is None or airport2 is None):
        flask.abort(400)
    
    dict = Utility.getMean(airport1, airport2, carrier, month)
    if(dict == "None"):
        return flask.abort(400, "empty dictionary return for mean")
    standardDeviationDictionary = Utility.getStandardDeviation(airport1, airport2, carrier, month, dict)
    
    finalDictionary = {
        "mean" : dict,
        "standard-deviation" : standardDeviationDictionary,
        "carrier-uri" : "/carriers/"+code+queryString
    
    
    }
    
    return json.dumps(finalDictionary) 
        
    
@app.route("/carriers/<code>/statistics/delays/amount", methods=["GET"])  
def getAmount(code = None):
    """
        Takes: carrier code (str)
        Query variables: month (str), content-type (str), delay (str)
        Returns:  Dictionary of amount + month + carrier uri
    """
    
    ## Load args ##
    month = request.args.get("month")
    contentType = request.args.get("content-type")
    airportCode = request.args.get("airport-code")
    if(contentType == "None" or contentType is None):
        contentType = "application/json"
    queryString =  "?airport-code=" + str(airportCode) + "&content-type=" + str(contentType) + "&month="  + str(month) 
    
    # Extra args functionality
    delayType = request.args.get("delay")
    if(airportCode == "None"):
        airportCode = None
    ###############

    ## Logic     ##
    if(code is None):
        flask.abort(400, "400(invalid paramater): carrier code invalid")
    else:
        if(airportCode is None):
                carrier = Carrier.query.filter_by(code = code).first()
                
                if(carrier is None):
                    flask.abort(400, "400(invalid paramter): carrier code invalid")
                dictionary = Utility.getAmountByMonth(realCarrier = carrier, month = month)
                dictionary["carrier-uri"] = "/carriers/"+code+queryString
                #return json.dumps(dictionary)
        else:
                carrier = Carrier.query.filter_by(code = code).first()
                airport = Airport.query.filter_by(code = airportCode).first()
                if(carrier is None or airport is None):
                    flask.abort(400, "400(invalid paramater): airport/carrier code invalid")
                dictionary = Utility.getAmountByMonth(realCarrier = carrier, airport = airport, month = month)
                dictionary["carrier-uri"] = "/carriers/"+code+queryString
                #return json.dumps(dictionary)
                
    if(contentType == "text/csv"):
        return CSVHandler.getAmountCSV(dictionary)
    else:
        return json.dumps(dictionary)
    




