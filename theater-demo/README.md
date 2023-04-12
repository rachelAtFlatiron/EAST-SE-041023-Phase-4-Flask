# Intro to Flask

## SWBATs

- [ ] Intialize a Flask application
- [ ] Understand how to use SQLAlchemy within Flask
- [ ] Use Flask routing and create views
- [ ] Use the Flask shell

---

## Deliverables

#### 1. In `models.py` create a Production Model 
- Use the tablename `productions`
- Include columns title: string, genre: string, budget:float, image:string,director: string, description:string, ongoing:boolean, created_at:date time, updated_at: date time 


#### 2. In `app.py` import flask, migrate, db, and the Production model

#### 3. Initialize the app
- Configure the database 
- Set migrations
- Initialize the app

#### 4. Migrate!

#### 5. In `seed.py` prepare to start seeding the database 
- Import app, db, and models
- Initialize an instance of SQLAlchemy with `db.init_app(app)`
- Create application context 

#### 6. Delete all existing records before reseeding

#### 7. Create some seeds and commit them to the database

#### 8. Run flask shell and query Production to check seeds

#### 9. Create a `/` route which will return a view with  `<h1>Hello World!</h1>`


#### 10. Create a dynamic route `/productions/<string:title>` that searches for all matching records
- Import `jsonify` and `make_response`
- Create the route() decorator
- Create a function `def production()` that filters through all Production records
- Return the result as json

#### 11. View the path and host with request context
- Inside the `production()` function, run `import ipdb; ipdb.set_trace()`
- Visit the route and check out the console!

#### 12. Use the before_request request hook, what this hook does is up to you. You could hit a breakpoint, print something to server console or anything else you can think of.
- Use the decorator: `@app.before_request`
- Create a function `def runs_before()` that prints `Hello World`
- Visit a few routes!

