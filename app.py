from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np
import pandas as pd

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

nav = '''
    <div style="width:80%;margin:auto">
        <img src="https://breakawayvacationrentals.com/wp-content/uploads/2014/05/hawaii-vacation-destination-history-attractions.png" style="height:40vh;width:100%">

        <h1>Available Routes:</h1>
        <ul>
              <li> <a href="/api/v1.0/precipitation">Precipitation</a> </li>
              <li> <a href="/api/v1.0/stations">Stations</a> </li>
              <li> <a href="/api/v1.0/tobs">Temps</a> </li>
              <li> <a href="/api/v1.0/start">Start Data</a> </li>
              <li> <a href="/api/v1.0/start/end">Start and End Date</a> </li>
        </ul>
    </div>
'''

app = Flask(__name__)

@app.route("/")
def welcome():
    return nav


@app.route("/api/v1.0/precipitation")
def precipitation():
    precipitation = list(np.ravel(session.query(Measurement.date,Measurement.prcp).all()))
    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations():
    stations = list(np.ravel(session.query(Station.station).all()))
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def temp():
    temps = list(np.ravel(session.query(Measurement.date,Measurement.tobs).all()))
    return jsonify(temps)



if __name__ == "__main__":
    app.run(debug=True)
