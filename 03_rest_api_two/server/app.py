#!/usr/bin/env python3

from flask import Flask, jsonify, make_response, request, abort
from flask_migrate import Migrate 
from models import db, Production, Role
# 2a. import Api, Resource
from flask_restful import Api, Resource
# 7a. import NotFound from werkzeug.exceptions and abort from Flask
from werkzeug.exceptions import NotFound 


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
        # 7b. if not found, raise NotFound exception
        q = Production.query.all()
        if not q:
            raise NotFound
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
        # 7b. raise NotFound exception
        if not q:
            raise NotFound
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
    # 🛑 don't forget the 'self'
    def get(self):
        q = Role.query.all()
        # 7c. If not found, use abort
        if not q:
            abort(404, "The role was not found")
        # 3c. add rules to .to_dict()
        # 🛑 can also add negative rules, with rules=
        role_dict = [r.to_dict(only=('id', 'role_name', 'actor.name', 'production.title')) for r in q]
        return make_response(role_dict, 200)
    
    #4a. create POST view method
    def post(self):
        data = request.get_json()
        role = Role(role_name=data.get('role_name'), production_id=data.get('production_id'))
        db.session.add(role)
        db.session.commit()

        return make_response(role.to_dict(), 201)
    
# 3d. create api endpoint for Roles 
# 🛑 can pass multiple URLs to same resource
api.add_resource(Roles, '/roles', '/test')

# 5a. create resource for SHOW and DELETE
class One_Role(Resource):
    
    # 🛑 If you try and use query outside of methods you would be working outside of application context


    # 5b. create SHOW view method
    def get(self, id):
        q = Role.query.filter_by(id=id).first()
        # 7c. If not found, use abort
        if not q:
            abort(404, "The role was not found")
        return make_response(q.to_dict(), 200)
    # 5c. create DELETE view method
    def delete(self, id):
        q = Role.query.filter_by(id=id).first()
        db.session.delete(q)
        db.session.commit()
        return make_response({}, 204)
    # 6. Create a PATCH view method
    def patch(self, id):
        # 6a. get matching query
        q = Role.query.filter_by(id=id).first()
        # 6b. iterate over attributes from request
        data = request.get_json()
        # 6c. update available attributes from request
        for attr in data:
            setattr(q, attr, data.get(attr))
        # 6d. add, commit to database
        db.session.add(q)
        db.session.commit()
        return make_response(q.to_dict(), 200)
    
# 5d. create an API endpoint for One_Role
api.add_resource(One_Role, '/roles/<int:id>')

# 🛑 you still ned raise() and abort() so view method can exit gracefully
#7d. create fallback
@app.errorhandler(NotFound)
def handle_not_found(e):
    response = make_response(
        "Not Found: Sorry the resource you are looking for does not exist",
        404
    )
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)