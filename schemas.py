from marshmallow import Schema, fields, post_load
from models import Habit, HabitProgress

class HabitSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    habit_name = fields.Str(required=True)
    start_date = fields.Date(dump_only=True)
    end_date = fields.Date(dump_only=True)
    notes = fields.Str()

    @post_load
    def create_habit(self, data, **kwargs):
        return Habit(**data)

class HabitProgressSchema(Schema):
    id = fields.Int(dump_only=True)
    habit_id = fields.Int(required=True)
    date = fields.Date(dump_only=True)
    completed = fields.Bool()
    notes = fields.Str()

    @post_load
    def create_habit_progress(self, data, **kwargs):
        return HabitProgress(**data)

# Instances of schemas
habit_schema = HabitSchema()
habit_progress_schema = HabitProgressSchema()
