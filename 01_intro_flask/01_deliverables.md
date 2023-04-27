# Intro to Flask

## SWBATs

- [ ] Intialize a Flask application
- [ ] Understand how to use SQLAlchemy within Flask
- [ ] Use Flask routing and create views
- [ ] Use the Flask shell

---

## Deliverables

#### 1. In `models.py` create a Production Model 
##### - Use the tablename `productions`
##### - Include columns title: string, genre: string, budget:float, image:string,director: string, description:string, ongoing:boolean, created_at:date time, updated_at: date time 

<br />

#### 2. Set up a flask app in `app.py`
##### 2a. In `app.py` import flask, migrate, db, and the Production model
##### 2b. Create an instance of a flask app
##### 2c. Configure the flask app to connect to a database 
##### 2d. Connect app to db with `Migrate`
##### 2e. Initialize the app
<br />

#### 3. Migrate the `Production` model using flask

<br />

#### 4. Create a `seed.py` file
##### 4a. Import app, db, and models
##### 4b. Create application context 
##### 4c. Delete all existing records before reseeding
##### 4d. Create some seeds and commit them to the database

<br />

#### 5. Run flask shell and query Production to check seeds

<br />

#### 6. Create a `/` route which will return a view with  `<h1>Hello World!</h1>`

<br />

#### 7. Create a dynamic route `/productions/<string:title>` that searches for all matching records
##### 7a. Import `jsonify` and `make_response`
##### 7b. Create the route() decorator
##### 7c. Create a function `def production()` that filters through all Production records and returns the appropriate one
##### 7d. Return the result as json

<br />

#### 8. Use `ipdb` to view request context
##### 8a. Inside the `production()` function, run `import ipdb; ipdb.set_trace()`
##### 8b. Visit the route and check out the console!

<br />

#### 12. Use the before_request request hook, what this hook does is up to you.
##### - Use the decorator: `@app.before_request`
##### - Create a function `def runs_before()` that prints `Hello World`
##### - Visit a few routes!

