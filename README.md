
## Summary
The application deployed in Heroku (and running locally) uses Auth0 authentication and RBAC to allow Create, Read, Update, Delete (CRUD) operations on movies and actors.

## Getting Starting

### 1. Installing all dependencies, setting the environment variables and running the server locally
1. Install python version 3.10.4 from https://www.python.org/downloads/release/python-3104/.
2. #### Create the virtual environment called "my_env":
   python3.10 -m venv my_venv
3. #### Activate the virtual environment :
   source my_venv/bin/activate
4. #### Install dependencies:
   python3.10 -m pip install -r requirements.txt
5. #### Run setup.sh to run the server locally:
   ./setup.sh <br/> <br />
   setup.sh should excute environment variables (DATABASE_URL, AUTH0_DOMAIN, API_AUDIENCE, CLIENT_SECRET, PASSWORD).
6. #### Run flask server inside virtual environment
   python3.10 -m flask run <br/> <br/>
   The flask server will start on http://localhost:5000
7. #### For running unit tests, Open another terminal and run this command where the app.py is located
   python -m unittest test_app.py
  

### 2. Setup Authentication, authorization, RBAC

1. register on auth0 account through using https://auth0.com/.
2. Create custom APIs called "movie-agency-app".
3. #### Add these permissions to the APIs - 
   - create:actor
   - delete:actor
   - read:actor
   - update:actor
   - create:movie
   - read:movie
   - delete:movie
   - update:movie
   
4. Create the test application called "movie-agency-app". Then, Go to advanced settings section of the application and enable grant type as password.
5. #### Create following roles with the correct permissions </b>
   - assistant (read:actor, read:movie)</b>
   - director (create:actor, read:actor, delete:actor, update:actor, create:movie, read:movie, update:movie)</b>
   - producer (create:actor, read:actor, delete:actor, update:actor, create:movie, read:movie, delete:movie, update:movie)</b>
5. #### Under User Management  click on Users, Then Create following users users:</b>
   - assistant@example.com to assitant role.</b>
   - director@cexample.com to director role.</b>
   - producer@cexample.com to producer role.</b>



### 3. Heroku

1. Register for Herko account by going to https://www.heroku.com/.</b>
2. #### Install git and run following commands to push application code to Heroku.</b>
   - git init </b>
   - login to heroku </b>
   - git commit -m "your comment" </b>
   - git push heroku </b>

You can use `heroku config` to see the configuration and `heroku logs` to see the logs of deployment.
The application is hosted on https://movie-agency-app.herokuapp.com

### 4. API documentation

#### - Get casting assistant token 

- Sample Request:
```
curl --location --request POST 'https://dev-0b4j5xak.us.auth0.com/oauth/token' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlcxTFhvZzVVdEpYVG9DRTJJTG02YiJ9.eyJpc3MiOiJodHRwczovL2Rldi0wYjRqNXhhay51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI1ZjNmYzNiYzA4MDQwMDY5Yjg3YzVkIiwiYXVkIjoibW92aWUtYWdlbmN5LWFwcCIsImlhdCI6MTY1MDQxMTkxMywiZXhwIjoxNjUwNDk4MzEzLCJhenAiOiJCSkxGUTY0bEQ4MTBoeXkyNWdWYjltNmFlS1dnekM3TiIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsicmVhZDphY3RvciIsInJlYWQ6bW92aWUiXX0.g7WF9JNHciiibSFEztDdHNXCY6edJaWzrlA2_RRcRnwGe3Fq6Jny9XuAmHYINsYIibfxzrRbcPNNvOwqGi4UAAau0E72EHjd_ZUTKx1lMtlyJ62FNDVCbEHHbmQrp1defi28T6pOh6mRJKJdmiaf2OBm2RlQl-6aNbLnIx8NM_JgSMi_MAOeSnx3ZQ2PVpLGW7SE0gm7JW2BYTD--xn1Pn_xBn72Jprq1Dauel2XnN7QCu7u6b2n8sM3C8e78eYj5Dx1ypWXpMJxRjLevrgEL-Fpyiar8CS1zt2BMBJtwjFtwjp1V-G1RjAdz2u8D0tr4nduvBtMScVkUq_jhiUKKA' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: did=s%3Av0%3A09a52e70-c036-11ec-b8c1-49f8eba26cf3.AvMB5s%2BQ11KLj9UpaMyJE7iL1g5tYxVO3T0anHjKCf0; did_compat=s%3Av0%3A09a52e70-c036-11ec-b8c1-49f8eba26cf3.AvMB5s%2BQ11KLj9UpaMyJE7iL1g5tYxVO3T0anHjKCf0' \
--data-urlencode 'client_id=BJLFQ64lD810hyy25gVb9m6aeKWgzC7N' \
--data-urlencode 'username=assistant@example.com' \
--data-urlencode 'audience=movie-agency-app' \
--data-urlencode 'grant_type=password' \
--data-urlencode 'password=gL7TO01jLlyR' \
--data-urlencode 'client_secret=Bj9EZz-sHhK4eN7RapdlJCWDBapv-U3KT4pH6wDiFQv5k60CGGvvwGfuMewCmXVq'
```

