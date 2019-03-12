from __init__ import db

class Airport(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True)
    name = db.Column(db.String(120), unique=True)
    
    def __init__(self, n, c):
        self.name = n
        self.code = c

    def getId(self):
        return self.id

    def getName(self):
        return self.name
    
    def getCode(self):
        return self.code

    def setId(self, newID):
        self.id = newID
    
    def setName(self, n):
        self.name = name
        
    def setCode(self, c):
        self.code = c      
    