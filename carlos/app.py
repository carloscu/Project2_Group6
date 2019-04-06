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
#table name: "stats"
Samples = Base.classes.stats

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

#print('Samples_Metadata: ', Samples_Metadata)
print('Data: ', Samples)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

""""@app.route("/data")
def data():
    stmt = db.session.query(Samples).statement
    df = pd.read_sql_query(stmt, db.session.bind)

  return jsonify(list(df.columns)[1:])  # Return a list of the column names (sample names)"""


#@app.route("/gen/<Generation>")
@app.route("/samples")
def samples():
    """Return the MetaData for a given sample."""
    """sel = [
        Samples.Generation,
        Samples.Name,
        Samples.Type_1,
        Samples.Total,
        Samples.HP,
        Samples.Attack,
        Samples.Defense
    ]"""

    """results = db.session.query(*sel).filter(Samples.Generation == Generation).all()"""

    results = session.query(samples).all()
    
    """    samples = {}"""
    all_samples = []
    for samples in results:
        """samples_dict = {}"""
            samples_dict = {}
            samples_dict["Generation"] = samples.Generation
            samples_dict["Name"] = samples.Name
            samples_dict["Type_1"] = samples.Type_1
            samples_dict["Total"] = samples.Total
            samples_dict["HP"] = samples.HP
            samples_dict["Attack"] = samples.Attack
            samples_dict["Defense"] = samples.Defense
            all_samples.append(samples_dict)

    print(samples)
    return jsonify(all_samples)


#window.onload = 
# 
function() {

chart = new CanvasJS.Chart("chartContainer", {
	animationEnabled: true,
	theme: "light2",
	title: {
		text: "Daily Sales Data"
	},
	axisY: {
		title: "Units",
		titleFontSize: 24
	},
	data: [{
		type: "column",
		yValueFormatString: "#,### Units",
		dataPoints: dataPoints
	}]
});


#$.getJSON("https://canvasjs.com/data/gallery/javascript/daily-sales.json?callback=?", callback);	

return jsonify(all_samples)

}

    function all_samples(data){
        for (var i = 0; i < data.dps.length; i++){
            dataPoints.push({
                x: new Generation(data.dps[i].Generation),
                y: data.dps[i].Total
            });
        }
    chart.render();
    }
"""@app.route("/samples/<Number>")
def samp(Number):
    
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
    return jsonify(data)"""

if __name__ == "__main__":
    app.run()