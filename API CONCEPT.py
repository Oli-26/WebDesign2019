import csv
import json
import flask
from flask import Flask, request, jsonify
from flask_restful import Resource, Api


app = Flask(__name__)
jsondir = "airlines.json"


def replaceUnderscores(original):
    if(original == None):
        return None
    newString = original.replace("_", " ")
    return newString

@app.route("/getairportnames", methods=["GET"]) 
def getAirportNames(type = None):
    """
        Returns all airports in a jsonified list.
        Definite Args: None
        Optional Args: type
    """
    type = request.args.get("type")
    nameList = list()
    if(type == "csv"):  
        with  open(airlines.csv) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if(not row[20] in nameList):
                    nameList.append(row[20])
         
    
    elif(type == "json" or type == None):
        with open(jsondir) as f:
            data = json.load(f)
            i = 0
            for index in data:
                if(not index["airport"]["name"] in nameList):
                    nameList.append(index["airport"]["name"])
    else:
        flask.abort(411)        
    return json.dumps(nameList)
  
@app.route("/getcarriernames", methods=["GET"])      
def getCarrierNames(type = None):
    """
        Returns all carrier names in a jsonified list.
        Definite Args: None
        Options Args: type
    """
    type = request.args.get("type")
    nameList = list()
    if(type == "csv"):
        flask.abort(410)
    elif(type == "json" or type == None):
        with open(jsondir) as f:
            data = json.load(f)
            i = 0
            for index in data:
                if(not index["carrier"]["name"] in nameList):
                    nameList.append(index["carrier"]["name"])
    else:
        flask.abort(411)
    return json.dumps(nameList)                

 
@app.route("/getcarriersatairport/<airport>", methods=["GET"])         
def getCarriersAtAirport(airport, type = None):
    """
        returns a list of all carriers at a specific airport.
        Definite args: airport
        optional args: type
    """
    type = request.args.get('type')
    airport = replaceUnderscores(airport)
    nameList = list()
    print("Searching for carriers at airport :" + airport)
    if(type == "csv"):
        flask.abort(410)
    elif(type == "json" or type == None):
        with open(jsondir) as f:
            data = json.load(f)
           
            for index in data:
                if( airport in index["airport"]["name"] and not index["carrier"]["name"] in nameList):
                    #print(index["carrier"]["name"])
                    nameList.append(index["carrier"]["name"])
    else:
        flask.abort(411)                
    return json.dumps(nameList)  
    
@app.route("/getinformation", methods=["GET"])    
def getInformation(carrier = None, month = None, type = None):
    """
        Returns canncled, on_time, delayed and diverted counts a (optional) carrier in a (optional) month.
        Definite args: None
        optional args: carrier, month, type
    """
    carrier = replaceUnderscores(request.args.get("carrier"))
    month = request.args.get("month")
    type = request.args.get("type")
    if(carrier != None):
        carrier = replaceUnderscores(carrier)
    cancelled = 0
    ontime = 0
    total = 0
    delayed = 0
    diverted = 0
    print("Searching flight details for:" + carrier)
    if(not month is None):
        print("For month:" + month)
    if(type == "csv"):
        flask.abort(410)
    elif(type == "json" or type == None):
        with open(jsondir) as f:
            data = json.load(f)
            if(month == None):
                for index in data:
                    if( carrier in index["carrier"]["name"]):
                        cancelled = cancelled + index["statistics"]["flights"]["cancelled"]
                        ontime = ontime + index["statistics"]["flights"]["on time"]
                        total = total + index["statistics"]["flights"]["total"]
                        delayed = delayed + index["statistics"]["flights"]["delayed"]
                        diverted = diverted + index["statistics"]["flights"]["diverted"]
            else:
                for index in data:
                    
                    if( carrier in index["carrier"]["name"] and index["time"]["month"] == int(month)):
                        cancelled = cancelled + index["statistics"]["flights"]["cancelled"]
                        ontime = ontime + index["statistics"]["flights"]["on time"]
                        total = total + index["statistics"]["flights"]["total"]
                        delayed = delayed + index["statistics"]["flights"]["delayed"]
                        diverted = diverted + index["statistics"]["flights"]["diverted"]
    else:
        flask.abort(411)
    dictionary = {
        'cancelled': cancelled,
        'on time': ontime,
        'delayed': delayed,
        'diverted': diverted
    }
        
    return jsonify(dictionary)
    
 