- Sample Response:
```
{
    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlcxTFhvZzVVdEpYVG9DRTJJTG02YiJ9.eyJpc3MiOiJodHRwczovL2Rldi0wYjRqNXhhay51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI1ZjNmYzNiYzA4MDQwMDY5Yjg3YzVkIiwiYXVkIjoibW92aWUtYWdlbmN5LWFwcCIsImlhdCI6MTY1MDQ5ODEyMywiZXhwIjoxNjUwNTg0NTIzLCJhenAiOiJCSkxGUTY0bEQ4MTBoeXkyNWdWYjltNmFlS1dnekM3TiIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsicmVhZDphY3RvciIsInJlYWQ6bW92aWUiXX0.yS5OCGIa3l3oNJAAj-BbKhrCc8Ruc4bGkGQLI9l7yGX1Lkp_DNTnYye40N0AH9pk0dQi5P4FjzPsS82lLy6HQbfZR9-zTUV98MLqxlhRFJlOcb9uLm19pw0WYn7wDqINBY2P2Cc3FsAvecJq5REA07Z-6U3ULY45m5_RWjGuik1LFNRdZCUgw44g-udyt0fLMfmroyZDrK-ZWCNhaghja6C9l5xHgY8lkTWf835uTEaSsJDGa7b3DfNmoaLxlu7oFnkB73R-YBicBOYh_dNpNXGw4uMuuWan7ZLJdwD7gT7bYJeszcbMVU8Je3_0BzFswiBsuPoreYM-HMEspD4NbQ",
    "expires_in": 86400,
    "token_type": "Bearer"
}
```
The same can be repeated for getting director and producer tokens. The application can be tested for each role and what they are authorized to do.

#### 1. Create actor:
- Creates an actor based on the parameters in the body. The First and Last name must be unique. 200 for success. Sample CURL -

```
curl --location --request POST 'https://movie-agency-app.herokuapp.com/api/actor' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlcxTFhvZzVVdEpYVG9DRTJJTG02YiJ9.eyJpc3MiOiJodHRwczovL2Rldi0wYjRqNXhhay51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI1ZjQwMTViYzA4MDQwMDY5Yjg3Yzc4IiwiYXVkIjoibW92aWUtYWdlbmN5LWFwcCIsImlhdCI6MTY1MDY0NDA4MiwiZXhwIjoxNjUwNzMwNDgyLCJhenAiOiJCSkxGUTY0bEQ4MTBoeXkyNWdWYjltNmFlS1dnekM3TiIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmFjdG9yIiwiY3JlYXRlOm1vdmllIiwiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwicmVhZDphY3RvciIsInJlYWQ6bW92aWUiLCJ1cGRhdGU6YWN0b3IiLCJ1cGRhdGU6bW92aWUiXX0.STsvy-MyltIjwhaGyxoDvknKTlIKEVYnBbd14c29FSCWjGDzrZ4SPT5-HEgFnlzaJuoXsVPRlymiI_6JtbB9K0BMRA_3DkMYSX_GVCqUt-7ZW6clK1sFV-Y1kLndiwfbTj0YD5lfINd_F7aKT-qxVxYcwSibnVzYZpBN_5vTLKG3bMBl81j6BIKnd1KWkRF4lTJSUkXhVVa9R2r-Mk9qOE8OW1eY-XsmCCjrfSpXBd8mxSCxce8ZsEDfRBfQvt_HpIN_q6IJric0zoAjZt_TpamlzvAD0VyF8JsEohNcNZLuXsU98v9Vo6XwhkVoyReW_jk67MISl5QXkDkH4d95cQ' \
--header 'Content-Type: application/json' \
--data-raw '{
    "firstName": "Bob",
    "lastName": "Kirkwood",
    "sex": "Male",
    "age": 45,
    "city": "New York"
}'
```

