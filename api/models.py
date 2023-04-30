from init_db import db

# Create DB model
class Workouts(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    title = db.Column(db.String(100), nullable = False)
    desc = db.Column(db.Text)
    typeOfWorkout =db.Column(db.String(100))
    bodyPart = db.Column(db.String(100))
    equipment = db.Column(db.String(150))
    level = db.Column(db.String(100))
    rating = db.Column(db.Float)
    # adding a string representation
    def __repr__(self):
        return f'<Workout {self.title}>'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    profile_pic = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'