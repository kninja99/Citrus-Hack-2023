import os
from flask import Flask
import pandas as pd
from flask_sqlalchemy import SQLAlchemy

from app import db, Workouts

data = pd.read_csv("../megaGymDataset.csv", index_col=0, delimiter=",")
df = pd.DataFrame(data)

try:
    basedir = os.path.abspath(os.path.dirname(__file__))
    # instantiate the app
    app = Flask(__name__)
    app.config.from_object(__name__)

    # DB Setup with SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)

    app.app_context().push()

    # add all data from csv into db
    for i in range(len(df)):
        db.session.add(
            Workouts(
                title=df.loc[i, "Title"],
                desc=df.loc[i, "Desc"],
                typeOfWorkout=df.loc[i, "Type"],
                bodyPart=df.loc[i, "BodyPart"],
                equipment=df.loc[i, "Equipment"],
                level=df.loc[i, "Level"],
                rating=df.loc[i, "Rating"]
            )
        )

    db.session.commit()

except Exception as e:
    print("Error while connecting to MySQL", e)

finally:
    db.session.close()