- Sample Response:
```
{
    "actorId": 4,
    "age": 45,
    "city": "New York",
    "firstName": "Bob",
    "lastName": "Kirkwood",
    "portfolio": [],
    "sex": "Male"
}
```


#### 2. Update actor:
- Update actor by passing its details.Sample CURL

```
curl --location --request PATCH 'https://movie-agency-app.herokuapp.com/api/actor/2' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlcxTFhvZzVVdEpYVG9DRTJJTG02YiJ9.eyJpc3MiOiJodHRwczovL2Rldi0wYjRqNXhhay51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI1ZjQwMTViYzA4MDQwMDY5Yjg3Yzc4IiwiYXVkIjoibW92aWUtYWdlbmN5LWFwcCIsImlhdCI6MTY1MDY0NDA4MiwiZXhwIjoxNjUwNzMwNDgyLCJhenAiOiJCSkxGUTY0bEQ4MTBoeXkyNWdWYjltNmFlS1dnekM3TiIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmFjdG9yIiwiY3JlYXRlOm1vdmllIiwiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwicmVhZDphY3RvciIsInJlYWQ6bW92aWUiLCJ1cGRhdGU6YWN0b3IiLCJ1cGRhdGU6bW92aWUiXX0.STsvy-MyltIjwhaGyxoDvknKTlIKEVYnBbd14c29FSCWjGDzrZ4SPT5-HEgFnlzaJuoXsVPRlymiI_6JtbB9K0BMRA_3DkMYSX_GVCqUt-7ZW6clK1sFV-Y1kLndiwfbTj0YD5lfINd_F7aKT-qxVxYcwSibnVzYZpBN_5vTLKG3bMBl81j6BIKnd1KWkRF4lTJSUkXhVVa9R2r-Mk9qOE8OW1eY-XsmCCjrfSpXBd8mxSCxce8ZsEDfRBfQvt_HpIN_q6IJric0zoAjZt_TpamlzvAD0VyF8JsEohNcNZLuXsU98v9Vo6XwhkVoyReW_jk67MISl5QXkDkH4d95cQ' \
--header 'Content-Type: application/json' \
--data-raw '{
    "firstName": "Johnny",
    "lastName": "Depp",
    "sex": "Male",
    "age": 48,
    "city": "New York"
}'
```

- Sample Response
```
{
    "actor": {
        "actorId": 2,
        "age": 48,
        "city": "New York",
        "firstName": "Johnny",
        "lastName": "Depp",
        "portfolio": [],
        "sex": "Male"
    },
    "Result": "Actor is updated."
}
```


#### 3. DELETE actor
- Delete an actor by specify id. Sample CURL

```
curl --location --request DELETE 'https://movie-agency-app.herokuapp.com/api/actor/3' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlcxTFhvZzVVdEpYVG9DRTJJTG02YiJ9.eyJpc3MiOiJodHRwczovL2Rldi0wYjRqNXhhay51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI1ZjNmZmQ5YjM2NzQwMDcwMWZhY2U0IiwiYXVkIjoibW92aWUtYWdlbmN5LWFwcCIsImlhdCI6MTY1MDQ5ODM1MywiZXhwIjoxNjUwNTg0NzUzLCJhenAiOiJCSkxGUTY0bEQ4MTBoeXkyNWdWYjltNmFlS1dnekM3TiIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmFjdG9yIiwiY3JlYXRlOm1vdmllIiwiZGVsZXRlOmFjdG9yIiwicmVhZDphY3RvciIsInJlYWQ6bW92aWUiLCJ1cGRhdGU6YWN0b3IiXX0.XqicyJ-jgxDgmptxLb0buzXOHRTatwse1WWLSWJTL39bqILQqqbxfDwhl3nAt-UYUxEe4qy50gs-P0UHKtexWA_OCozE3BW-k9eYbxJytriYB1JORIMxygkX3uGUuJEvxMYIi-hCijY680Yx_iQIFFKmXL8k2VU5g5BpTzX6AtyzozzIznPf-WB6CjoMWqUyXYv25vDSBtD1Br2CVSSfqGlletWnCbKJto6y6kmQYauJxtiX9EmHLN5EEcTcYbSHpfPE5zw0bHHB7kFWrKMe4y8Lex37KeCc0vITl91w54FqSGesOUn_PYZdboGiJ0jygDonGxb4iMDcGzCdU0zJEw'
```

