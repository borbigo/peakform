# models.py
from app import db
from sqlalchemy import func, text

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=func.now())

    # optional: relationship if you want to link workouts
    workouts = db.relationship('Workout', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"


class Workout(db.Model):
    __tablename__ = 'workout'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, server_default=func.now())
    activity_type = db.Column(db.String(50), nullable=False, server_default=text("'Run'"))
    duration_minutes = db.Column(db.Integer, nullable=False, server_default=text('0'))
    distance = db.Column(db.Float, nullable=False, server_default=text('0.0'))
    notes = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<Workout {self.activity_type} by User {self.user_id}>"
