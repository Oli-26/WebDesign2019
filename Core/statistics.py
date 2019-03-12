from __init__ import db
from sqlalchemy import Table, Column, Integer, ForeignKey

class Statistics(db.Model):
    __tablename__ = 'Statistics'
    id = db.Column(db.Integer, primary_key=True)
    relationID = db.Column(db.Integer, ForeignKey("Relation_table.id"), nullable=False)
    flightID = db.Column(db.Integer, ForeignKey("Flights.id"), nullable=False)
    delayID = db.Column(db.Integer, ForeignKey("Delays.id"), nullable=False)

    def __init__(self, rID, fID, dID):
        self.relationID = rID
        self.flightID = fID
        self.delayID = dID

    def getId(self):
        return self.id

    def getRelationID(self, id):
        return self.relationID

    def getFlightID(self, id):
        return self.flightID

    def getDelayID(self, id):
        return self.delayID
    
    def setId(self, newID):
        self.id = newID
    
    def setRelationID(self, rID):
        self.relationID = rID

    def setFlightID(self, fID):
        self.flightID = fID

    def setDelayID(self, dID):
        self.delayID = dID