- Sample Response
```
{
    "Result": "Actor is deleted."
}
```

#### 4. GET actor
- Get actor. Sample CURL

```
curl --location --request GET 'https://movie-agency-app.herokuapp.com/api/actor/1' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlcxTFhvZzVVdEpYVG9DRTJJTG02YiJ9.eyJpc3MiOiJodHRwczovL2Rldi0wYjRqNXhhay51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI1ZjQwMTViYzA4MDQwMDY5Yjg3Yzc4IiwiYXVkIjoibW92aWUtYWdlbmN5LWFwcCIsImlhdCI6MTY1MDY0NDA4MiwiZXhwIjoxNjUwNzMwNDgyLCJhenAiOiJCSkxGUTY0bEQ4MTBoeXkyNWdWYjltNmFlS1dnekM3TiIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmFjdG9yIiwiY3JlYXRlOm1vdmllIiwiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwicmVhZDphY3RvciIsInJlYWQ6bW92aWUiLCJ1cGRhdGU6YWN0b3IiLCJ1cGRhdGU6bW92aWUiXX0.STsvy-MyltIjwhaGyxoDvknKTlIKEVYnBbd14c29FSCWjGDzrZ4SPT5-HEgFnlzaJuoXsVPRlymiI_6JtbB9K0BMRA_3DkMYSX_GVCqUt-7ZW6clK1sFV-Y1kLndiwfbTj0YD5lfINd_F7aKT-qxVxYcwSibnVzYZpBN_5vTLKG3bMBl81j6BIKnd1KWkRF4lTJSUkXhVVa9R2r-Mk9qOE8OW1eY-XsmCCjrfSpXBd8mxSCxce8ZsEDfRBfQvt_HpIN_q6IJric0zoAjZt_TpamlzvAD0VyF8JsEohNcNZLuXsU98v9Vo6XwhkVoyReW_jk67MISl5QXkDkH4d95cQ'
```

- Sample Response:
```
{
    "actorId": 1,
    "age": 60,
    "city": "Los Angeles",
    "firstName": "Jack",
    "lastName": "Nicholson",
    "portfolio": [],
    "sex": "Male"
}
```

#### 5. GET all actors
- Get all actors. Sample CURL

```
curl --location --request GET 'https://movie-agency-app.herokuapp.com/api/actor' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlcxTFhvZzVVdEpYVG9DRTJJTG02YiJ9.eyJpc3MiOiJodHRwczovL2Rldi0wYjRqNXhhay51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI1ZjQwMTViYzA4MDQwMDY5Yjg3Yzc4IiwiYXVkIjoibW92aWUtYWdlbmN5LWFwcCIsImlhdCI6MTY1MDY0NDA4MiwiZXhwIjoxNjUwNzMwNDgyLCJhenAiOiJCSkxGUTY0bEQ4MTBoeXkyNWdWYjltNmFlS1dnekM3TiIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmFjdG9yIiwiY3JlYXRlOm1vdmllIiwiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwicmVhZDphY3RvciIsInJlYWQ6bW92aWUiLCJ1cGRhdGU6YWN0b3IiLCJ1cGRhdGU6bW92aWUiXX0.STsvy-MyltIjwhaGyxoDvknKTlIKEVYnBbd14c29FSCWjGDzrZ4SPT5-HEgFnlzaJuoXsVPRlymiI_6JtbB9K0BMRA_3DkMYSX_GVCqUt-7ZW6clK1sFV-Y1kLndiwfbTj0YD5lfINd_F7aKT-qxVxYcwSibnVzYZpBN_5vTLKG3bMBl81j6BIKnd1KWkRF4lTJSUkXhVVa9R2r-Mk9qOE8OW1eY-XsmCCjrfSpXBd8mxSCxce8ZsEDfRBfQvt_HpIN_q6IJric0zoAjZt_TpamlzvAD0VyF8JsEohNcNZLuXsU98v9Vo6XwhkVoyReW_jk67MISl5QXkDkH4d95cQ'
```

