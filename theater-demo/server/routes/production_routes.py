from werkzeug.exceptions import BadRequest, NotFound
from flask import Flask, request, abort, make_response, url_for, redirect, jsonify
from flask_restful import Api, Resource 
from models import db, Production
#Production GET POST
class Productions(Resource):
    def get(self):

        production_list = [production.to_dict() for production in Production.query.all()]
        return make_response(production_list, 200)
    
    def post(self):
        request_json = request.get_json()

        new_prod = Production()
        #need this to raise integrity errors
        for attr in request_json:
            setattr(new_prod, attr, request_json[attr])

        #import ipdb; ipdb.set_trace()
        #request.path, request.host, request.get_json()
        db.session.add(new_prod)
        db.session.commit()

        return make_response(
            new_prod.to_dict(),
            201
        )
    
api.add_resource(Productions, '/productions')

#Production SHOW PATCH DELETE
class ProductionById(Resource):
    def get(self, id):
        try: 
            prod = Production.query.filter(Production.id == id).first().to_dict()
            return make_response(prod, 200)
        except Exception as e:
            abort(404, 'The production you were looking for was not found')

    def patch(self, id):
        try:
            prod = Production.query.filter_by(id=id).first()
            req_json = request.get_json()
            for attr in req_json:
                #MAKE SURE TO USE ATTR
                setattr(prod, attr, req_json[attr])
            db.session.add(prod)
            db.session.commit()
            return make_response(prod.to_dict(), 200)
        except Exception as e:
            return make_response(e, 400)
            
    def delete(self, id):
        try:
            prod = Production.query.filter_by(id=id).first()
            db.session.delete(prod)
            db.session.commit()
            return make_response('', 204)
        except Exception as e:
            return make_response(e, 404)

api.add_resource(ProductionById, '/productions/<int:id>')