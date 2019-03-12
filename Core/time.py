from __init__ import db

class Time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.Integer)
    year = db.Column(db.Integer)

    def __init__(self, m, y):
        self.month = m
        self.year = y

    def getMonth(self, id):
        return self.month

    def getYear(self, id):
        return self.year
        
    def getId(self):
        return self.id

    def getLabel(self, id):
        return str(self.year) + "/" + str(self.month)
