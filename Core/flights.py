from __init__ import db


class Flights(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cancelled = db.Column(db.Integer)
    on_time = db.Column(db.Integer)
    delayed = db.Column(db.Integer)
    diverted = db.Column(db.Integer)
    total = db.Column(db.Integer)

    def __init__(self, cancel, onTime, delay, divert, t):
        self.cancelled = cancel
        self.on_time = onTime
        self.delayed = delay
        self.diverted = divert
        self.total = t

    @staticmethod
    def get_cancelled(self):
        return self.cancelled

    @staticmethod
    def get_on_time(self):
        return self.on_time

    @staticmethod
    def get_delayed(self):
        return self.delayed

    @staticmethod
    def get_diverted(self):
        return self.diverted

    @staticmethod
    def get_total(self):
        return self.total

    def set_cancelled(self, new_cancelled):
        self.cancelled = new_cancelled

    def set_on_time(self, new_on_time):
        self.on_time = new_on_time

    def set_name(self, new_delayed):
        self.delayed = new_delayed

    def set_diverted(self, new_diverted):
        self.diverted = new_diverted

    def set_total(self, new_total):
        self.total = new_total

