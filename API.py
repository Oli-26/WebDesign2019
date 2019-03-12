import csv
import json
import flask
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from __init__ import app, db


#### CORE
from Core.airport import Airport
from Core.time import Time

jsondir = "airlines.json"



#airport1 = Airport(c = "AAA", n = "American Airlines Air")
#db.session.add(airport1)
#db.session.commit()


airports = Airport.query.all()
print(str(airports.name))


#time1 = Time(m = 6, y = 1997)
#db.session.add(time1)
#db.session.commit()

times = Time.query.all()
for t in times:
    print(t.getLabel(t.getId()))


app.run(port='5002', ssl_context='adhoc')  