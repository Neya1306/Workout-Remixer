from App.database import db

class WorkoutRoutine(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))
  workouts = db.relationship('Workout', backref=db.backref('routines', lazy=True))
  routine_id = db.Column(db.Integer, db.ForeignKey('routine.id'))
  routines = db.relationship('Routine', backref=db.backref('routines', lazy=True))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  users = db.relationship('User', backref=db.backref('routines', lazy=True))

  def __init__(self, name, workout_id, routine_id):
    self.name = name
    self.workout_id = workout_id
    self.routine_id = routine_id
    

  def to_dict(self):
    return{
      "id": self.id,
      "name": self.name,
      "workout_id": self.workout_id,
      "routine_id": self.routine_id,
    }
      
  


