from App.database import db

class Workout(db.Model):
  id=db.Column(db.Integer, primary_key=True)
  name=db.Column(db.String(100), nullable=False)
  bodypart = db.Column(db.String(100), nullable=False)
  equipment = db.Column(db.String(100), nullable=False)
  target = db.Column(db.String(100), nullable=False)
  secondaryMuscles = db.Column(db.String(100), nullable=False)
  instructions = db.Column(db.String(100), nullable=False)
  gifurl = db.Column(db.String(100), nullable=False)
  
  
    
  
  def __init__(self, name, bodypart, equipment, target, secondaryMuscles, instructions, gifurl):
        self.name = name
        self.bodypart = bodypart
        self.equipment = equipment
        self.target = target
        self.secondaryMuscles = secondaryMuscles
        self.instructions = instructions
        self.gifurl = gifurl

  def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "bodypart": self.bodypart,
            "equipment": self.equipment,
            "target": self.target,
            "secondaryMuscles": self.secondaryMuscles,
            "instructions": self.instructions,
            "gifurl": self.gifurl
        }