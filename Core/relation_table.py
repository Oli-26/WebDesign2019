from __init__ import db

class Relation_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    airportID = db.Column(db.Integer, ForeignKey=("Airport.id"), nullable=False)
    carrierID = db.Column(db.Integer, ForeignKey=("Carrier.id"), nullable=False)
    timeID = db.Column(db.Integer, ForeignKey=("Time.id"), nullable=False)

    def __init__(self,aID,cID,tID):
        self.airportID = aID
        self.carrierID = cID
        self.timeID = tID

    def getAirportID(self, id):
        return self.airportID

    def getCarrierID(self, id):
        return self.carrierID

    def getTimeID(self, id):
        return self.timeID