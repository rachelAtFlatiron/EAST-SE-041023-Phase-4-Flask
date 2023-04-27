- all routes need user login (no hash for now)
- keep user logged in


## Deliverables

##### 1. Create a dark mode cookie
##### 1a. In `app.py` create a non-restful route `/dark_mode` that sets a cookie

<br />

##### 2. Create a `User` model in `models.py` for sessions
###### - Create the fields `name`, `email`, `admin` (default false)

<br />

#### 3. Create a `User` resource in `app.py` that represents signing up
##### 3a. Create a `post` route
##### 3b. Create value `user_id` as part of session
##### 3c. Return the new user information as the response

<br />

#### 4. Create a `Login` resource in `app.py` that represents logging in
##### 4a. Create a `POST` method that searches for the user
##### 4b. If the user exists set `user_id` as part of session and send the user info to the client

<br />

#### 5. Create a `Logout` resource in `app.py` that represents logging out
##### 5a. Create a `DELETE` method that clears session user id to `None`
##### 5b. Send back a 204 no content response to frontend 

<br />

#### 6. Create an `AuthorizedSession` resource and `/authorize` route in `app.py` that represents staying logged in
##### 6a. Create a `GET` route that checks if there is a user_id in session
##### 6b. Send back either the user (200) or unauthorized (401)


<br />

#### 7. Build a `formik` form for signing up/logging in that uses `yup` to make client side validations
##### 7a. Create React state, `signUp` that represents which form (sign up or log in) to render 
##### 7b. Use a button to toggle `signUp`
##### 7c. Use `signUp` to conditionally render the login or signup form

<br />

#### 8. On form submit update React state `user`
##### 8a. Create state `user` in App.js
##### 8b. On form submit make a fetch `POST` to `/users` or `/login`
##### 8c. On successful signup add user to React state and redirect to homepage

<br />

#### 9. Make a request to `/authorize` in `App.js` to keep user logged in
##### 9a. If user is found, set `user` state to user, otherwise set `user` state to `null` and redirect appropriately 

<br />

#### 10. In `Navigation.js` create a button that conditionally renders between `Login/Signup` and `Logout` based on `user` state
##### 10a. When user clicks on `Logout` button, log user out and redirect to signup/login form.
##### 10b. When user clicks on `Login/Signup` redirect to login/signup form (yes this is redundant)