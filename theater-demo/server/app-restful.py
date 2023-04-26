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

#********************custom routes*******************
@app.route('/longest-movies')
def get_longest_movies():
    prods = Production.query.order_by(Production.length.desc()).limit(5)
    prods_list = [prod.to_dict() for prod in prods]
    return make_response(prods_list, 200)

@app.route('/most-popular-actors')
def most_popular_actors():
    #for each actor
    #sum number of roles
    pass 

# ***********************reusable get***********************
def default_get(model):
    try:
        items = model.query.all()
        items_dict = [item.to_dict() for item in items]
        return make_response(items_dict, 200)
    except Exception as e:
        raise NotFound(f'{model.__name__}s was not found')

# ***********************reusable show***********************
def default_show(model, id):
    try:
        item = model.query.filter(
            model.id == id).first().to_dict()
        return make_response(item, 200)
    except Exception as e:
        abort(404, f'The {model.__name__} you were looking for was not found')


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

# ************************reusable post*********************

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

# ************************reusable delete*********************

def default_delete(model, id):
    row = model.query.filter(model.id == id).first()
    if not row:
        raise NotFound(f'the {model.__name__} requested was not found')
    db.session.delete(row)
    db.session.commit()
    return make_response('', 204)


# ***************************production: GET, POST********************

class Productions(Resource):
    def get(self): #404, 200
        res = default_get(Production)
        return res 
    
    def post(self):
        res = default_post(Production, request)
        return res


api.add_resource(Productions, '/productions')

# ************************production: SHOW, PATCH, DELETE********************
class ProductionById(Resource):
    def get(self, id): #404, 200
        res = default_show(Production, id)
        return res

    def patch(self, id): #422, 200, 404
        res = default_patch(id, Production, request)
        return res

    def delete(self, id): #204, 404
        res = default_delete(Production, id)
        return res


api.add_resource(ProductionById, '/productions/<int:id>')

# ********************actor: GET, POST***********************
class Actors(Resource):
    def get(self): #404, 200
        res = default_get(Actor)
        return res 
 
    def post(self): #422, 201
        res = default_post(Actor, request)
        return res 


api.add_resource(Actors, '/actors')

# ********************actor: SHOW, PATCH, DELETE***********************


class ActorById(Resource):
    def get(self, id): #404, 200
        res = default_show(Actor, id)
        return res


    def patch(self, id): #201, 404, 422
        res = default_patch(id, Actor, request)
        return res

    def delete(self, id): #404, 204
        res = default_delete(Actor, id)
        return res


api.add_resource(ActorById, '/actors/<int:id>')

# **********************role: GET, POST************************


class Roles(Resource):
    def get(self): #404, 200
        res = default_get(Role)
        return res

    def post(self): #201, 422
        res = default_post(Roles, request)
        return res


api.add_resource(Roles, '/roles')

# **********************role: SHOW, PATCH, DELETE************************


class RoleById(Resource):
    def get(self, id): #404, 200
        res = default_show(Role, id)
        return res

    def patch(self, id): #404, 201, 422
        res = default_patch(id, Actor, request)
        return res

    def delete(self, id): #404, 204
        res = default_delete(Role, id)
        return res


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
