from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, url_for
from App.models import db
from App.models.routine import Routine

from App.controllers.routine import create_routine, get_routine, get_all_routines, get_user_routines, add_workout_to_routine


routine_views = Blueprint('routine_views', __name__, template_folder='../templates')



@routine_views.route('/addRoutine', methods=['POST'])
def add_to_routine():
    workout_id = request.form['workout_id']
    routine_id = request.form['routine_id']
    add_workout_to_routine(routine_id, workout_id)
    return redirect(url_for('index_views.index_page'))


@routine_views.route('/createroutine', methods=['POST'])
def create_routine_page():
    name = request.form['name']
    workout_id = request.form['workout_id']
    create_routine(name, workout_id)
    return redirect(url_for('index_views.index_page'))
