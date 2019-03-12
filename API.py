import csv
import json
import flask
from flask import Flask, request, jsonify
from flask_restful import Resource, Api


app = Flask(__name__)
jsondir = "airlines.json"





app.run(port='5002', ssl_context='adhoc')  