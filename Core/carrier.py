from __init__ import db


class Carrier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True)
    name = db.Column(db.String(120), unique=True)

    def __init__(self, n, c):
        self.name = n
        self.code = c

    @staticmethod
    def get_name(self):
        return self.name

    @staticmethod
    def get_code(self):
        return self.code

    def set_name(self, new_name):
        self.name = new_name

    def set_code(self, new_code):
        self.code = new_code

