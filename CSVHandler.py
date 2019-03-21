import csv
import json
import flask
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from __init__ import app, db
import math



from Core.airport import Airport
from Core.time import Time 
from Core.carrier import Carrier
from Core.flights import Flights
from Core.delays_minutes import Delays_minutes
from Core.delays_amount import Delays_amount
from Core.delays import Delays
from Core.relation_table import Relation_table
from Core.statistics import Statistics

class CSVHandler():
    
    def getAirportCSV(dictionary = None, dataList = None):
        returnString = ""
    
        if not dictionary is None:
            
            returnString = returnString + dictionary["name"] + "\n"
            for uri in dictionary["uri-list"]:
                returnString = returnString + uri + "\n"
        else:
            for data in dataList:
                returnString = returnString + data["name"] + "," + data["uri"] + "\n"
    
        return returnString
            
    
    def getCarrierCSV(dictionary = None, dataList = None):
        returnString = ""
        
        if not dictionary is None:
            returnString = returnString + dictionary["name"] + "\n"
            returnString = returnString + dictionary["statistics-uri"] + "\n"
            for uri in dictionary["airport-uris"]:
                returnString = returnString + uri + "\n"
        
        else:
            for data in dataList:
                returnString = returnString + data["name"] + "," + data["uri"] + "\n"
        return returnString