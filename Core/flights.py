from __init__ import db
from sqlalchemy import Table, Column, Integer, ForeignKey


class Flights(db.Model):
    __tablename__ = 'Flights'
    id = db.Column(db.Integer, primary_key=True)
    cancelled = db.Column(db.Integer)
    onTime = db.Column(db.Integer)
    delayed = db.Column(db.Integer)
    diverted = db.Column(db.Integer)
    total = db.Column(db.Integer)

    def __init__(self, cancel, onTime, delay, divert, t):
        self.cancelled = cancel
        self.onTime = onTime
        self.delayed = delay
        self.diverted = divert
        self.total = t

    def getCancelled(self):
        return self.cancelled

    def getOnTime(self):
        return self.on_time

    def getDelayed(self):
        return self.delayed

    def getDiverted(self):
        return self.diverted

    def getTotal(self):
        return self.total

    def setCancelled(self, new_cancelled):
        self.cancelled = new_cancelled

    def setOnTime(self, new_on_time):
        self.on_time = new_on_time

    def setName(self, new_delayed):
        self.delayed = new_delayed

    def setDiverted(self, new_diverted):
        self.diverted = new_diverted

    def setTotal(self, new_total):
        self.total = new_total

