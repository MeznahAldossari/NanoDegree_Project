import http.client
import json
import os
import random
import string
import unittest
import warnings
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db
from actor import Actor
from movie import Movie



class MovieAgency(unittest.TestCase):
    PRODUCER_TOKEN = ""

    
    def init_tokens(self):
        domain = os.environ.get('AUTH0_DOMAIN')
        cli_secret = os.environ.get('CLIENT_SECRET')
        my_pass = os.environ.get('PASSWORD')
        my_connection = http.client.HTTPSConnection(domain)
        payload = 'client_id=BJLFQ64lD810hyy25gVb9m6aeKWgzC7N&username=producer@example.com&audience=movie-agency-app&grant_type=password&password=' + my_pass + '&client_secret=' + cli_secret
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        my_connection.request("POST", "/oauth/token", payload, headers)
        Results = my_connection.getresponse()
        data = Results.read()
        data = json.loads(data.decode())
        self.PRODUCER_TOKEN = data['access_token']


    def setUp(self):
        warnings.simplefilter('ignore', category=ResourceWarning)
        warnings.simplefilter('ignore', category=DeprecationWarning)
        self.init_tokens()
        self.app = create_app()
        self.client = self.app.test_client

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_actors_success(self):
        Result = self.client().get("/api/actor", headers={'Authorization': 'Bearer ' + self.PRODUCER_TOKEN})
        data = json.loads(Result.data)

        self.assertEqual(Result.status_code, 200)
        self.assertTrue(data["actors"])
        self.assertTrue(len(data["actors"]))
    
    def test_get_movies_success(self):
        Results = self.client().get("/api/movie", headers={'Authorization': 'Bearer ' + self.PRODUCER_TOKEN})
        data = json.loads(Results.data)
        self.assertEqual(Results.status_code, 200)
        self.assertTrue(data["movies"])
        self.assertTrue(len(data["movies"]))


    def test_get_movies_error(self):
        Results = self.client().get("/api/movie")
        data = json.loads(Results.data)
        self.assertEqual(Results.status_code, 401)

    def test_create_actor_success(self):
        sample = {
            "firstName": "Jennifer",
            "lastName": "Anniston",
            "sex": "Female",
            "age": 45,
            "city": "Los Angeles"
        }

        Results = self.client().post("/api/actor", json = sample, headers={'Authorization': 'Bearer ' + self.PRODUCER_TOKEN})
        data = json.loads(Results.data)
        self.assertEqual(Results.status_code, 200)
        self.assertEqual(data["Result"], "Actor is created")

    def test_delete_actor_success(self):
        Results = self.client().get("/api/actor", headers={'Authorization': 'Bearer ' + self.PRODUCER_TOKEN})
        data = json.loads(Results.data)

        for actor in data['actors']:
            if actor['firstName'] == 'Jennifer':
                actor_id = actor['actorId']

        Results = self.client().delete("/api/actor/" + str(actor_id), headers={'Authorization': 'Bearer ' + self.PRODUCER_TOKEN})
        data = json.loads(Results.data)

        self.assertEqual(Results.status_code, 200)
        self.assertEqual(data["Result"], "Actor is deleted")

    
    def test_get_actors_error(self):
        Results = self.client().get("/api/actor")
        data = json.loads(Results.data)
        self.assertEqual(Results.status_code, 401)

    def test_create_actor_error(self):
        sample = {
            "firstName": "Elisha",
            "lastName": "Cuthbert",
            "sex": "Female",
            "age": 32,
            "city": "Sydney"
        }

        Results = self.client().post("/api/actor", json = sample)
        data = json.loads(Results.data)
        self.assertEqual(Results.status_code, 401)

    def test_delete_actor_error(self):

        Results = self.client().delete("/api/actor/1", headers={'Authorization': 'Bearer '})
        data = json.loads(Results.data)
        self.assertEqual(Results.status_code, 401)

    
    def test_create_movie_success(self):
        sample = {
            "movieName": "Django Unchained1",
            "category": "Drama",
            "releaseDate": "2010-01-01"
        }

        Results = self.client().post("/api/movie", json = sample, headers={'Authorization': 'Bearer ' + self.PRODUCER_TOKEN})
        data = json.loads(Results.data)
        self.assertEqual(Results.status_code, 200)
        self.assertEqual(data["Result"], "Movie is created")

    def test_delete_movie_success(self):

        Results = self.client().get("/api/movie", headers={'Authorization': 'Bearer ' + self.PRODUCER_TOKEN})
        data = json.loads(Results.data)

        for movie in data['movies']:
            if movie['movieName'] == 'Django Unchained1':
                movie_id = movie['movieId']

        Results = self.client().delete("/api/movie/" + str(movie_id), headers={'Authorization': 'Bearer ' + self.PRODUCER_TOKEN})
        data = json.loads(Results.data)
        self.assertEqual(Results.status_code, 200)
        self.assertEqual(data["Result"], "Movie is deleted")


    def test_create_movie_nulltoken(self):
        sample = {
            "movie_name": "The Godfather",
            "category": "Drama",
            "releaseDate": "1985-07-11"
        }

        Results = self.client().post("/api/movie", json = sample, headers={'Authorization': 'Bearer '})
        data = json.loads(Results.data)

        self.assertEqual(Results.status_code, 401)

    def test_delete_movie_nulltoken(self):
        Results = self.client().delete("/api/movie/1", headers={'Authorization': 'Bearer '})
        data = json.loads(Results.data)
        self.assertEqual(Results.status_code, 401)



if __name__ == "__main__":
    unittest.main()