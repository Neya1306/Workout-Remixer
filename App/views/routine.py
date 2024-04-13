from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.models.routine import Routine

from App.controllers.routine import create_routine, get_routine, get_all_routines, get_user_routines


routine_views = Blueprint('routine_views', __name__, template_folder='../templates')

@routine_views.route('/addroutine', methods=['GET'])
def get_routines_page():
  
  routines = get_all_routines()
  return render_template('workouts.html', routines=routines)  