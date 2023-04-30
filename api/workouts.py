import os
from flask import Flask

from models import Workouts

def gen_workout(muscle_group, experience_level, equipment):

    data = []
    workouts = Workouts.query.filter(Workouts.bodyPart==muscle_group, Workouts.level==experience_level, Workouts.equipment==equipment).limit(5)
    for w in workouts:
        d = []
        d.append(w.title)
        d.append(w.bodyPart)
        d.append(w.level)

        data.append(d)

    return data