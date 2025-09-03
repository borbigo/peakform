from datetime import datetime
from extensions import db

class Workout(db.Model):
    __tablename__ = 'workout'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False, default=lambda: datetime.utcnow().date())
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'date': self.date.isoformat() # convert date object -> YYYY-MM-DD
        }

    def __repr__(self):
        return f"<Workout {self.name} on {self.date}>"
