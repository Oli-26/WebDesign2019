from __init__ import db

class Statistics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    relationID = db.Column(db.Integer, ForeignKey=("Relation_table.id"), nullable=False)
    flightID = db.Column(db.Integer, ForeignKey=("Flights.id"), nullable=False)
    delayID = db.Column(db.Integer, ForeignKey=("Delays.id"), nullable=False)

    def __init__(self, rID, fID, dID):
        self.relationID = rID
        self.flightID = fID
        self.delayID = dID

    def getRelationID(self, id):
        return self.relationID

    def getFlightID(self, id):
        return self.flightID

    def getDelayID(self, id):
        return self.delayID