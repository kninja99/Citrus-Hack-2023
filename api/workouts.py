import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import db, Workouts

MUSCLE = "Chest"
EXPERIENCE_LEVEL = "Intermediate"
EQUIPMENT = "Dumbbell"

def generate_workout(muscle_group, experience_level, equipment):
    workouts = Workouts.query.filter(Workouts.bodyPart==MUSCLE, Workouts.level==EXPERIENCE_LEVEL, Workouts.equipment==EQUIPMENT).limit(5)
    for w in workouts:
        print(w.title)
        print(w.desc)
        print(w.bodyPart)
        print(w.level)
        print("---------------------------")

if __name__ == "__main__":

    basedir = os.path.abspath(os.path.dirname(__file__))
    # # instantiate the app
    app = Flask(__name__)
    app.config.from_object(__name__)

    # # DB Setup with SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # db = SQLAlchemy()
    db.init_app(app)

    with app.app_context():
        generate_workout(MUSCLE, EXPERIENCE_LEVEL, EQUIPMENT)