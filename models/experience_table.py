from app import db

class ExperienceTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    xp = db.Column(db.Float)
    level = db.Column(db.Integer)