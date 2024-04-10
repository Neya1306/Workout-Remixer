from App.models import Routine

from App.database import db

def add_exercise(self,name, workout):
  if workout not in self.workouts:
      new_routine = Routine(name=name, workout=workout, user_id=self.id)
      self.workout.append(new_routine)
      db.session.commit()

def remove_exercise(self, workout):
  if workout in self.workouts:
      self.workouts.remove(workout)
      db.session.commit()