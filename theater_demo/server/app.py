#!/usr/bin/env python3

# 1. Navigate to `models.py`

# 2a. Set Up Imports
# 2b. Create instance of Flask
# 2c. Configure the flask app to connect to a database
# 2d. Connect app to db with Migrate
# 2e. Initialize the app


# 3. Migrate the Production model

# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# flask db init - creates migrations, instance, pycache folders
# flask db revision --autogenerate -m 'Create tables productions' 
# (or flask db migrate)
# flask db upgrade


# 4-5. Navigate to `seed.rb`

# 6. Create a / route that returns Hello World
# 6a. Run `flask run --debug` to check if its in the browser

#7. Create a path to retrieve the longest movie
# 7a. Import jsonify, make_response
# 7b. Use the `route` decorator
    # 7c. Query for the longest movie
    # 7d. Jsonify and return the response

# 8. Create a dynamic route
# 8a. Use the route decorator
# 8b. Create productions() to filter through db
    # 8c. Return result as JSON


# 9. View the path and host with request context
# 9a. Import 'request'
# 9b. Create route `context` 
    # 9c. use ipdb
    # import ipdb; 
    # ipdb.set_trace()


# 10. Use the before_request request hook, what this hook does is up to you. You could hit a breakpoint, print something to server console or anything else you can think of.

# Note: If you'd like to run the application as a script instead of using `flask run`, uncomment the line below 
# and run `python app.py`

# if __name__ == '__main__':
#     app.run(port=5555, debug=True)