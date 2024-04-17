from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, url_for,flash
from App.models import db
from App.models.routine import Routine
from App.models.workout import Workout
from App.models.workoutRoutine import WorkoutRoutine
from flask_jwt_extended import current_user,jwt_required
from App.controllers.routine import create_routine, get_routine, get_all_routines, get_user_routines, add_workout_to_routine, delete_routine, remove_workout_from_routine


routine_views = Blueprint('routine_views', __name__, template_folder='../templates')



@routine_views.route('/addRoutine', methods=['POST'])
def add_routine_to_workout():
    workout_id = request.form['workout_id']
    routine_id = request.form['routine_id']
    
    existing_workout_routine = WorkoutRoutine.query.filter_by(workout_id=workout_id, routine_id=routine_id).first()
    
    if existing_workout_routine:
        flash('Workout already exists in routine')
    else:
        new_workout_routine = WorkoutRoutine(workout_id=workout_id, routine_id=routine_id)
        db.session.add(new_workout_routine)
        db.session.commit()
        flash('Workout added successfully')
    return redirect(url_for('index_views.index_page'))


@routine_views.route('/createroutine', methods=['POST'])
@jwt_required()
def create_routine_page():
    name = request.form['name']
    create_routine(name,current_user.id )
    return redirect(url_for('index_views.index_page'))

@routine_views.route('/routine/<int:routine_id>', methods=['GET'])
def view_routine_page(routine_id):
    workouts = WorkoutRoutine.query.filter_by(routine_id=routine_id).all()
    workout_data = []
    for workout in workouts:
        workout_obj = Workout.query.get(workout.workout_id)
        workout_data.append(workout_obj)
    return render_template('routine.html', workouts=workout_data,routine_id=routine_id)

# Route to delete a routine
@routine_views.route('/delete_routine/<int:routine_id>', methods=['POST'])
def delete_routine_page(routine_id):
    delete_routine(routine_id)
    return redirect(url_for('index_views.index_page'))

# Route to remove workout from routine
@routine_views.route('/deleteworkout/<int:routine_id>/<int:workout_id>', methods=['POST'])
def delete_workout(routine_id, workout_id):
    remove_workout_from_routine(routine_id, workout_id)
    return redirect(request.referrer)

@routine_views.route('/routines', methods=['GET'])
def get_all_routines_page():
  routines = Routine.query.all()
  return render_template('routine.html', routines = routines)