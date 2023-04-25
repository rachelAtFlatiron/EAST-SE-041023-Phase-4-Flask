from flask import Flask, request, abort, make_response, url_for, redirect, jsonify
from flask_migrate import Migrate
from flask_cors import CORS

from werkzeug.exceptions import HTTPException, BadRequest, NotFound, Unauthorized, UnprocessableEntity, InternalServerError
from sqlalchemy.exc import IntegrityError, DBAPIError

from flask_restful import Api, Resource

from models import db, Production, Role, Actor

# TODO: UPDATE ERRORS TO REFLECT UNAUTHORIZED
# TODO: Up next: ERRORS IN default_post

app = Flask(__name__)
# CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

# ************************reusable patch*********************


def default_patch(id, model, request):
    try:
        new_item = model.query.filter_by(id=id).first()
        if not new_item:
            abort(404, f'{model.__name__} not found')
        req_json = request.get_json()
        for attr in req_json:
            # MAKE SURE TO USE ATTR
            setattr(new_item, attr, req_json[attr])
        db.session.add(new_item)
        db.session.commit()
        return make_response(new_item.to_dict(), 201)
    except Exception as e:
        if isinstance(e, HTTPException):
            raise e
        elif isinstance(e, ValueError):
            raise UnprocessableEntity(str(e))


def default_post(model, request):
    request_json = request.get_json()  # 422, 201

    new_prod = model()
       # need this to raise integrity errors
    try:
        for attr in request_json:

            setattr(new_prod, attr, request_json[attr])
            request.path, request.host, request.get_json()
        db.session.add(new_prod)
        db.session.commit()
    except Exception as e:

        if isinstance(e, HTTPException) or isinstance(e, DBAPIError):
            raise e
        elif isinstance(e, ValueError):
            raise UnprocessableEntity(str(e))
    
    return make_response(new_prod.to_dict(), 201)

# ***************************production: GET, POST********************

class Productions(Resource):
    def get(self): #404, 200
        # production_list = [{
        #     "title": production.title,
        #     "genre": production.genre,
        #     "director": production.director,
        #     "description": production.description,
        #     "image": production.image,
        #     "budget": production.title,
        #     "ongoing": production.ongoing,
        #     "cast_members": production.cast_members
        # } for production in Production.query.all()]
        try:
            production_list = [production.to_dict()
                               for production in Production.query.all()]
            return make_response(production_list, 200)
        except Exception as e:
            raise NotFound('Productions could not be found')

    def post(self):
        res = default_post(Production, request)
        return res
    
    def old_post(self):
        request_json = request.get_json() #422, 201
        # new_prod = Production(
        #     title=request_json['title'],
        #     genre=request_json['genre'],
        #     length=request_json['length'],
        #     year=request_json['year'],
        #     image=request_json['image'],
        #     language=request_json['language'],
        #     director=request_json['director'],
        #     description=request_json['description'],
        #     composer=request_json['composer']
        # )
        new_prod = Production()
        # need this to raise integrity errors
        try:
            for attr in request_json:
                
                setattr(new_prod, attr, request_json[attr])
                import ipdb; ipdb.set_trace()
                request.path, request.host, request.get_json()
            db.session.add(new_prod)
            db.session.commit()
        except Exception as e:
            
            raise UnprocessableEntity(str(e))

        return make_response(
            new_prod.to_dict(),
            201
        )


api.add_resource(Productions, '/productions')

# ************************production: SHOW, PATCH, DELETE********************


    
class ProductionById(Resource):
    def get(self, id): #404, 200
        try:
            prod = Production.query.filter(
                Production.id == id).first().to_dict()
            return make_response(prod, 200)
        except Exception as e:
            abort(404, 'The production you were looking for was not found')

    def patch(self, id): #422, 200, 404
        res = default_patch(id, Production, request)
        return res

    def delete(self, id): #204, 404
        prod = Production.query.filter_by(id=id).first()
        if not prod:
            raise NotFound('production was not found')
        db.session.delete(prod)
        db.session.commit()
        return make_response('', 204)


api.add_resource(ProductionById, '/productions/<int:id>')

# ********************actor: GET, POST***********************


class Actors(Resource):
    def get(self): #404, 200
        actors = Actor.query.all()
        if not actors:
            raise NotFound('actors not found')
        actors_dict = [actor.to_dict() for actor in actors]
        return make_response(actors_dict, 200)
 
    def post(self): #422, 201
        try:
            req_json = request.get_json()
            new_actor = Actor(
                name=req_json["name"],
                image=req_json["image"],
                age=req_json["age"],
                country=req_json["country"]
            )
            db.session.add(new_actor)
            db.session.commit()
            return make_response(new_actor.to_dict(), 201)
        except Exception as e:
            raise UnprocessableEntity(str(e))


api.add_resource(Actors, '/actors')

# ********************actor: SHOW, PATCH, DELETE***********************


class ActorById(Resource):
    def get(self, id): #404, 200
        actor = Actor.query.filter(Actor.id == id).first()
        if not actor:
            raise NotFound('actor not found')
        return make_response(actor.to_dict(), 200)


    def patch(self, id): #201, 404, 422
        res = default_patch(id, Actor, request)
        return res

    def delete(self, id): #404, 204
        actor = Actor.query.filter(Actor.id == id).first()
        if not actor:
            raise NotFound('actor not found')
        db.session.delete(actor)
        db.session.commit()
        return make_response('', 204)


api.add_resource(ActorById, '/actors/<int:id>')

# **********************role: GET, POST************************


class Roles(Resource):
    def get(self): #404, 200

        roles = Role.query.all()
        if not roles:
            abort(404, 'roles not found')
        role_dict = [role.to_dict() for role in roles]
        return make_response(role_dict, 200)

    def post(self): #201, 422
        try:
            req_json = request.get_json()
            new_role = Role(
                role_name=req_json['role_name'],
                production_id=req_json['production_id'],
                actor_id=req_json['actor_id']
            )
            db.session.add(new_role)
            db.session.commit()

            return make_response(new_role.to_dict(), 201)
        except Exception as e:
            abort(422, str(e))


api.add_resource(Roles, '/roles')

# **********************role: SHOW, PATCH, DELETE************************


class RoleById(Resource):
    def get(self, id): #404, 200
        role = Role.query.filter(Role.id == id).first()
        if not role:
            abort(404, 'role not found')
        return make_response(role.to_dict(), 200)

    def patch(self, id): #404, 201, 422
        res = default_patch(id, Actor, request)
        return res

    def delete(self, id): #404, 204
        role = Role.query.filter(Role.id == id).first()
        if not role:
            abort(404, 'role not found')
        db.session.delete(role)
        db.session.commit()

        return make_response('', 204)


api.add_resource(RoleById, '/roles/<int:id>')

# ******************************errors********************************
# generic errors that will be falled back to


@app.errorhandler(NotFound)
def not_found_error(e):
    return make_response({
        'message': 'the requested resource does not exist'
    }, 404)


@app.errorhandler(Unauthorized)
def unauthorized_error(e):
    return make_response({
        'message': 'you are not authorized'
    }, 401)

# To run the file as a script
# if __name__ == '__main__':
#     app.run(port=5555, debug=True)
