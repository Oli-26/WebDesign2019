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
        
    def getMonthText(num):
        num = int(num)
        if(num == 1):
            return "january"
        if(num == 2):
            return "febuary"
        if(num == 3):
            return "march"
        if(num == 4):
            return "april"
        if(num == 5):
            return "may"
        if(num == 6):
            return "june"
        if(num == 7):
            return "july"
        if(num == 8):
            return "august"
        if(num == 9):
            return "september"    
        if(num == 10):
            return "october"
        if(num == 11):
            return "november"
        if(num == 12):
            return "december"
        return "not-a-month"