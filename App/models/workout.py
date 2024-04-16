from App.database import db

class Workout(db.Model):
  id=db.Column(db.Integer, primary_key=True)
  name=db.Column(db.String(100), nullable=False)
  bodypart = db.Column(db.String(100), nullable=False)
  equipment = db.Column(db.String(100), nullable=False)
  target = db.Column(db.String(100), nullable=False)
  secondaryMuscles = db.Column(db.String(100), nullable=False)
  instruction0 = db.Column(db.String(100), nullable=False)
  instruction1 = db.Column(db.String(100), nullable=False)
  gifurl = db.Column(db.String(100), nullable=False)
  
  
    
  
  def __init__(self, name, bodypart, equipment, target, secondaryMuscles, instruction0,instruction1, gifurl):
        self.name = name
        self.bodypart = bodypart
        self.equipment = equipment
        self.target = target
        self.secondaryMuscles = secondaryMuscles
        self.instruction0 = instruction0
        self.instruction1 = instruction1
        self.gifurl = gifurl

  def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "bodypart": self.bodypart,
            "equipment": self.equipment,
            "target": self.target,
            "secondaryMuscles": self.secondaryMuscles,
            "instruction0": self.instruction0,
            "instruction1": self.instruction1,
            "gifurl": self.gifurl
        }

 