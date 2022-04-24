from models import db, movie_actor
from sqlalchemy import Column, String, Integer

class Actor(db.Model):
    __tablename__ = 'Actor'

    actorId = Column(db.Integer, primary_key=True)
    nameFirst = Column(String)
    nameLast = Column(String)
    sex = Column(String)
    age = Column(Integer)
    city = Column(String)
    portfolio = db.relationship('Movie', secondary=movie_actor)

    db.UniqueConstraint(nameFirst, nameLast)

    def __init__(self, fname, lname, sex, age, city):
        self.nameFirst = fname
        self.nameLast = lname
        self.sex = sex
        self.age = age
        self.city = city

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def print(self):
        return {
            'actorId': self.actorId,
            'firstName': self.nameFirst,
            'lastName': self.nameLast,
            'sex': self.sex,
            'age': self.age,
            'city': self.city,
            'portfolio': [movie.movieName for movie in self.portfolio]
        }