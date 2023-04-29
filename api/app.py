import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))
# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# DB Setup with SQLite
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


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

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()
