from App.controllers.workout import get_all_workouts
from App.controllers.routine import get_all_routines
from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_jwt_extended import jwt_required, current_user
from App.models import db
from App.models.workout import Workout
from App.models.routine import Routine
from App.controllers import create_user
from App.controllers.routine import get_user_routines

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/home', methods=['GET'])
@jwt_required()
def index_page():
    workouts = get_all_workouts()
    routines =get_user_routines(current_user.id)
    return render_template('index.html', workouts=workouts, routines = routines)

@index_views.route('/filter', methods=['GET'])
@jwt_required()
def get_target_workout():
    bodypart = request.args.get('bodypart')
    workouts = Workout.query.filter_by(bodypart=bodypart).all()
    routines = Routine.query.all()
    return render_template('index.html', workouts=workouts, routines=routines)
  
@index_views.route('/search', methods=['GET'])
@jwt_required()
def search_workouts():
    routines = Routine.query.all()
    key = request.args.get('key')
    if key:
        workouts= Workout.query.filter(Workout.name.ilike(f'%{key}%')).all()
    return render_template('index.html', workouts=workouts, routines=routines)

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})