- Sample Response:
```
{
    "actors": [
        {
            "actorId": 1,
            "age": 60,
            "city": "Los Angeles",
            "firstName": "Jack",
            "lastName": "Nicholson",
            "portfolio": [],
            "sex": "Male"
        },
        {
            "actorId": 3,
            "age": 45,
            "city": "New York",
            "firstName": "Angelina",
            "lastName": "Jolie",
            "portfolio": [],
            "sex": "Female"
        },
        {
            "actorId": 2,
            "age": 48,
            "city": "New York",
            "firstName": "Johnny",
            "lastName": "Depp",
            "portfolio": [],
            "sex": "Male"
        }
    ]
}
```


#### 6. Create movie
- Create movie by adding its details in the body. Sample CURL

```
curl --location --request POST 'https://movie-agency-app.herokuapp.com/api/movie' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlcxTFhvZzVVdEpYVG9DRTJJTG02YiJ9.eyJpc3MiOiJodHRwczovL2Rldi0wYjRqNXhhay51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI1ZjQwMTViYzA4MDQwMDY5Yjg3Yzc4IiwiYXVkIjoibW92aWUtYWdlbmN5LWFwcCIsImlhdCI6MTY1MDY0NDA4MiwiZXhwIjoxNjUwNzMwNDgyLCJhenAiOiJCSkxGUTY0bEQ4MTBoeXkyNWdWYjltNmFlS1dnekM3TiIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmFjdG9yIiwiY3JlYXRlOm1vdmllIiwiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwicmVhZDphY3RvciIsInJlYWQ6bW92aWUiLCJ1cGRhdGU6YWN0b3IiLCJ1cGRhdGU6bW92aWUiXX0.STsvy-MyltIjwhaGyxoDvknKTlIKEVYnBbd14c29FSCWjGDzrZ4SPT5-HEgFnlzaJuoXsVPRlymiI_6JtbB9K0BMRA_3DkMYSX_GVCqUt-7ZW6clK1sFV-Y1kLndiwfbTj0YD5lfINd_F7aKT-qxVxYcwSibnVzYZpBN_5vTLKG3bMBl81j6BIKnd1KWkRF4lTJSUkXhVVa9R2r-Mk9qOE8OW1eY-XsmCCjrfSpXBd8mxSCxce8ZsEDfRBfQvt_HpIN_q6IJric0zoAjZt_TpamlzvAD0VyF8JsEohNcNZLuXsU98v9Vo6XwhkVoyReW_jk67MISl5QXkDkH4d95cQ' \
--header 'Content-Type: application/json' \
--data-raw '{
    "movieName": "Test",
    "category": "Horror",
    "releaseDate": "1885-01-11"
}'
```

- Sample response
```
{
    "Result": "Movie is created."
}
```


#### 7. Create actor portfolio -
- Create actor's portfolio by linking movies to specific actor. Sample CURL
```
curl --location --request POST 'https://movie-agency-app.herokuapp.com/api/actor/1/movie/3' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlcxTFhvZzVVdEpYVG9DRTJJTG02YiJ9.eyJpc3MiOiJodHRwczovL2Rldi0wYjRqNXhhay51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI1ZjQwMTViYzA4MDQwMDY5Yjg3Yzc4IiwiYXVkIjoibW92aWUtYWdlbmN5LWFwcCIsImlhdCI6MTY1MDY0NDA4MiwiZXhwIjoxNjUwNzMwNDgyLCJhenAiOiJCSkxGUTY0bEQ4MTBoeXkyNWdWYjltNmFlS1dnekM3TiIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmFjdG9yIiwiY3JlYXRlOm1vdmllIiwiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwicmVhZDphY3RvciIsInJlYWQ6bW92aWUiLCJ1cGRhdGU6YWN0b3IiLCJ1cGRhdGU6bW92aWUiXX0.STsvy-MyltIjwhaGyxoDvknKTlIKEVYnBbd14c29FSCWjGDzrZ4SPT5-HEgFnlzaJuoXsVPRlymiI_6JtbB9K0BMRA_3DkMYSX_GVCqUt-7ZW6clK1sFV-Y1kLndiwfbTj0YD5lfINd_F7aKT-qxVxYcwSibnVzYZpBN_5vTLKG3bMBl81j6BIKnd1KWkRF4lTJSUkXhVVa9R2r-Mk9qOE8OW1eY-XsmCCjrfSpXBd8mxSCxce8ZsEDfRBfQvt_HpIN_q6IJric0zoAjZt_TpamlzvAD0VyF8JsEohNcNZLuXsU98v9Vo6XwhkVoyReW_jk67MISl5QXkDkH4d95cQ'
``` 
- Sample Response -
```
{
    "Result": "Actor portfolio created successfuly."
}
```

