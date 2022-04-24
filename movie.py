from models import db
from sqlalchemy import Column, String, Integer, Date


class Movie(db.Model):
    __tablename__ = 'Movie'

    movieId = Column(Integer, primary_key=True)
    movieName = Column(String)
    category = Column(String)
    releaseDate = Column(String)
    db.UniqueConstraint(movieName, releaseDate)

    def __init__(self, movieName, category, releaseDate):
        self.movieName = movieName
        self.category = category
        self.releaseDate = releaseDate

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
    	    'movieId': self.movieId,
    	    'movieName': self.movieName,
    	    'category': self.category,
            'releaseDate': self.releaseDate
    	}
    

