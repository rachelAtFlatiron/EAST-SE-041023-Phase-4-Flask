from flask import Flask, jsonify, make_response, request
#wrapper for alembic?
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy

from models import db, Production

#so that flask application can see all files/folders
#pass in __name__ to look in current module section
app = Flask(__name__)

#config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db' #attach to database
#deprecated from new flask but will throw error if not included
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# connect app to db
migrate = Migrate(app, db)
#intialize app with sqlalchemy
db.init_app(app)

#environment variables in terminal now
#export FLASK_APP = app.py #where majority of app will be build
#export FLASK_RUN_PORT=5555 
#flask db init
#flask db revision --autogenerate -m 'create tables'
#flask db upgrade head 


#WEB SERVER TIME:) 
#flask run --debug <- flask will run and restart on every save

#HOOKS
@app.before_request
def runs_before():
    current_user = {"user_id": 1, "username": "frank"}
    print(current_user)

@app.route('/')
def index():
    return "<h1>Hello world</h1" 

@app.route('/image')
def image():
    return '<img src="https://hips.hearstapps.com/hmg-prod/images/golden-retriever-royalty-free-image-506756303-1560962726.jpg?crop=1.00xw:0.756xh;0,0.0756xh&resize=1200:*" />'

@app.route('/productions/<string:title>')
def production(title):
    #c for continue
    #import ipdb; ipdb.set_trace() 

    #NOTE THE [0] or .first() FILTER RETURNS A LIST () 
    production = Production.query.filter(Production.title == title).first()

    production_response = {
        "title": production.title,
        "director": production.director
    }
    #don't need jsonify...will automatically parse as json
    return make_response(jsonify(production_response), 200)

# @app.route('/context')
# def context():
#     import ipdb; ipdb.set_trace()
    #useful for POSTs
    #request => <Request 'http://localhost:5555/context' [GET]>
    #request.path => /context




