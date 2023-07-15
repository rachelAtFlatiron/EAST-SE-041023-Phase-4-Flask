# Intro to Flask: Deliverables

### 1. In `models.py` create a Production Model 
#### - Use the tablename `productions`
#### - Include columns title: string, genre: string, budget:float, image:string,director: string, description:string, ongoing:boolean, created_at:date time, updated_at: date time 

<br />

---

<br />

### 2. Set up a flask app in `app.py`
#### 2a. In `app.py` import flask, migrate, db, and the Production model
#### 2b. Create an instance of a flask app
#### 2c. Configure the flask app to connect to a database 
#### 2d. Connect app to db with `Migrate`
#### 2e. Initialize the app

<br />

---

<br />

### 3. Migrate the `Production` model using flask

<br />

---

<br />

### 4. Create a `seed.py` file
#### 4a. Import app, db, and models
#### 4b. Create application context 
#### 4c. Delete all existing records before reseeding
#### 4d. Create some seeds and commit them to the database

<br />

---

<br />

### 5. Run flask shell and query Production to check seeds

<br />

---

<br />

### 6. Create a `/` route which will return a view with  `<h1>Hello World!</h1>`
#### 6a. Run the server with `flask run --debug` to verify the route in the browser

<br />

---

<br />

### 7. Create a `/longest-movies` route to retrieve the first 5 longest movies
#### 7a. Import `jsonify` and `make_response`
#### 7b. Use the `route()` decorator
#### 7c. Query for the top 5 longest movies
#### 7d. Jsonify and return the response

<br />

---

<br />

### 8. Create a dynamic route `/productions/<string:title>` that searches for all matching records
#### 8a. Use the `route()` decorator
#### 8b. Create a function `def production()` that filters through all Production records and returns the appropriate one
#### 8c. Return the result as json

<br />

---

<br />

### 9. Use `ipdb` to view request context
#### 9a. Inside the `production()` function, run `import ipdb; ipdb.set_trace()`
#### 9b. Visit the route and check out the console!

<br />

---

<br />

### 10. Use the before_request request hook, what this hook does is up to you.
#### - Use the decorator: `@app.before_request`
#### - Create a function `def runs_before()` that prints `Hello World`
#### - Visit a few routes!

