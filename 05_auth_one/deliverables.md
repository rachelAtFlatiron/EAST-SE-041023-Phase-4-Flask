- all routes need user login (no hash for now)
- keep user logged in


## Deliverables

##### 1. Create a `User` model

<br />

##### 2. Create a `User` resource in `app.py` that represents signing up
###### 2a. Create a `post` route
###### 2b. Create value `user_id` as part of session hash

<br />

#### 3. Build a `formik` form for signing up/logging in that uses `yup` to make client side validations
##### 3a. Use React state to conditionally render the sign up/log in form
##### 3b. Conditionally make a fetch `POST` based on signup or login
##### 3c. On successful signup/login add user to React state and redirect to homepage
##### 3d. Use `ipdb` to check cookies in terminal

<br />

#### 4. Create a `Login` resource in `app.py` that represents logging in
##### 4a. Create a `post` request that searches for the user
##### 4b. If the user exists set user_id to the session hash and send the user info to the client
##### 4c. Toggle the signup/login button appropriately

<br />

#### 5. Create a `Logout` resource in `app.py` that represents logging out
##### 5a. Create a `delete` method that clears session user id to None
##### 5b. Send back a 204 no content response to frontend 
##### 5c. Redirect frontend to login/signup page

<br />

#### 6. Create an `AuthorizedSession` resource in `app.py` that represents staying logged in
##### 6a. Create a `get` route that checks if there is a user_id in session
##### 6b. Send the user as a response and put in react state, else set react state to `null`

