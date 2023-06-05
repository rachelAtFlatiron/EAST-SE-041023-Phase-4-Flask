# REST APIs with Flask: Deliverables

### 1. Review: Serializer
#### 1a. Review `Actor` class in `models.py` and the relationships 

<br />

---

<br />

`production` -> `roles` <- `actors`
#### 1b. Set up the database and run `seed.py`
#### 1c. Write the serializer rules to prevent max recursion

<br />

---

<br />


### 2. Use `Flask-RESTful` to write `GET` and `POST` routes for `Roles`.
#### 2a. Import `Api` and `Resource` from flask-restful.
#### 2b. Create an instance of an `Api`

<br />

---

<br />

### 3. Create the route GET `/roles` using flask restful
#### 3a. Create a `Resource` for `Roles`
#### 3b. Create a view method that returns all roles from the database
#### 3c. Update `to_dict()` so that it only returns `role_name`, the actor's name, and the production's name
#### 3d. Create an Api endpoint for the `Roles` `Resource`

<br />

---

<br />

### 4. Create the route POST `/roles`
#### 4a. Create the view method for a POST

<br />

---

<br />

### 5. Create a resource for `/roles/:id`
#### 5a. Create a `Resource` for `One_Role`
#### 5b. Create a view method for GET
#### 5c. Create a view method for DELETE
#### 5d. Create an Api endpoint for the resource

<br />

---

<br />

### 6. Add a view for PATCH `/roles/:id`
#### 6a. Get the matching query from the database
#### 6b. Iterate over available attributes from request
#### 6c. Using `setattr`, update the appropriate key/value pairs in the matching query
#### 6d. Add and commit the updated object to the database

<br />

---

<br />

## You Do: CRUD for `/actors`