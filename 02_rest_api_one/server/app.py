#!/usr/bin/env python3

from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate 
from models import db, Production


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

migrate = Migrate(app, db)

db.init_app(app)

# | HTTP Verb 	|       Path       	| Description        	|
# |-----------	|:----------------:	|--------------------	|
# | GET       	|   /productions   	| READ all resources 	|
# | GET       	| /productions/:id 	| READ one resource   	|
# | POST      	|   /productions   	| CREATE one resource 	|
# | PATCH/PUT 	| /productions/:id 	| UPDATE one resource	|
# | DELETE    	| /productions/:id 	| DESTROY one resource 	|

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1. Create a route to /productions for GET requests
    # 1a. Create the query
    # 1b. Loop through the query and convert each object into a dictionary 
    # 1c. Use make_response and jsonify to return a response
    # 1d. Test in Postman

        # 5c. use SerializerMixin's .to_dict() for responses here and everywhere

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 3. Create a route to /productions for a POST request
        # 3a. Get information from request.get_json() 
        # 3b. Create new object
        # 3c. Add and commit to db 
        # 3d. Convert to dictionary / # 5c. use .to_dict
        # 3e. return as JSON
        # 3f. Test in postman

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 2. Create a route to /productions/:id for single GET requests

        # 5c. use to_dict

    # 4. Create a delete request 


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 5. Serializers: navigate back to models.py 

if __name__ == '__main__':
    app.run(port=5555, debug=True)