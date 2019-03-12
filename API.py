import csv
import json
import flask
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from __init__ import app
jsondir = "airlines.json"





app.run(port='5002', ssl_context='adhoc')  