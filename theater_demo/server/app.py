#!/usr/bin/env python3

from flask import Flask, jsonify, make_response, request, abort, session
from flask_migrate import Migrate 
# 1b. import bcrypt
from flask_bcrypt import Bcrypt
from flask_restful import Api, Resource
from werkzeug.exceptions import NotFound, UnprocessableEntity, Unauthorized

from config import app, db, api
from models import Production, Role, Actor, User

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/longest-movies')
def get_longest_movies():
    prods = Production.query.order_by(Production.length.desc()).limit(5)
    prods_list = [prod.to_dict() for prod in prods]
    return make_response(prods_list, 200)

@app.route('/dark-mode', methods=["GET"])
def mode():
    return make_response(jsonify(
        {
            "cookies": request.cookies["mode"]
        }
    ), 200)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app.route('/logout', methods=["GET"])
def logout():
    session['user_id'] = None 
    return make_response('' , 204)

@app.route('/authorized-session', methods=["GET"])
def authorize():
    try:
        user = User.query.filter_by(id=session.get('user_id')).first()
        return make_response(user.to_dict(), 200)
    except: 
        raise Unauthorized("invalid credentials")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 6a. create signup resource
class Signup(Resource):
    def post(self):
        data = request.get_json()
        new_user = User(name=data.get('name'), username=data.get('username'))
        # 6b. hash the given password and save it to _password_hash
        new_user.password_hash = data.get('password')
        # db.session add and commit
        db.session.add(new_user)
        db.session.commit()
        # 6c. save the user_id in session
        session['user_id'] = new_user.id
        #return response
        return make_response(new_user.to_dict(rules=('-_password_hash', )), 201)
api.add_resource(Signup, '/signup')

class Login(Resource):
    def post(self):
        try:
        # 7a. check if user exists
            data = request.get_json()
            user = User.query.filter_by(username=data.get('username')).first()
            # 7b. check if password is authentic
            if user.authenticate(data.get('password')):
                # 7c. set session's user id
                session['user_id'] = user.id 
                return make_response(user.to_dict(), 200)
        except:
            # 7d. send error 
            abort(401, "Unauthorized")

api.add_resource(Login, '/login')            

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@app.route('/productions', methods=["GET", "POST"])
def Productions():
    if(request.method=="GET"):
        q = Production.query.all()
        if not q:
            raise NotFound
        prod_list = [p.to_dict() for p in q]
        res = make_response(jsonify(prod_list), 200)
        return res 
    
    if(request.method=="POST"):
        data = request.get_json()
        try:
            prod = Production(title=data.get('title'), genre=data.get('genre'), length=data.get('length'), year=data.get('year'), image=data.get('image'), language=data.get('language'), director=data.get('director'), description=data.get('description'), composer=data.get('composer') )
            db.session.add(prod)
            db.session.commit()
        except Exception:
            raise UnprocessableEntity('no')

        dict = prod.to_dict()
        return make_response(jsonify(dict), 201)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app.route('/productions/<int:id>', methods=["GET", "DELETE"])
def One_Production(id):
    if(request.method == 'GET'):
        q = Production.query.filter_by(id=id).first()
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

class Roles(Resource):
    
    def get(self):
        q = Role.query.all()
        if not q:
            abort(404, "The role was not found")
        role_dict = [r.to_dict(only=('id', 'role_name', 'actor.name', 'production.title')) for r in q]
        return make_response(role_dict, 200)
    
    def post(self):
        data = request.get_json()
        try:
            role = Role(role_name=data.get('role_name'), production_id=data.get('production_id'))
            db.session.add(role)
            db.session.commit()
        except Exception:
            raise UnprocessableEntity('no')

        return make_response(role.to_dict(), 201)
    
api.add_resource(Roles, '/roles', '/test')

class One_Role(Resource):

    def get(self, id):
        q = Role.query.filter_by(id=id).first()
        if not q:
            abort(404, "The role was not found")
        return make_response(q.to_dict(), 200)
    def delete(self, id):
        q = Role.query.filter_by(id=id).first()
        db.session.delete(q)
        db.session.commit()
        return make_response({}, 204)
    def patch(self, id):
        q = Role.query.filter_by(id=id).first()
        data = request.get_json()
        try:
            for attr in data:
                setattr(q, attr, data.get(attr))
            db.session.add(q)
            db.session.commit()
        except Exception:
            raise UnprocessableEntity('no')
        return make_response(q.to_dict(), 200)
    
api.add_resource(One_Role, '/roles/<int:id>')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Actors(Resource):
    def get(self):
        q = Actor.query.all()
        if not q:
            abort(404, "The Actor was not found")
        actor_dict = [a.to_dict() for a in q]
        return make_response(actor_dict, 200)
    
    def post(self):
        data = request.get_json()
        try:
            actor = Actor(name=data.get('name'), image=data.get('image'), age=data.get('age'), country=data.get('country'))
            db.session.add(actor)
            db.session.commit()
        except Exception:
            raise UnprocessableEntity('no')

        return make_response(actor.to_dict(), 201)
api.add_resource(Actors, '/actors')

class One_Actor(Resource):

    def get(self, id):
        q = Actor.query.filter_by(id=id).first()
        if not q:
            abort(404, "The Actor was not found")
        return make_response(q.to_dict(), 200)
    def delete(self, id):
        q = Actor.query.filter_by(id=id).first()
        db.session.delete(q)
        db.session.commit()
        return make_response({}, 204)

    def patch(self, id):
        q = Actor.query.filter_by(id=id).first()
        data = request.get_json()
        try:
            for attr in data:
                setattr(q, attr, data.get(attr))
            db.session.add(q)
            db.session.commit()
        except Exception: 
            raise UnprocessableEntity('no')
        return make_response(q.to_dict(), 200)
api.add_resource(One_Actor, '/actors/<int:id>')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app.errorhandler(NotFound)
def handle_not_found(e):
    response = make_response(
        "Not Found: Sorry the resource you are looking for does not exist",
        404
    )
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)