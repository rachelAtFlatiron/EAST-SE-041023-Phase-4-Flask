#!/usr/bin/env python3

# 📚 Review With Students:
    # Request-Response Cycle
    # Web Servers and WSGI/Werkzeug

# 1. Navigate to `models.py`

# 2a. Set Up Imports
from flask import Flask, request, jsonify, make_response 
from flask_migrate import Migrate 
from models import db, Production

# 2b. Create instance of Flask
app = Flask(__name__)
# 2c. Configure the flask app to connect to a database
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

# 2d. Connect app to db with Migrate
migrate = Migrate(app, db)

# 2e. Initialize the app
db.init_app(app)

# 3. Migrate the Production model

# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# flask db init - creates migrations, instance, pycache folders
# flask db revision --autogenerate -m 'Create tables productions' 
# (or flask db migrate)
# flask db upgrade


# 4. Navigate to `seed.rb`

# 6. Create a / route that returns Hello World
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
# 6a. Run `flask run --debug` to check if its in the browser

#7. Create a path to retrieve the first 5 longest movies
# 7a. Import jsonify, make_response
# 7b. Use the `route` decorator
@app.route('/longest-movies')
def get_longest_movies():
    # 7c. Query for longest movie
    q = Production.query.order_by(Production.length.desc()).limit(1)
    # 7d. Jsonify and return the response
    prod = {
        "title": q[0].title,
        "genre": q[0].genre,
        "length": q[0].length
    }
    return make_response(jsonify(prod), 200)

# 8. Create a dynamic route
# 8a. Use the route decorator
@app.route('/productions/<string:title>')
# 8b. Create productions() to filter through db
# 🛑 First run in browser and view the title as response just to show that its working
def production(title):
    q = Production.query.filter_by(title=title).first()
    production_response = {
        "title": q.title,
        "genere": q.genre,
        "length": q.length
    }

    # 📚 Review With Students: status codes
    # 🛑 `make_response` will allow us to make a response object with the response body and status code
    # 🛑 `jsonify` will convert our query into JSON

    # 8c. Return result as JSON
    return make_response(
        jsonify(production_response),
        200
    )

# 9. View the path and host with request context
# 9a. Import 'request'
# 🛑 this is a LocalProxy object from werkzeug
# 9b. Create route `context` 
@app.route('/context')
def context():
    # 9c. use ipdb
    # import ipdb; 
    # ipdb.set_trace()
    return f'<h1>Path{request.path} Host:{request.host}</h1>'


# 10. Use the before_request request hook, what this hook does is up to you. You could hit a breakpoint, print something to server console or anything else you can think of.
@app.before_request
def runs_before():
    current_user={"user_id":1, "username":"rose"}
    print(current_user)


# Note: If you'd like to run the application as a script instead of using `flask run`, uncomment the line below 
# and run `python app.py`

if __name__ == '__main__':
    app.run(port=5555, debug=True)