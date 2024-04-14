from App.controllers.workout import get_all_workouts
from App.controllers.routine import get_all_routines
from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.models.workout import Workout
from App.models.routine import Routine
from App.controllers import create_user

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    workouts = get_all_workouts()
    routines = get_all_routines()
    return render_template('index.html', workouts=workouts, routines = routines)
  

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})