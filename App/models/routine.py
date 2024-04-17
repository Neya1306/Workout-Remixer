from App.database import db

class Routine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
                                                             
  

    def __init__(self, name,user_id):
        self.name = name
        self.user_id = user_id
    

    def get_json(self):
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

  
  