import os
from sqlalchemy import Column, String, create_engine, DateTime, Date, Integer, cast
from flask_sqlalchemy import SQLAlchemy
import json

database_path = os.environ['DATABASE_URL']
if database_path.startswith("postgres://"):
  database_path = database_path.replace("postgres://", "postgresql://", 1)

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()



movie_actor = db.Table("Movie_Actor",
    db.Column('movieId', db.Integer, db.ForeignKey('Movie.movieId')),
    db.Column('actorId', db.Integer, db.ForeignKey('Actor.actorId'))
)



