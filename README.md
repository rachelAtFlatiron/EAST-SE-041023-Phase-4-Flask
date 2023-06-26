# Auth Part Two: Deliverables

### 1. Create a config file 
#### 1a. Move all app setup from `app.py` to config
#### 1b. Move all db setup from `models.py` to config
#### 1c. In `app.py` import `app`, `api`, and `db` from `config.py`
#### 1d. In `models.py` import `db` from `config.py`

<br />

---

<br />

### 2. Include Bcrypt
#### 2a. `pipenv install flask-bcrypt`
#### 2b. In `config.py` import `Bcrypt` from `flask-bcrypt`
#### 2c. Pass `app` to `Bcrypt`
#### 2d. In `models.py` import `bcrypt`

<br />

---

<br />

### 3. Add a password column to `Users`
#### 3a. Add column `_password_hash` of type string
#### 3b. Add an `admin` column of type string and default set to `False`

<br />

---

<br />

### 4. Create a hybrid property `password_hash`

<br />

---

<br />

### 5. Create a password setter 
#### 5a. Create the password setter so that it takes self and a password
#### 5b. Use bcyrpt to generate the password hash with bcrypt.generate_password_hash
#### 5c. Set the _password_hash to the hashed password  

<br />

---

<br />

### 6. Create a method to authenticate a hash
#### 6a. Pass in self and password
#### 6b. Use `bcrypt`'s `check_password_hash` to verify the password against the hash in the DB with  

<br />

---

<br />

### 7. In `app.py` create a `signup` route
#### - NOTE: Removed `Users` resource and `/users` for creating users
#### 7a. Create a `Signup` resource and add it to the route `/signup`
#### 7b. Hash the given password and save it to `_password_hash`
#### 7c. Don't forget to save the `user_id` in `session`!

<br />

---

<br />

### 8. Update the `Login` resource to use a `try...except`
#### 8a. Check if user exists
#### 8b. Check if password is authentic using the `authenticate` method defined in `models.py`
#### 8c. Set `session`'s `user_id` and send a response
#### 8d. Otherwise send an error message

<br />

---

<br />

### 9. Create an error message for the user if their credentials are invalid
#### 9a. In `Auth.js` create a state `error`
#### 9b. If `formik`'s `onSubmit` throws on error, set error state with the message
#### 9c. Use conditional rendering to display the error on the form on an unsuccessful sign up/log in