from app import db

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    username = db.Column(db.String)
    level = db.Column(db.Integer)
    xp = db.Column(db.Float)
    total_xp = db.Column(db.Float)