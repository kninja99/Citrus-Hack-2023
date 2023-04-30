import os
import json
from flask import Flask, jsonify, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

from init_db import db, app
from workouts import gen_workout

#TODO: remove these 3 lines when User db is up and running
MUSCLE = "Chest"
EXPERIENCE_LEVEL = "Intermediate"
# EQUIPMENT = ["Dumbbell"]
EQUIPMENT = "Dumbbell"

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/generate', methods=['GET'])
def generate_workout():
    workouts = gen_workout(MUSCLE, EXPERIENCE_LEVEL, EQUIPMENT)
    json_data = json.dumps(workouts)

if __name__ == '__main__':
    app.run()
