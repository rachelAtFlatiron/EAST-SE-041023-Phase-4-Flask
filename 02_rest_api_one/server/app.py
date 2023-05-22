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

# 1. Create a route to /productions for GET requests
    # 1a. Create the query
    # 1b. Loop through the query and convert each object into a dictionary 
    # 1c. Use make_response and jsonify to return a response
    # 1d. Test in Postman
@app.route('/productions', methods=["GET", "POST"])
# 🛑 emphasize this has to be a different class name than the model class
def Productions():
    if request.method == "GET":
        q = Production.query.all()

        # prods_list = []
        # for prod in q:
        #     prods_list.append({
        #         "title": prod.title,
        #         "genre": prod.genre,
        #         "length": prod.length
        #     })

        # 5c. use SerializerMixin's .to_dict() for responses here and everywhere
        prods_list = [p.to_dict() for p in q]

        return make_response(jsonify(prods_list), 200)

    # 3. Create a route to /productions for a POST request
    if request.method == "POST":
        # 3a. Get information from request.get_json() 
        # 🛑 review: request.args (key value pairs in query string)
        # 🛑 review: request.form (key value pairs in body from HTML post form)
        # 🛑 review: request.values (combines args, form)
        # 🛑 review: request.json (parsed json data)
            # 🛑 review: use request.get_json(force=True) to ignore content type
        data = request.get_json() # or request.json
        # 3b. Create new object
        prod = Production(
            # 🛑 review: request.__['key'] is for if you know key exists
            # 🛑 review: otherwise use request.__.get('key')
            title=data.get('title'),
            year=data.get('year'),
        )
        # 3c. Add and commit to db 
        db.session.add(prod)
        db.session.commit()

        # 3d. Convert to dictionary / # 5c. use .to_dict
        prod_dict = {
            "title": prod.title,
            "year": prod.year,
            "id": prod.id
        }
        # 3e. return as JSON
        return make_response(jsonify(prod_dict), 201)
        # 3f. Test in postman

# 2. Create a route to /productions/:id for single GET requests
@app.route('/productions/<int:id>', methods=["GET", "DELETE"])
def One_Production(id):
    if request.method == "GET":
        q = Production.query.filter_by(id=id).first()
        # 5c. use to_dict
        prod = {
            "title": q.title,
            "genre": q.genre,
            "director": q.director,
            "year": q.year
        }

        return make_response(jsonify(q.to_dict()), 200)
    # 4. Create a delete request 
    if request.method == "DELETE":
        q = Production.query.filter_by(id=id).first()
        db.session.delete(q)
        db.session.commit()
        return make_response({}, 204)
    
# 5. Serializers: navigate back to models.py 



if __name__ == '__main__':
    app.run(port=5555, debug=True)