#### 8. Update movie
- Update movie by specifying the corresponding id and the details. Sample CURL -

```
curl --location --request PATCH 'https://movie-agency-app.herokuapp.com/api/movie/3' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlcxTFhvZzVVdEpYVG9DRTJJTG02YiJ9.eyJpc3MiOiJodHRwczovL2Rldi0wYjRqNXhhay51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI1ZjQwMTViYzA4MDQwMDY5Yjg3Yzc4IiwiYXVkIjoibW92aWUtYWdlbmN5LWFwcCIsImlhdCI6MTY1MDY0NDA4MiwiZXhwIjoxNjUwNzMwNDgyLCJhenAiOiJCSkxGUTY0bEQ4MTBoeXkyNWdWYjltNmFlS1dnekM3TiIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmFjdG9yIiwiY3JlYXRlOm1vdmllIiwiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwicmVhZDphY3RvciIsInJlYWQ6bW92aWUiLCJ1cGRhdGU6YWN0b3IiLCJ1cGRhdGU6bW92aWUiXX0.STsvy-MyltIjwhaGyxoDvknKTlIKEVYnBbd14c29FSCWjGDzrZ4SPT5-HEgFnlzaJuoXsVPRlymiI_6JtbB9K0BMRA_3DkMYSX_GVCqUt-7ZW6clK1sFV-Y1kLndiwfbTj0YD5lfINd_F7aKT-qxVxYcwSibnVzYZpBN_5vTLKG3bMBl81j6BIKnd1KWkRF4lTJSUkXhVVa9R2r-Mk9qOE8OW1eY-XsmCCjrfSpXBd8mxSCxce8ZsEDfRBfQvt_HpIN_q6IJric0zoAjZt_TpamlzvAD0VyF8JsEohNcNZLuXsU98v9Vo6XwhkVoyReW_jk67MISl5QXkDkH4d95cQ' \
--header 'Content-Type: application/json' \
--data-raw '{
    "category": "Thriller",
    "releaseDate": "1977-01-01",
    "movieName": "The Shining"
}'
```

- Sample Response
```
{
    "movie": {
        "category": "Thriller",
        "movie_id": 3,
        "movieName": "The Shining",
        "release_date": "Sat, 01 Jan 1977 00:00:00 GMT"
    },
    "Result": "Movie is updated."
}
```

#### 9. DELETE movie
- Delete a movie. Sample CURL -

```
curl --location --request DELETE 'https://movie-agency-app.herokuapp.com/api/movie/5' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlcxTFhvZzVVdEpYVG9DRTJJTG02YiJ9.eyJpc3MiOiJodHRwczovL2Rldi0wYjRqNXhhay51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI1ZjQwMTViYzA4MDQwMDY5Yjg3Yzc4IiwiYXVkIjoibW92aWUtYWdlbmN5LWFwcCIsImlhdCI6MTY1MDY0NDA4MiwiZXhwIjoxNjUwNzMwNDgyLCJhenAiOiJCSkxGUTY0bEQ4MTBoeXkyNWdWYjltNmFlS1dnekM3TiIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmFjdG9yIiwiY3JlYXRlOm1vdmllIiwiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwicmVhZDphY3RvciIsInJlYWQ6bW92aWUiLCJ1cGRhdGU6YWN0b3IiLCJ1cGRhdGU6bW92aWUiXX0.STsvy-MyltIjwhaGyxoDvknKTlIKEVYnBbd14c29FSCWjGDzrZ4SPT5-HEgFnlzaJuoXsVPRlymiI_6JtbB9K0BMRA_3DkMYSX_GVCqUt-7ZW6clK1sFV-Y1kLndiwfbTj0YD5lfINd_F7aKT-qxVxYcwSibnVzYZpBN_5vTLKG3bMBl81j6BIKnd1KWkRF4lTJSUkXhVVa9R2r-Mk9qOE8OW1eY-XsmCCjrfSpXBd8mxSCxce8ZsEDfRBfQvt_HpIN_q6IJric0zoAjZt_TpamlzvAD0VyF8JsEohNcNZLuXsU98v9Vo6XwhkVoyReW_jk67MISl5QXkDkH4d95cQ'
```

- Sample response
```
{
    "Result": "Movie is deleted."
}
```

