from __init__ import db


class DelaysMinutes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    late_aircraft = db.Column(db.Integer)
    carrier = db.Column(db.Integer)
    security = db.Column(db.Integer)
    weather = db.Column(db.Integer)
    national_aviation_system = db.Column(db.Integer)
    total = db.Column(db.Integer)

    def __init__(self, la, c, s, w, nas, t):
        self.late_aircraft = la
        self.carrier = c
        self.security = s
        self.weather = w
        self.national_aviation_system = nas
        self.total = t

    @staticmethod
    def get_late_aircraft(self):
        return self.late_aircraft

    @staticmethod
    def get_carrier(self):
        return self.carrier

    @staticmethod
    def get_security(self):
        return self.security

    @staticmethod
    def get_weather(self):
        return self.weather

    @staticmethod
    def get_national_aviation_system(self):
        return self.national_avaiation_system

    @staticmethod
    def get_total(self):
        return self.total

    def set_late_aircraft(self, la):
        self.late_aircraft = la

    def set_carrier(self, c):
        self.carrier = c

    def set_security(self, s):
        self.security = s

    def set_weather(self, w):
        self.weather = w

    def set_national_avaition_system(self, nas):
        self.national_aviation_system = nas

    def set_total(self, new_total):
        self.total = new_total

