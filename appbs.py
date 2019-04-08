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

# Create our database model
class Pokemon(db.Model):
    __tablename__ = 'stats'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    name = db.Column(db.String)
    type_1 = db.Column(db.String)
    type_2 = db.Column(db.String)
    total = db.Column(db.Integer)
    hp = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    defense = db.Column(db.Integer)
    sp_atk = db.Column(db.Integer)
    sp_def = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    generation = db.Column(db.Integer)
    islegendary = db.Column(db.String)
    color = db.Column(db.String)
    hasgender = db.Column(db.String)
    pr_male = db.Column(db.Float)
    egg_group_1 = db.Column(db.String)
    egg_group_2 = db.Column(db.String)
    hasmegaevolution = db.Column(db.String)
    height_m = db.Column(db.Float)
    weight_kg = db.Column(db.Float)
    catch_rate = db.Column(db.Integer)
    body_style = db.Column(db.String)

    def __repr__(self):
        return '<Pokemon %r>' % (self.name)

@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()

@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")

@app.route("/type_total")
def type_data():
    """Return pokemon type and pokemon total"""
    
    # Query for the data
    results = db.session.query(stats.type_1, stats.total).\
        group_by(stats.type_1).order_by(stats.type_1.asc()).all()
    
    # Create lists from the query results
    pokemon_type = [result[0] for result in results]
    total_score = [int(result[1]) for result in results]

    # Generate the plot trace
    trace = {
        "x": pokemon_type,
        "y": total_score,
        "type": "bar"
    }
    return jsonify(trace)
    


if __name__ == "__main__":
    app.run()