from __init__ import db

class Time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.Integer)
    year = db.Column(db.Integer)

    def __init__(self, m, y):
        month = m
        year = y

    def getMonth(id):
        return m

    def getYear(id):
        return y

    def getLabel(id):
        return y + "/" + m
