# Exceptions and Validations: Deliverables

### 7. Add not found errors 
#### 7a. Import `NotFound` from `werkzeug.exceptions` for error handling
#### 7b. If a production is not found raise the NotFound exception in `/productions` and `/productions/:id`
#### 7c. OR use abort() to create a 404 with a customized error message in `/roles` and `/roles/:id`
#### 7d. AND create a fallback errorhandler using `@app.errorhandler` for non-existant endpoints

<br />

---

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

---

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

---

<br />

### 10. Add unprocessable entity errors
#### 10a. Import `UnprocessableEntity` from `werkzeug.exceptions` for error handling
#### 10b. In POST and PATCH use a `try...except` to raise an `UnprocessableEntity` error when necessary