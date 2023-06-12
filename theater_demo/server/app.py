#!/usr/bin/env python3

from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate 
from models import db, Production #has to be different from route method


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

migrate = Migrate(app, db)

db.init_app(app)

# | HTTP Verb 	|       Path       	| Description        	|
# |-----------	|:----------------:	|--------------------	|
# | GET       	|   /productions   	| READ all productions 	|
# | GET       	| /productions/:id 	| READ one production   	|
# | POST      	|   /productions   	| CREATE one production 	|
# | PATCH/PUT 	| /productions/:id 	| UPDATE one production	|
# | DELETE    	| /productions/:id 	| DESTROY one production 	|

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1. Create a route to /productions for GET requests
@app.route('/productions', methods=["GET", "POST"])
def Productions(): #has to be different from models class name
    if(request.method == "GET"):
        # 1a. Create the query
        q = Production.query.all()
        # 1b. Loop through the query and convert each object into a dictionary 
        prods = []
        for p in q:
            # prods.append({
            #     "id": p.id,
            #     "title": p.title,
            #     "genre": p.genre,
            #     "length": p.length
            # })
            # 5c. use SerializerMixin's .to_dict() for responses here and everywhere
            prods.append(p.to_dict(rules = ('-language',)))

        # 1c. Use make_response and jsonify to return a response
        res = make_response(jsonify(prods), 200)
        return res
        # 1d. Test in Postman


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 3. Create a route to /productions for a POST request
    if(request.method == "POST"):
        # 3a. Get information from request.get_json() 
        data = request.get_json()
        # 3b. Create new object
        prod = Production(title=data.get('title'), genre=data.get('genre'), length=data.get('length'))
        # 3c. Add and commit to db 
        db.session.add(prod)
        db.session.commit()
        # 3d. Convert to dictionary / # 5c. use .to_dict
        # prod_dict = {
        #     "id": prod.id,
        #     "title": prod.title,
        #     "genre": prod.genre,
        #     "length": prod.length
        # }
        prod_dict = prod.to_dict()
        # 3e. return as JSON
        res = make_response(jsonify(prod_dict), 201)
        return res
        # 3f. Test in postman

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 2. Create a route to /productions/:id for single GET requests
@app.route('/productions/<int:id>', methods=["GET", "DELETE", "PATCH"])
def One_Production(id):
    if(request.method == "GET"):
        q = Production.query.filter_by(id=id).first()
        #import ipdb; ipdb.set_trace()
        # prods = {
        #     "title": q.title,
        #     "genre": q.genre,
        #     "length": q.length
        # }
        prods = q.to_dict()
        # 5c. use to_dict

        res = make_response(jsonify(prods), 200)
        return res
    # 4. Create a delete request 
    if(request.method == "DELETE"):
        q = Production.query.filter_by(id=id).first()
        db.session.delete(q)
        db.session.commit()
        return make_response({}, 204)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 5. Serializers: navigate back to models.py 

if __name__ == '__main__':
    app.run(port=5555, debug=True)