from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(50))
    description = db.Column(db.String(200))
    priority = db.Column(db.Integer)
    completed = db.Column(db.Integer)
    xp = db.Column(db.Integer)
    deadline = db.Column(db.Date)