#### 10. GET the movie by id.
- Get movie by id. Sample CURL -

```
curl --location --request GET 'https://movie-agency-app.herokuapp.com/api/movie/1' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlcxTFhvZzVVdEpYVG9DRTJJTG02YiJ9.eyJpc3MiOiJodHRwczovL2Rldi0wYjRqNXhhay51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI1ZjQwMTViYzA4MDQwMDY5Yjg3Yzc4IiwiYXVkIjoibW92aWUtYWdlbmN5LWFwcCIsImlhdCI6MTY1MDY0NDA4MiwiZXhwIjoxNjUwNzMwNDgyLCJhenAiOiJCSkxGUTY0bEQ4MTBoeXkyNWdWYjltNmFlS1dnekM3TiIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmFjdG9yIiwiY3JlYXRlOm1vdmllIiwiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwicmVhZDphY3RvciIsInJlYWQ6bW92aWUiLCJ1cGRhdGU6YWN0b3IiLCJ1cGRhdGU6bW92aWUiXX0.STsvy-MyltIjwhaGyxoDvknKTlIKEVYnBbd14c29FSCWjGDzrZ4SPT5-HEgFnlzaJuoXsVPRlymiI_6JtbB9K0BMRA_3DkMYSX_GVCqUt-7ZW6clK1sFV-Y1kLndiwfbTj0YD5lfINd_F7aKT-qxVxYcwSibnVzYZpBN_5vTLKG3bMBl81j6BIKnd1KWkRF4lTJSUkXhVVa9R2r-Mk9qOE8OW1eY-XsmCCjrfSpXBd8mxSCxce8ZsEDfRBfQvt_HpIN_q6IJric0zoAjZt_TpamlzvAD0VyF8JsEohNcNZLuXsU98v9Vo6XwhkVoyReW_jk67MISl5QXkDkH4d95cQ'
```

- Sample Response
```
{
    "category": "Action",
    "movie_id": 1,
    "movieName": "Pirates of the Caribbean",
    "release_date": "Fri, 15 Feb 2008 00:00:00 GMT"
}
```

#### 11. GET all movies -
- Get all movies. Sample CURL -

```
curl --location --request GET 'https://movie-agency-app.herokuapp.com/api/movie' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlcxTFhvZzVVdEpYVG9DRTJJTG02YiJ9.eyJpc3MiOiJodHRwczovL2Rldi0wYjRqNXhhay51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI1ZjQwMTViYzA4MDQwMDY5Yjg3Yzc4IiwiYXVkIjoibW92aWUtYWdlbmN5LWFwcCIsImlhdCI6MTY1MDY0NDA4MiwiZXhwIjoxNjUwNzMwNDgyLCJhenAiOiJCSkxGUTY0bEQ4MTBoeXkyNWdWYjltNmFlS1dnekM3TiIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmFjdG9yIiwiY3JlYXRlOm1vdmllIiwiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwicmVhZDphY3RvciIsInJlYWQ6bW92aWUiLCJ1cGRhdGU6YWN0b3IiLCJ1cGRhdGU6bW92aWUiXX0.STsvy-MyltIjwhaGyxoDvknKTlIKEVYnBbd14c29FSCWjGDzrZ4SPT5-HEgFnlzaJuoXsVPRlymiI_6JtbB9K0BMRA_3DkMYSX_GVCqUt-7ZW6clK1sFV-Y1kLndiwfbTj0YD5lfINd_F7aKT-qxVxYcwSibnVzYZpBN_5vTLKG3bMBl81j6BIKnd1KWkRF4lTJSUkXhVVa9R2r-Mk9qOE8OW1eY-XsmCCjrfSpXBd8mxSCxce8ZsEDfRBfQvt_HpIN_q6IJric0zoAjZt_TpamlzvAD0VyF8JsEohNcNZLuXsU98v9Vo6XwhkVoyReW_jk67MISl5QXkDkH4d95cQ'
```

- Sample response
```
{
    "movies": [
        {
            "category": "Action",
            "movie_id": 1,
            "movieName": "Pirates of the Caribbean",
            "release_date": "Fri, 15 Feb 2008 00:00:00 GMT"
        },
        {
            "category": "Thriller",
            "movie_id": 3,
            "movieName": "The Shining",
            "release_date": "Sat, 01 Jan 1977 00:00:00 GMT"
        }
    ]
}
```
