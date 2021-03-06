from __init__ import db
from sqlalchemy import Table, Column, Integer, ForeignKey


class Carrier(db.Model):
    __tablename__ = 'Carrier'
    id = db.Column(db.Integer, primary_key=True)
    __table_args__ = (
        db.UniqueConstraint('code', 'name'),
    )
    code = db.Column(db.String(10))
    name = db.Column(db.String(200))

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

    def setName(self, new_name):
        self.name = new_name

    def setCode(self, new_code):
        self.code = new_code

