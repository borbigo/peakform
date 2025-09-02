from flask import Blueprint, request, jsonify

workouts_bp = Blueprint('workouts', __name__, url_prefix="/workouts")

# Example workouts list (placeholder)
workouts_list = []

@workouts_bp.route('/', methods=['GET'])
def get_workouts():
  return jsonify(workouts_list)

@workouts_bp.route('/', methods=['POST'])
def add_workout():
  data = request.get_json()
  workouts_list.append(data)
  return jsonify({"message": "Workout added.", "workout": data})