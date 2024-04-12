from App.database import db
from App.models.workout import Workout


def get_all_workouts():
    return Workout.query.all()