@app.route("/flightstatus/<airport>/<carrier>", methods=["GET"])           
def flightStatus(airport, carrier, month = None, type = None):
    """
        returns cancelled, on_time, and delayed counts for a specific carrier at a specific airport in (optionally) a specific month.
        Definite args: airport, carrier
        optional args: month, type
    """
    month = request.args.get("month")
    type = request.args.get("type")
    
    cancelled = 0
    ontime = 0
    delayed = 0
    if(type == "csv"):
        flask.abort(410)
    elif(type == "json" or type == None):
        with open(jsondir) as f:
            data = json.load(f)
           
            if(month == None):
                for index in data:
                    if(airport in index["airport"]["name"] and carrier in index["carrier"]["name"]):
                        cancelled = cancelled + index["statistics"]["flights"]["cancelled"]
                        ontime = ontime + index["statistics"]["flights"]["on time"]
                        delayed = delayed + index["statistics"]["flights"]["delayed"]
            else:
                print("month given!")
                for index in data:
                    if(airport in index["airport"]["name"] and carrier in index["carrier"]["name"] and str(index["time"]["month"]) == month):
                        cancelled = cancelled + index["statistics"]["flights"]["cancelled"]
                        ontime = ontime + index["statistics"]["flights"]["on time"]
                        delayed = delayed + index["statistics"]["flights"]["delayed"]
    else:
        flask.abort(411)
    dictionary = {
        'cancelled': cancelled,
        'on time': ontime,
        'delayed': delayed,
    }
        
    return jsonify(dictionary)
 
@app.route("/getminslate/<carrier>", methods=["GET"])      
def getMinsLate(carrier, reason = None, month = None, airport = None, type = None):
    """
        returns the number of minutes a specific carrier is late for (optionally) a specific reason, in (optionally) a specific month, in (optionally) a specific airport.
        Definite args: carrier
        optional args: reason, month, airport, type
    """
    reason = replaceUnderscores(request.args.get("reason"))
    month = request.args.get("month")
    airport = replaceUnderscores(request.args.get("airport"))
    type = request.args.get("type")
    delay = 0
    if(type == "csv"):
        flask.abort(410)
    elif(type == "json" or type == None):
        with open(jsondir) as f:
            data = json.load(f)
            if(month == None):
                if(airport == None):
                    if(reason == "total" or reason == None):
                        for index in data:
                            if(carrier in index["carrier"]["name"]):
                                delay = index["statistics"]["minutes delayed"]["total"] + delay
                    else:
                        for index in data:
                            if(carrier in index["carrier"]["name"]):
                                delay = delay + index["statistics"]["minutes delayed"][reason]
                else:
                    if(reason == "total" or reason == None):
                        for index in data:
                            if(carrier in index["carrier"]["name"] and airport in index["carrier"]["name"]):
                                delay = indexp["statistics"]["minutes delayed"]["total"] + delay
                    else:
                        for index in data:
                            if(carrier in index["carrier"]["name"] and airport in index["carrier"]["name"]):
                                delay = delay + index["statistics"]["minutes delayed"][reason]
                
             
            else:
                if(airport == None):
                    if(reason == "total" or reason == None):
                        for index in data:
                            if(carrier in index["carrier"]["name"] and str(index["time"]["month"]) == month):
                                delay = index["statistics"]["minutes delayed"]["total"] + delay
                    else:
                        for index in data:
                            if(carrier in index["carrier"]["name"] and str(index["time"]["month"]) == month):
                                delay = delay + index["statistics"]["minutes delayed"][reason]
                else:
                    if(reason == "total" or reason == None):
                        for index in data:
                            if(carrier in index["carrier"]["name"] and airport in index["carrier"]["name"] and str(index["time"]["month"]) == month):
                                delay = index["statistics"]["minutes delayed"]["total"] + delay
                    else:
                        for index in data:
                            if(carrier in index["carrier"]["name"] and airport in index["carrier"]["name"] and str(index["time"]["month"]) == month):
                                delay = delay + index["statistics"]["minutes delayed"][reason]
    
    else:
        flask.abort(411)
    print("Delays(min):" + str(delay))
    return str(delay)
    
@app.route("/getstats/", methods = ["GET"])
def getStats():
    flask.abort(410)
    
##### ERRORS
@app.errorhandler(410)
def invalid_functionality(e):
    return "This functionality is not yet implemented."

@app.errorhandler(411)    
def invalid_type(e):
    return "This type is not valid. Only csv and json are available."

app.run(port='5002', ssl_context='adhoc')   