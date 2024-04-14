from App.database import db

class Routine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))
    workouts = db.relationship('Workout', backref=db.backref('routine', lazy=True), uselist=True)
                                                             
  

    def __init__(self, name,workout_id, ):
        self.name = name
        self.workout_id = workout_id
    

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "workouts": [workout.to_dict() for workout in self.workouts]
        }

    def add_workout(self, workout):
      if workout not in self.workouts:
          self.workouts.append(workout)
          db.session.commit()

    def remove_workout(self, workout):
      if workout in self.workouts:
          self.workouts.remove(workout)
          db.session.commit()

  
  