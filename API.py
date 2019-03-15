import csv
import json
import flask
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

## INIT and UPDATE core objects
from __init__ import app, db
from utility import Utility
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
    contentType = request.args.get("content-type")
    if(contentType == "None" or contentType is None):
        contentType = "application/json"
    ###############
    
    ## Logic     ##
    if(code is None):
        # return all airport URIs + airport names.
        allAirports = Airport.query.all()
        dataList = []
        for a in allAirports:
            dict = {
                "name" : a.getName(),
                "uri" : "/airports/" + a.getCode()
            }
            dataList.append(dict)
        return json.dumps(dataList)
    else:
        # return all carrier URIs with airport + airport name
        airport = Airport.query.filter_by(code = code).first()
        if(not (airport is None)):
            relations = Relation_table.query.filter_by(airportID = airport.id)
            dataList = []

            for r in relations:
                carriers = Carrier.query.filter_by(id = r.getCarrierID())
                for c in carriers:
                    dataList.append("/carriers/" + c.getCode() + "?airport-code=" + code + "&content-type=" + str(contentType))
                    
            dict = {
                "name" : airport.getName(),
                "uri-list" : dataList
            }
            return json.dumps(dict)
        else:
            flask.abort(400, "400(invalid paramater): airport code invalid")

 

 
  ############################# returning wrong
@app.route("/carriers", methods=["GET"])  
@app.route("/carriers/<code>", methods=["GET"])  
def getCarrier(code = None):
    """
        Takes: carrier code (str)
        Query variables: airport-code (str), content-type (str)
        Returns:  (carrierName (str), statisticsURI (str)) or list(carrierName (str), carrierURI (str))
    """
    
    ## Load args ##
    airportCode = request.args.get("airport-code")
    contentType = request.args.get("content-type")
    if(contentType == "None" or contentType is None):
        contentType = "application/json"
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
                    "uri" : "/carriers/" + c.getCode()+"?content-type="+str(contentType)
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
                        "uri" : "/carriers/"+carrier.getCode()+"?content-type="+str(contentType)+"&airport-code="+airportCode
                    }
                    if(not (dict in dataList)):
                        dataList.append(dict)
                
      
        return json.dumps(dataList)
    else:
        # return specific statistics URI + carrier name.
        carrier = Carrier.query.filter_by(code=code).first()
        if(not (carrier is None)):
            dict = {
                "name" : carrier.getName(),
                "uri" : "/carriers/" + carrier.getCode() + "/statistics"+"?content-type="+str(contentType)+"&airport-code="+str(airportCode)
            }
            return json.dumps(dict)
        else:
            flask.abort(400, "400(invalid paramater): carrier code invalid")  

 
 
@app.route("/carriers/<code>/statistics", methods=["GET"])
def getStatistics(code = None):
    """
        Takes: carrier code (str)
        Query variables: month (str), content-type (str)
        Returns:  ?
    """
    
    ## Load args ##
    month = request.args.get("month")
    contentType = request.args.get("content-type")
    airportCode = request.args.get("airport-code")
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
                    "flights-uri" : "/carriers/"+code+"/statistics/flights?month="+str(month)+"&content-type="+str(contentType),
                    "minutes-uri" : "/carriers/"+code+"/statistics/delays/minutes?month="+str(month)+"&content-type="+str(contentType),
                    "amount-uri" : "/carriers/"+code+"/statistics/delays/amount?month="+str(month)+"&content-type="+str(contentType)
                }
                return json.dumps(dict)
            else:
                ## Same as above
                dict = {
                    "flights-uri" : "/carriers/"+code+"/statistics/flights?month="+str(month)+"&airport-code="+airportCode+"&content-type="+str(contentType),
                    "minutes-uri" : "/carriers/"+code+"/statistics/delays/minutes?month="+str(month)+"&airport-code="+airportCode+"&content-type="+str(contentType),
                    "amount-uri" : "/carriers/"+code+"/statistics/delays/amount?month="+str(month)+"&airport-code="+airportCode+"&content-type="+str(contentType)      
                }
                return json.dumps(dict)

    
    
@app.route("/carriers/<code>/statistics/flights", methods=["GET"])  
def getFlights(code = None):
    """
        Takes: carrier code (str)
        Query variables: month (str), content-type (str)
        Returns:  ?
    """
    
    ## Load args ##
    month = request.args.get("month")
    contentType = request.args.get("content-type")
    airportCode = request.args.get("airport-code")
    
    ## Logic     ##
    if(code is None):
        flask.abort(400, "400(invalid paramater): airport code invalid")
    else:
        if(airportCode is None):
           
            carrier = Carrier.query.filter_by(code = code).first()
            if(carrier is None):
                flask.abort(400, "400(invalid paramter): carrier code invalid")
            dictionary = Utility.getFlightsByMonth(carrier = carrier, month = month)
            return json.dumps(dictionary)
        else:
   
            carrier = Carrier.query.filter_by(code = code).first()
            airport = Airport.query.filter_by(code = airportCode).first()
            if(carrier is None or airport is None):
                flask.abort(400, "400(invalid paramater): airport/carrier code invalid")
            dictionary = Utility.getFlightsByMonth(carrier = carrier, airport = airport, month = month)
            return json.dumps(dictionary)



    
@app.route("/carriers/<code>/statistics/delays/minutes", methods=["GET"])  
def getMinutes(code = None):
    """
        Takes: carrier code (str)
        Query variables: month (str), content-type (str), delay (str)
        Returns:  ?
    """
    
    ## Load args ##
    month = request.args.get("month")
    contentType = request.args.get("content-type")
    delayType = request.args.get("delay")
    airportCode = request.args.get("airport-code")
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
                dictionary = Utility.getMinutesByMonth(carrier = carrier, month = month)
                return json.dumps(dictionary)
        else:
                carrier = Carrier.query.filter_by(code = code).first()
                airport = Airport.query.filter_by(code = airportCode).first()
                if(carrier is None or airport is None):
                    flask.abort(400, "400(invalid paramater): airport/carrier code invalid")
                dictionary = Utility.getMinutesByMonth(carrier = carrier, airport = airport, month = month)
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
    ###############
    
    ## Logic     ##
    return "to be implemented" 
        
    
@app.route("/carriers/<code>/statistics/delays/amount", methods=["GET"])  
def getAmount(code = None):
    """
        Takes: carrier code (str)
        Query variables: month (str), content-type (str), delay (str)
        Returns:  ?
    """
    
    ## Load args ##
    month = request.args.get("month")
    contentType = request.args.get("content-type")
    delayType = request.args.get("delay")
    airportCode = request.args.get("airport-code") 
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
                dictionary = Utility.getAmountByMonth(carrier = carrier, month = month)
                return json.dumps(dictionary)
        else:
                carrier = Carrier.query.filter_by(code = code).first()
                airport = Airport.query.filter_by(code = airportCode).first()
                if(carrier is None or airport is None):
                    flask.abort(400, "400(invalid paramater): airport/carrier code invalid")
                dictionary = Utility.getAmountByMonth(carrier = carrier, airport = airport, month = month)
                return json.dumps(dictionary)
                
    
    




