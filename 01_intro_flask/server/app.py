#!/usr/bin/env python3

# 📚 Review With Students:
    # Request-Response Cycle
    # Web Servers and WSGI/Werkzeug

# 1. ✅ Navigate to `models.py`

# 2. ✅ Set Up Imports
from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate 
from models import db, Production

# 3. ✅ Initialize the App
    # Add `app = Flask(__name__)`
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

migrate = Migrate(app, db)

db.init_app(app)

 # 4. ✅ Migrate 

# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# flask db init - creates migrations, instance, pycache folders
# flask db revision --autogenerate -m 'Create tables productions' 
# (or flask db migrate)
# flask db upgrade


# 5. ✅ Navigate to `seed.rb`

# 12. ✅ Routes

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# 13. ✅ Run the server with `flask run` and verify your route in the browser at `http://localhost:5000/`

# 14. ✅ Create a dynamic route
# 15.✅ Update the route to find a `production` by its `title` and send it to our browser

# 🛑 Before continuing, import `jsonify` and `make_response` from Flask at the top of the file.
    
@app.route('/productions/<string:title>')
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

    return make_response(
        jsonify(production_response),
        200
    )

# 16.✅ View the path and host with request context
# 🛑 Import request - this is a LocalProxy object from werkzeug, 
@app.route('/context')
def context():
    import ipdb; 
    ipdb.set_trace()
    return f'<h1>Path{request.path} Host:{request.host}</h1>'


# 17.✅ Use the before_request request hook, what this hook does is up to you. You could hit a breakpoint, print something to server console or anything else you can think of.
@app.before_request
def runs_before():
    current_user={"user_id":1, "username":"rose"}
    print(current_user)

# Note: If you'd like to run the application as a script instead of using `flask run`, uncomment the line below 
# and run `python app.py`

if __name__ == '__main__':
    app.run(port=5555, debug=True)