from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.models.workout import Workout

from App.controllers.workout import get_all_workouts


workout_views = Blueprint('workout_views', __name__, template_folder='../templates')

@workout_views.route('/workouts', methods=['GET'])
def get_workouts_page():
  workouts = get_all_workouts
  return render_template('workouts.html', workouts=workouts)  