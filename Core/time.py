from __init__  import db

class Time(db.Model):
    __tablename__ = 'Time'
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.Integer)
    year = db.Column(db.Integer)

    def __init__(self, m, y):
        self.month = m
        self.year = y

    def getId(self):
        return self.id

    def getMonth(self, id):
        return self.month

    def getYear(self, id):
        return self.year

    def getLabel(self, id):
        return str(self.year) + "/" + str(self.month)

    def setId(self, newID):
        self.id = newID

    def setMonth(self, m):
        self.month = m

    def setYear(self, y):
        self.year = y
