import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)

#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL', '') or "sqlite:///db_pokemon.db"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)
#print('Base: ', Base)
# Save references to each table
Samples = Base.classes.stats
#print('Samples_Metadata: ', Samples_Metadata)
print('Data: ', Samples)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/data")
def data():
    stmt = db.session.query(Samples).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[1:])

@app.route("/gen/<Generation>")
def samples(Generation):
    """Return the MetaData for a given sample."""
    sel = [
        Samples.Generation,
        Samples.Name,
        Samples.Type_1,
        Samples.Total,
        Samples.HP,
        Samples.Attack,
        Samples.Defense
    ]

    results = db.session.query(*sel).filter(Samples.Generation == Generation).all()

    samples = {}
    
    for result in results:
        samples["Generation"] = result[0]
        samples["Name"] = result[1]
        samples["Type_1"] = result[2]
        samples["Total"] = result[3]
        samples["HP"] = result[4]
        samples["Attack"] = result[5]
        samples["Defense"] = result[6]

    print(samples)
    return jsonify(samples)

@app.route("/samples/<Number>")
def samp(Number):
    """Return `otu_ids`, `otu_labels`,and `sample_values`."""
    stmt = db.session.query(Samples).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Filter the data based on the sample number and
    # only keep rows with values above 1
    sample_data = df.loc[df[Number] > 0, ["otu_id", "otu_label", Number]]
    # Format the data to send as json
    data = {
        "otu_ids": sample_data.Number.values.tolist(),
        "sample_values": sample_data[Number].values.tolist(),
        "otu_labels": sample_data.Generation.tolist(),
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run()