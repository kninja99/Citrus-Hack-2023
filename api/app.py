import os
import json
from flask import Flask, jsonify, render_template,request,make_response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

from init_db import db, app
from workouts import gen_workout

#TODO: remove these 2 lines when User db is up and running
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
    try:
        muscle = request.args['Muscle']
        workouts = jsonify(gen_workout(muscle, EXPERIENCE_LEVEL, EQUIPMENT))
        return workouts
    
    except:
        response = make_response("<h1>Failed</h1>")
        response.status_code = 404
        return response
    
    


if __name__ == '__main__':
    app.run()
