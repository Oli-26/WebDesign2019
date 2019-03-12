from __init__ import db
from sqlalchemy import Table, Column, Integer, ForeignKey

class Delays_minutes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lateAircraft = db.Column(db.Integer)
    carrier = db.Column(db.Integer)
    security = db.Column(db.Integer)
    weather = db.Column(db.Integer)
    nationalAviationSystem = db.Column(db.Integer)
    total = db.Column(db.Integer)

    def __init__(self, la, c, s, w, nas, t):
        self.lateAircraft = la
        self.carrier = c
        self.security = s
        self.weather = w
        self.nationalAviationSystem = nas
        self.total = t

    def getId(self):
        return self.id

    def getLateAircraft(self):
        return self.lateAircraft

    def getCarrier(self):
        return self.carrier

    def getSecurity(self):
        return self.security

    def getWeather(self):
        return self.weather

    def getNationalAviationSystem(self):
        return self.nationalAvaiationSystem

    def getTotal(self):
        return self.total

    def setId(self, newID):
        self.id = newID

    def setLateAircraft(self, la):
        self.lateAircraft = la

    def setCarrier(self, c):
        self.carrier = c

    def setSecurity(self, s):
        self.security = s

    def setWeather(self, w):
        self.weather = w

    def setNationalAvaitionSystem(self, nas):
        self.nationalAviationSystem = nas

    def setTotal(self, new_total):
        self.total = newTotal

