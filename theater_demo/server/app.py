#!/usr/bin/env python3

from flask import Flask, jsonify, make_response, request, abort
from flask_migrate import Migrate 
from models import db, Production, Role, Actor
# 2a. import Api, Resource
from flask_restful import Api, Resource


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

migrate = Migrate(app, db)

# 2b. create Api instance
api = Api(app)

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

@app.route('/productions', methods=["GET", "POST"])
def Productions():
    if(request.method=="GET"):
        q = Production.query.all()
        prod_list = [p.to_dict() for p in q]
        res = make_response(jsonify(prod_list), 200)
        return res 
    
    if(request.method=="POST"):
        data = request.get_json()
        prod = Production(title=data.get('title'), genre=data.get('genre'), length=data.get('length'), year=data.get('year'), image=data.get('image'), language=data.get('language'), director=data.get('director'), description=data.get('description'), composer=data.get('composer') )
        db.session.add(prod)
        db.session.commit()

        dict = prod.to_dict()
        return make_response(jsonify(dict), 201)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app.route('/productions/<int:id>', methods=["GET", "DELETE"])
def One_Production(id):
    if(request.method == 'GET'):
        q = Production.query.filter_by(id=id).first()
        prod_dict = q.to_dict()
        res = make_response(jsonify(prod_dict), 200)
        return res

    if(request.method == "DELETE"):
        q = Production.query.filter_by(id=id).first()
        db.session.delete(q)
        db.session.commit()
        return make_response({}, 204)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3a. create resource for roles
class Roles(Resource):
    # 3b. create view method for all roles
    def get(self):
        q = Role.query.all()
        role_dict = [r.to_dict() for r in q]
        # 3c. add rules to .to_dict()
        return make_response(role_dict, 200)
    
    #4a. create POST view method
    def post(self):
        data = request.get_json()
        role = Role(role_name = data.get('role_name'), production_id=data.get('production_id'), actor_id=data.get('actor_id'))
        db.session.add(role)
        db.session.commit()
        return make_response(role.to_dict(), 201)
# 3d. create api endpoint for Roles 
api.add_resource(Roles, '/roles')

class One_Role(Resource):
# 5a. create resource for SHOW and DELETE
    # 5b. create SHOW view method
    def get(self, id):

        q = Role.query.filter_by(id=id).first()
        #raise error
        if not q:
            return make_response({"error": "not found"}, 404)
        return make_response(q.to_dict(), 200)
    # 5c. create DELETE view method
    def delete(self, id):
        #.delete() does not honor cascading deletes
        #Role.query.filter_by(id=id).first().delete() 
        q = Role.query.filter_by(id=id).first()
        db.session.delete(q)
        db.session.commit()
        return make_response({}, 204)

    # 6. Create a PATCH view method
    def patch(self, id):
        # 6a. get matching query
        role = Role.query.filter_by(id=id).first()
        # 6b. iterate over attributes from request
        data = request.get_json()
        # 6c. update available attributes from request
        for attr in data:
            #update role[attr] with data.get(attr)
            setattr(role, attr, data.get(attr))
        # 6d. add, commit to database
        db.session.add(role)
        db.session.commit()
        return make_response(role.to_dict(), 200)
    
# 5d. create an API endpoint for One_Role
api.add_resource(One_Role, '/roles/<int:id>')

# ~~~~~~~~~~~~~~~YOU DO~~~~~~~~~~~~~~~~~~~~
class Actors(Resource):
    def get(self):
        q = Actor.query.all()
        actor_dict = [a.to_dict() for a in q]

        return make_response(actor_dict, 200)
    
    def post(self):
        data = request.get_json()
        new_actor = Actor(name=data.get('name'), country=data.get('country'), age=data.get('age'), image=data.get('image'))
        db.session.add(new_actor)
        db.session.commit()
        res_dict = new_actor.to_dict()
        response = make_response(res_dict, 201)
        return response

api.add_resource(Actors, '/actors')

class One_Actor(Resource):
    def get(self, id):
        q = Actor.query.filter_by(id=id).first()
        if not q:
            return make_response({"error": "not found"}, 404)
        return make_response(q.to_dict(), 200)
    
    def patch(self, id):
        data = request.get_json()
        actor = Actor.query.filter_by(id=id).first()
        for attr in data: 
            setattr(actor, attr, data.get(attr))
        db.session.add(actor)
        db.session.commit()

        return make_response(actor.to_dict(), 200)

    def delete(self, id):
        actor = Actor.query.filter_by(id=id).first()
        db.session.delete(actor)
        db.session.commit()
        return make_response({}, 204)

api.add_resource(One_Actor, '/actors/<int:id>')
#~~~~~~~~~~~~~~~~~~~~~~~~~~END YOU DO~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
    app.run(port=5555, debug=True)