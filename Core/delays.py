from __init__ import db
from sqlalchemy import Table, Column, Integer, ForeignKey

class Delays(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    minutesID = db.Column(db.Integer, ForeignKey("Delays_minutes.id"))
    amountID = db.Column(db.Integer, ForeignKey("Delays_amount.id"))

    def __init__(self, mID, aID):
        self.minutesID = mID
        self.amountID = aID

    def getId(self):
        return self.id

    def getMinutesID(self, id):
        return self.minutesID

    def getAmountID(self, id):
        return self.amountID

    def setId(self, newID):
        self.id = newID

    def setMinutesID(self, mID):
        self.minutesID = mID

    def setAmountID(self, aID):
        self.amountID = aID
