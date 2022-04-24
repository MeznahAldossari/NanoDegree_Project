import os
from flask import Flask, request, abort, make_response, jsonify
from models import setup_db
from actor import Actor
from movie import Movie
from flask_cors import CORS
import json

from auth import requires_authentication, requires_permission, AuthenticationError

CREATE_ACTOR_PERMISSION = "create:actor"
READ_ACTOR_PERMISSION = "read:actor"
UPDATE_ACTOR_PERMISSION = "update:actor"
DELETE_ACTOR_PERMISSION = "delete:actor"

CREATE_MOVIE_PERMISSION = "create:movie"
READ_MOVIE_PERMISSION = "read:movie"
UPDATE_MOVIE_PERMISSION = "update:movie"
DELETE_MOVIE_PERMISSION = "delete:movie"


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/api/actor', methods=['POST'])
    @requires_authentication
    def create_new_actor(payload):
        if not requires_permission(CREATE_ACTOR_PERMISSION):
            raise AuthenticationError({"code": "Unauthorized"}, 403)

        getData = request.get_json()
        actor = Actor(fname=getData['firstName'],
                      lname=getData['lastName'],
                      sex=getData['sex'],
                      age=getData['age'],
                      city=getData['city'])
        actor.create()
        # return make_response(jsonify(new_actor.print()), 200)
        return make_response(jsonify({"Result": "Actor is created"}), 200)
    
    @app.route('/api/actor', methods=["GET"])
    @requires_authentication
    def get_actors(payload):
        if not requires_permission(READ_ACTOR_PERMISSION):
            raise AuthenticationError({"code": "Unauthorized"}, 403)

        
        actors = Actor.query.all()
        if actors is None:
            abort(404)
        listed = [actor.print() for actor in actors]
        return make_response(
            jsonify({"actors": listed
                    }), 200)
        
    
    @app.route('/api/actor/<int:actor_id>', methods=["GET"])
    @requires_authentication
    def get_actorbyID(payload, actor_id):
        if not requires_permission(READ_ACTOR_PERMISSION):
            raise AuthenticationError({"code": "Unauthorized"}, 403)
        actor=Actor.query.get(actor_id)
        if actor is None:
            abort(404)
        printing = actor.print()
        return make_response(jsonify(printing),200)
        
    
    @app.route('/api/actor/<int:actor_id>', methods=["PATCH"])
    @requires_authentication
    def update_specific_actor(payload, actor_id):
        if not requires_permission(UPDATE_ACTOR_PERMISSION):
            raise AuthenticationError({"code": "Unauthorized"}, 403)

        getData = request.get_json()
        actor=Actor.query.get(actor_id)
        if actor is None:
            abort(404)

        actor.nameFirst = getData.get('firstName')
        actor.nameLast = getData.get('lastName')
        actor.sex = getData.get('sex')
        actor.age = getData.get('age')
        actor.city = getData.get('city')
        actor.update()
        actor = Actor.query.get(actor_id)
        return make_response(jsonify({"Result": "Actor is updated"}), 200)
        

   

    @app.route('/api/actor/<int:actor_id>/movie/<int:movie_id>', methods=['POST'])
    @requires_authentication
    def create_actorportfolio(payload, actor_id, movie_id):
        if not requires_permission(UPDATE_ACTOR_PERMISSION):
            raise AuthenticationError({"code": "Unauthorized"}, 403)
        actor = Actor.query.get(actor_id)
        movie = Movie.query.get(movie_id)
        actor.portfolio.append(movie)
        actor.update()
        return make_response(jsonify({"Result": "Actor portfolio created successfully."}), 200)
    
    @app.route('/api/actor/<int:actor_id>', methods=["DELETE"])
    @requires_authentication
    def delete_actorbyID(payload, actor_id):
        if not requires_permission(DELETE_ACTOR_PERMISSION):
             raise AuthenticationError({"code": "Unauthorized"}, 403)

        actor=Actor.query.get(actor_id)
        if actor is None:
            abort(404)
        actor.delete()
        return make_response(jsonify({"Result": "Actor is deleted"}), 200)

       
    @app.route('/api/movie', methods=['POST'])
    @requires_authentication
    def create_new_movie(payload):
        if not requires_permission(CREATE_MOVIE_PERMISSION):
            raise AuthenticationError({"code": "Unauthorized"}, 403)
        getData = request.get_json()
        movie = Movie(movieName=getData['movieName'],
                      category=getData['category'],
                      releaseDate=getData['releaseDate'])
        movie.create()
        return make_response(jsonify({"Result": "Movie is created"}), 200)
        
    
    @app.route('/api/movie', methods=["GET"])
    @requires_authentication
    def get_movies(payload):
        if not requires_permission(READ_MOVIE_PERMISSION):
            raise AuthenticationError({"code": "Unauthorized"}, 403)
        movies = Movie.query.all()
        if movies is None:
            abort(404)
        listed = [movie.print() for movie in movies]
        return make_response(jsonify({
            "movies": listed
        }), 200)
        
    
    @app.route('/api/movie/<int:movie_id>', methods=["GET"])
    @requires_authentication
    def get_moviebyID(payload, movie_id):
        if not requires_permission(READ_MOVIE_PERMISSION):
            raise AuthenticationError({"code": "Unauthorized"}, 403)
        movie = Movie.query.get(movie_id)
        if movie is None:
            abort(404)
        printing = movie.print()
        return make_response(jsonify(printing),200)
    
    @app.route('/api/movie/<int:movie_id>', methods=["DELETE"])
    @requires_authentication
    def delete_moviebyID(payload, movie_id):
        if not requires_permission(DELETE_MOVIE_PERMISSION):
            raise AuthenticationError({"code": "Unauthorized"}, 403)
        movie = Movie.query.get(movie_id)
        if movie is None:
            abort(404)
        movie.delete()
        return make_response(jsonify({"Result": "Movie is deleted"}), 200)
        

    
    @app.route('/api/movie/<int:movie_id>', methods=["PATCH"])
    @requires_authentication
    def update_specific_movie(payload, movie_id):
        if not requires_permission(UPDATE_MOVIE_PERMISSION):
            raise AuthenticationError({"code": "Unauthorized"}, 403)
        getData = request.get_json()
        movie = Movie.query.get(movie_id)
        if movie is None:
            abort(404)

        movie.movieName = getData.get('movieName')
        movie.category = getData.get('category')
        movie.releaseDate = getData['releaseDate']
        movie.update()
        movie = Movie.query.get(movie_id)
        return make_response(jsonify({"Result": "Movie is updated"}), 200)
        

   
    @app.errorhandler(AuthenticationError)
    def handle_auth_error(error):
        response = jsonify(error.error)
        response.status_code = error.status_code
        return response

    return app



app = create_app()

if __name__ == '__main__':
    app.run()
