from datetime import datetime
from app import db

class Workout(db.Model):
    __tablename__ = 'workout'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False, default=lambda: datetime.utcnow().date())

    def __repr__(self):
        return f"<Workout {self.name} on {self.date}>"
