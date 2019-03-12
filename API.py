import csv
import json
import flask
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from __init__ import app, db
from Core.airport import Airport


jsondir = "airlines.json"



airport1 = Airport(c = "AAA", n = "American Airlines Air")
db.session.add(airport1)
db.session.commit()


airports = Airport.query.all()
print(airports)

app.run(port='5002', ssl_context='adhoc')  