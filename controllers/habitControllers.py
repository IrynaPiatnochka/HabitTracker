from flask import request, jsonify
from schemas import habit_schema, habit_progress_schema
from services.habitServices import (
    get_all_habits,
    create_new_habit,
    get_progress_for_habit,
    save_progress
)

def get_habits():
    habits = get_all_habits()
    return habit_schema.dump(habits, many=True), 200

def create_habit():
    data = request.get_json()
    habit = habit_schema.load(data)  # Deserialize input data
    new_habit = create_new_habit(habit)
    return habit_schema.dump(new_habit), 201

def get_habit_progress(habit_id):
    progress_records = get_progress_for_habit(habit_id)
    return habit_progress_schema.dump(progress_records, many=True), 200

def record_progress(habit_id):
    data = request.get_json()
    progress = habit_progress_schema.load(data)  # Deserialize input data
    result = save_progress(habit_id, progress)
    return habit_progress_schema.dump(result), 201
