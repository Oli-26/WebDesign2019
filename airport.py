from __init__ import db

class Airport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), index=True, unique=True)
    name = db.Column(db.String(120), index=True, unique=True)
    
    def __init__(self, n, c):
        name = n
        code = c
    
        