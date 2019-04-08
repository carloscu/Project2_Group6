import os
import sys

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)

#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_pokemon.db"
db = SQLAlchemy(app)

# print(db, file=sys.stderr)


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


@app.route("/catchrate")
def catchrate():
    """Return emoji score and emoji char"""

    # Query for the top 10 emoji data
    results = db.session.query(Pokemon.type_1, func.avg(Pokemon.catch_rate)).\
        group_by(Pokemon.type_1).order_by(Pokemon.total.desc()).all()
    

    # Create lists from the query results
    poke_type = [result[0] for result in results]
    catch = [int(result[1]) for result in results]

    # Generate the plot trace
    trace = {
        "x": poke_type,
        "y": catch,
        "type": "bar"
    }
    return jsonify(trace)


# attempt to do averages, looks bad
# @app.route("/catchrate")
# def catchrate():
#     """Return emoji score and emoji char"""

#     # Query for the top 10 emoji data
#     results = db.session.query_property(func.avg(Pokemon.catch_rate).label('average')).scalar().order_by(average.asc()).group_by(Pokemon.type_1).all()
#     # Create lists from the query results
#     poke_type = [result[0] for result in results]
#     catch = [int(result[1]) for result in results]

#     # Generate the plot trace
#     trace = {
#         "x": poke_type,
#         "y": catch,
#         "type": "bar"
#     }
#     return jsonify(trace)


@app.route("/type_total")
def type_total():
    """Return pokemon type and pokemon total"""
    
    # Query for the data
    results = db.session.query(Pokemon.type_1, func.avg(Pokemon.total)).\
        group_by(Pokemon.type_1).all()
    
    # Create lists from the query results
    pokemon_type = [result[0] for result in results]
    total_score = [int(result[1]) for result in results]

    # Generate the plot trace
    trace_type = {
        "x": pokemon_type,
        "y": total_score,
        "type": "bar",
        "barmode": "group"
    }
    return jsonify(trace_type)
    
# trying to make a grouped bar chart using the generations; started by just doing regular and group1, in case it didn't work and it isn't!
# @app.route("/type_total_gen")
# def type_total_gen():
#     """Return pokemon type and pokemon by generation total"""
    
#     # Query for the data
#     results = db.session.query(Pokemon.type_1, func.avg(Pokemon.total)).\
#         group_by(Pokemon.type_1).all()
    
#     # Create lists from the query results
#     pokemon_type = [result[0] for result in results]
#     total_score = [int(result[1]) for result in results]

#     # Generate the plot trace
#     trace_type = {
#         "x": pokemon_type,
#         "y": total_score,
#         "type": "bar"
#     }

#     # Query for the gen1data
#     gen1results = db.session.query(Pokemon.type_1, func.avg(Pokemon.total)).\
#         filter(Pokemon.generation==1).group_by(Pokemon.type_1).all()
#     g1pokemon_type = [result[0] for result in gen1results]
#     g1total_score = [int(result[1]) for result in gen1results]

#     g1trace_type = {
#         "x": g1pokemon_type,
#         "y": g1total_score,
#         "type": "bar",
#         "barmode": group
#     }
    
#     datavariable = [trace_type, g1trace_type]
#     return jsonify(datavariable)

@app.route("/pokemon_generation")
def pokemon_generation():
    """Pokemon total by generation"""

    # Query for data
    results = db.session.query(Pokemon.generation, func.avg(Pokemon.total)).\
        group_by(Pokemon.generation).order_by(Pokemon.generation.asc()).all()

    df = pd.DataFrame(results, columns=['generation', 'total_score'])

    # Format the data for Plotly
    plot_trace = {
        "x": df["generation"].values.tolist(),
        "y": df["total_score"].values.tolist(),
        "type": "bar"
    }
    return jsonify(plot_trace)

if __name__ == "__main__":
    app.run()

# trying to get the scatter to work
# @app.route("/catchbytotal")
# def catchbytotal():
#     """Catch Rate by Total"""

#     # Query for data
#     results = db.session.query(Pokemon.catch_rate, Pokemon.total, Pokemon.name).all()

#     pokemon_cr = [result[0] for result in results]
#     total_score = [int(result[1]) for result in results]
#     names = [result[2] for result in results]

#     # Format the data for Plotly
#     catch_trace = {
#         "x": pokemon_cr,
#         "y": total_score,
#         "labels": names,
#         "type": "scatter",
#         "mode": "markers"
#     }
    
#     return jsonify(catch_trace)

if __name__ == "__main__":
    app.run()