# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from extensions import db
from models import Workout
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///peakform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/workouts", methods=["GET"])
def get_workouts():
    workouts = Workout.query.all()
    return jsonify([w.to_dict() for w in workouts])

@app.route("/workouts", methods=["POST"])
def add_workout():
    data = request.json
    
    # convert date string -> Python date object
    workout_date = datetime.strptime(data['date'], '%Y-%m-%d').date()
    
    new_workout = Workout(
        name=data['name'],
        date=workout_date
    )
    db.session.add(new_workout)
    db.session.commit()
    return jsonify(new_workout.to_dict()), 201

@app.route("/workouts/<int:id>", methods=["DELETE"])
def delete_workout(id):
    workout = Workout.query.get_or_404(id)
    db.session.delete(workout)
    db.session.commit()
    return jsonify({"message": "Workout deleted"})
