from App.models.routine import Routine
from App.models.workout import Workout
from App.database import db
from flask import  jsonify

def create_routine(name,user_id):
  new_routine = Routine(name=name,user_id=user_id)
  db.session.add(new_routine)
  db.session.commit()
  return new_routine

def get_routine(id):
    return Routine.query.get(id)

def get_all_routines():
    routines = Routine.query.all()
    routines_json = [routine.get_json() for routine in routines]
    return jsonify(routines_json)

def get_user_routines(user_id):
    return Routine.query.filter_by(user_id=user_id).all()

def update_routine(id, name=None):
    routine = get_routine(id)
    if routine:
        if name:
            routine.name = name
        db.session.add(routine)
        db.session.commit()
        return routine
    return None

def delete_routine(id):
    routine = get_routine(id)
    if routine:
        db.session.delete(routine)
        db.session.commit()
        return routine
    return None


def add_workout_to_routine(routine_id, workout_id):
  routine = get_routine(routine_id)
  workout = Workout.query.get(workout_id)
  if routine and workout:
      if workout not in routine.workouts:
          routine.workouts.append(workout)
          db.session.commit()
      return routine
  return None


def remove_workout_from_routine(routine_id, workout_id):
    routine = get_routine(routine_id)
    workout = Workout.query.get(workout_id)
    if routine and workout:
        routine.remove_workout(workout)
        return routine
    return None