import os
from flask import Flask

from models import Workouts

INCREMENT = 5

I = 0
J = I + INCREMENT
SIZE = 0

def gen_workout(muscle_group, experience_level, equipment):

    data = []
    workouts = Workouts.query.filter(Workouts.bodyPart==muscle_group, Workouts.level==experience_level, Workouts.equipment==equipment).all()

    global I
    global J
    global SIZE
    SIZE = len(workouts)

    I += INCREMENT
    J += INCREMENT
    if J > SIZE:
        I = 0
        J = I + INCREMENT

    actual_workouts = workouts[I:J]

    for w in actual_workouts:
        d = []
        d.append(w.title)
        d.append(w.bodyPart)
        d.append(w.level)

        data.append(d)

    return data