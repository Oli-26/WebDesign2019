from __init__ import db

class Relation_table:
	id = db.Column(db.Integer, primary_key=True)
	airportID = db.Column(db.Integer, ForeignKey=("airport.id"), nullable=False)
	carrierID = db.Column(db.Integer, ForeignKey=("carrier.id"), nullable=False)
	timeID = db.Column(db.Integer, ForeignKey=("time.id"), nullable=False)


	def __init__(self,aID,cID,tID):
		airportID = aID
		carrierID = cID
		timeID = tID
