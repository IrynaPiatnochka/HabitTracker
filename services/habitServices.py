from models import db, Habit, HabitProgress

def get_all_habits():
    habits = Habit.query.all()
    return [{'id': h.id, 'user_id': h.user_id, 'habit_name': h.habit_name, 
             'start_date': h.start_date.strftime('%Y-%m-%d'), 
             'end_date': h.end_date.strftime('%Y-%m-%d'), 
             'notes': h.notes} for h in habits]

def create_new_habit(data):
    new_habit = Habit(
        user_id=data['user_id'],
        habit_name=data['habit_name'],
        notes=data.get('notes', '')
    )
    db.session.add(new_habit)
    db.session.commit()
    return {'id': new_habit.id, 'habit_name': new_habit.habit_name}

def get_progress_for_habit(habit_id):
    progress_records = HabitProgress.query.filter_by(habit_id=habit_id).order_by(HabitProgress.date).all()
    return [{'date': record.date.strftime('%Y-%m-%d'), 'completed': record.completed, 'notes': record.notes} for record in progress_records]

def save_progress(habit_id, data):
    new_progress = HabitProgress(habit_id=habit_id, completed=data['completed'], notes=data.get('notes', ''))
    db.session.add(new_progress)
    db.session.commit()
    return {'message': 'Progress recorded'}
