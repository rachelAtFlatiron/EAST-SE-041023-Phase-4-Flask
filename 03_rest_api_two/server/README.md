# Deliverables

### 1. Review: Serializer
#### 1a. Review `Actor` class in `models.py` and the relationships 
<br />

`production` -> `roles` <- `actors`
#### 1b. Set up the database and run `seed.py`
#### 1c. Write the serializer rules to prevent max recursion

<br />

### 2. Use `Flask-RESTful` to write `GET` and `POST` routes for `Roles`.
#### 2a. Import `Api` and `Resource` from flask-restful.
#### 2b. Create an instance of an `Api`

<br />

### 3. Create the route GET `/roles` using flask restful
#### 3a. Create a `Resource` for `Roles`
#### 3b. Create a view method that returns all roles from the database
#### 3c. Update `to_dict()` so that it only returns `role_name`, the actor's name, and the production's name
#### 3d. Create an Api endpoint for the `Roles` `Resource`
<br />

### 4. Create the route POST `/roles`
#### 4a. Create the view method for a POST
<br />

### 5. Create a resource for `/roles/:id`
#### 5a. Create a `Resource` for `One_Role`
#### 5b. Create a view method for GET
#### 5c. Create a view method for DELETE
#### 5d. Create an Api endpoint for the resource
<br />

### 6. Add a view for PATCH `/roles/:id`
#### 6a. Get the matching query from the database
#### 6b. Iterate over available attributes from request
#### 6c. Using `setattr`, update the appropriate key/value pairs in the matching query
#### 6d. Add and commit the updated object to the database
<br />

## You Do: CRUD for `/actors`

<br />

### 7. Add not found errors 
#### 7a. Import `NotFound` from `werkzeug.exceptions` for error handling
#### 7b. If a production is not found raise the NotFound exception in `/productions` and `/productions/:id`
#### 7c. OR use abort() to create a 404 with a customized error message in `/roles` and `/roles/:id`
#### 7d. AND create a fallback errorhandler using `@app.errorhandler` for non-existant endpoints

<br />

### 8. In `models.py` add constraints
#### 8a. In `Production`
#### - `production.title` is required and must be unique
#### - `production.image` is required
#### - `production.description` must be at least 50 characters
#### 8b. In `Actor`
#### - `actor.name` is required and must be unique
#### - `actor.image` is required
#### 8c. In `Role`
#### - `role.actor_id`, `role.production_id` and `role.role_name` is required
#### 8d. Migrate and upgrade `db`
#### 8e. Test in sqlite3 and Postman

<br />

### 9. In `models.py` add validations
#### 9a. Import `validates` from `sqlalchemy.orm`
#### 9b. In `Production`
#### - `production.image` must be `png`, `jpg`, or `jpeg`
#### - `production.year` must be greater than 1850
#### 9c. In `Actor`
#### - `actor.age` must be between 0 and 200
#### 9d. Test in sqlite3 and Postman

<br />

### 10. Add unprocessable entity errors
#### 10a. Import `UnprocessableEntity` from `werkzeug.exceptions` for error handling
#### 10b. In POST and PATCH use a `try...except` to raise an `UnprocessableEntity` error when necessary