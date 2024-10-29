from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

db = SQLAlchemy()

class Habit(db.Model):
    __tablename__ = 'habits'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    habit_name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, default=datetime.utcnow)
    end_date = db.Column(db.Date)
    notes = db.Column(db.Text)

    def __init__(self, user_id, habit_name, notes=''):
        self.user_id = user_id
        self.habit_name = habit_name
        self.notes = notes
        self.end_date = datetime.utcnow() + timedelta(days=90)

class HabitProgress(db.Model):
    __tablename__ = 'habit_progress'
    id = db.Column(db.Integer, primary_key=True)
    habit_id = db.Column(db.Integer, db.ForeignKey('habits.id'), nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow)
    completed = db.Column(db.Boolean, default=False)
    notes = db.Column(db.Text)

    habit = db.relationship('Habit', backref='progress')
