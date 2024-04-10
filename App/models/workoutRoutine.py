from App.database import db

class WorkoutRoutine(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  workouts = db.relationship('Workout', backref=db.backref('routines', lazy=True))
  routines = db.relationship('Routine', backref=db.backref('routines', lazy=True))


