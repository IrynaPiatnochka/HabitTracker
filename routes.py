from flask import Blueprint
from controllers.habitControllers import (
    get_habits,
    create_habit,
    get_habit_progress,
    record_progress
)

habit_blueprint = Blueprint('habit_bp', __name__)

habit_blueprint.route('/habits', methods=['GET', 'OPTIONS'])(get_habits)
habit_blueprint.route('/habits', methods=['POST', 'OPTIONS'])(create_habit)
habit_blueprint.route('/habits/<int:habit_id>/progress', methods=['GET', 'OPTIONS'])(get_habit_progress)
habit_blueprint.route('/habits/<int:habit_id>/progress', methods=['POST', 'OPTIONS'])(record_progress)
