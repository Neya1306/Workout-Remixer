from App.database import db

class Routine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'), nullable=False)
    workout = db.relationship('Workout', backref=db.backref('routines', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('routines', lazy=True))

    def __init__(self, name):
        self.name = name
 


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "Workouts": [workout.to_dict() for workout in self.workouts]
        }

  
  