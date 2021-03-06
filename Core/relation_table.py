from __init__ import db
from sqlalchemy import Table, Column, Integer, ForeignKey

class Relation_table(db.Model):
    __tablename__ = 'Relation_table'
    id = db.Column(db.Integer, primary_key=True)
    airportID = db.Column(db.Integer, ForeignKey("Airport.id"), nullable=False)
    carrierID = db.Column(db.Integer, ForeignKey("Carrier.id"), nullable=False)
    timeID = db.Column(db.Integer, ForeignKey("Time.id"), nullable=False)

    def __init__(self,aID,cID,tID):
        self.airportID = aID
        self.carrierID = cID
        self.timeID = tID

    def getId(self):
        return self.id

    def getAirportID(self):
        return self.airportID

    def getCarrierID(self):
        return self.carrierID

    def getTimeID(self):
        return self.timeID

    def setId(self, newID):
        self.id = newID

    def setAirportID(self, aID):
        self.airportID = aID

    def setCarrierID(self, cID):
        self.carrierID = cID

    def setTimeID(self, tID):
        self.timeID = tID
