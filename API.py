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





#airports = Airport.query.all()
#for a in airports:
#    print(str(a.id) + "  |  " + a.getName() + "  |  " + a.getCode())



#carriers = Carrier.query.all()
#for c in carriers:
#    db.session.delete(a);
#    print(str(c.id) + "  |  " + c.getName() + "  |  " + c.getCode())
#
#times = Time.query.all()
#for t in times:
#    print(t.getLabel(t.getId()))
   

#relations = Relation_table.query.all()
#j = 0
#for r in relations:
#    j = j + 1
#    if(j > 100):
#        break;
#    print(str(r.getAirportID()) + " -- " + str(r.getCarrierID()) + " -- " + str(r.getTimeID()))

        
#print("statistics")
#statistics = Statistics.query.all()
#for s in statistics:
 #   print(str(s.relationID) + " -- " + str(s.flightID) + " -- " + str(s.delayID))

 
 
 
 
 
 
 
 
 
 
 
  
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
            return "Code 400"

 

 
  
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
    ###############
    
    ## Logic     ##
    if(code is None):
        # return all carrier URIs + carrier names.
        allCarriers = Carrier.query.all()
        dataList = []
        for c in allCarriers:
            dict = {
                "name" : c.getName(),
                "uri" : "/carriers/" + c.getCode()
            }
            dataList.append(dict)
        return json.dumps(dataList)
    else:
        # return specific statistics URI + carrier name.
        carrier = Carrier.query.filter_by(code=code).first()
        if(not (carrier is None)):
            dict = {
                "name" : carrier.getName(),
                "uri" : "/carriers/" + carrier.getCode() + "/statistics"
            }
            return json.dumps(dict)
        else:
            return "Code 400"    

 
 
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
        return "Code 400"
    else:
        carrier = Carrier.query.filter_by(code = code).first()
        if(carrier is None):
            return "Code 400"
        else:
            if(airportCode is None):
                ## carrier -> relation -> statistics -> flights/(delays->minutes)/(delays->amount)
                ## we will do this in a utility package (not in the main api.py)
                return "sum of {{flights}, {minutes}, {amount}}"
            else:
                ## Same as above
                return "{flights}, {minutes}, {amount}}"
    return "to be implemented"
    
    
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
    
    
    ## Logic     ##
    return "to be implemented" 

    
@app.route("/carriers/<code>/delays/minutes", methods=["GET"])  
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
    ###############
    
    ## Logic     ##
    return "to be implemented" 
    
@app.route("/carriers/<code>/delays/minutes/averages", methods=["GET"])  
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
        
    
@app.route("/carriers/<code>/delays/amount", methods=["GET"])  
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
    ###############

    ## Logic     ##
    return "to be implemented"     
    
    
    
    
app.run(port='5002', ssl_context='adhoc')  



