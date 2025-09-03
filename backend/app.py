from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

# -------------------
# App & DB Setup
# -------------------
app = Flask(__name__)
CORS(app)

# SQLite database location
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'instance', 'peakform.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# -------------------
# Routes
# -------------------
@app.route('/workouts', methods=['GET'])
def get_workouts():
    from models import Workout  # Import here to avoid circular import
    workouts = Workout.query.all()
    workouts_list = [
        {"id": w.id, "name": w.name, "date": w.date.strftime("%Y-%m-%d") if w.date else None}
        for w in workouts
    ]
    return jsonify(workouts_list)


@app.route('/workouts', methods=['POST'])
def add_workout():
    from models import Workout  # Import here to avoid circular import
    data = request.get_json()
    new_workout = Workout(name=data['name'], date=data['date'])
    db.session.add(new_workout)
    db.session.commit()
    return jsonify({"message": "Workout added!", "id": new_workout.id}), 201

# -------------------
# Run
# -------------------
if __name__ == '__main__':
    # Ensure instance folder exists
    os.makedirs(os.path.join(basedir, 'instance'), exist_ok=True)
    db.create_all()
    app.run(debug=True)
