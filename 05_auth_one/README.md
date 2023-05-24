# Deliverables

### 1. Use cookies
#### 1a. In the inspector of the browser, enter a cookie for dark/light mode.
#### 1b. Create a GET `/dark-mode` route in `App.py` to track dark mode and light mode.
#### 1c. Use `ipdb` to check out `request.cookies`
#### 1d. Send a response with the cookies' dark-mode information

---

## Our end goal is to require the user to log in to view the site and KEEP the user logged in

---

### 2. Create a `Resource` for `User` to sign up
#### - Review the `User` class in `models.py`
#### 2a. Create a `POST` method to create a new user
#### 2b. Import `session` from `flask`
#### 2c. Create a secret key to enable hasing of `session`
#### - generate secret key in terminal with 
```js
python -c 'import os; print(os.urandom(16))'
```
#### - save secret key with 
```js 
api.secret_key = <secret_key>
```
#### 2d. In the `POST` request save the user id to the session hash (NOT `db.session`)
#### 2e. Add `User` resource to the route `/users`

---

### 3. Review: In `Auth.js` update the form with a `formik` and `yup` 
#### 3a. Create a validations schema using `yup`
#### 3b. Create a `formik` instance containing...
#### - initialValues
#### - validationSchema
#### - onSubmit
#### 3c. Update the inputs in the form to contain `formik` values and `formik`'s `handleChange`
#### - [You Do] `onBlur` and errors

---

### 4. Pass the new user up to `App.js`
#### 4a. Create a state `user` in `App.js` and an `updateUser` function
#### 4b. Pass `updateUser` to `Auth.js`
#### 4c. Pass `POST` response to `updateUser`
#### 4d. Redirect to homepage if login is successful

---

### 5. Create a `/logout` custom route
#### 5a. Set `session['user_id']` to `None`
#### 5b. Return an empty response

---

### 6. You Do: In `Navigation.js` fetch `/logout`
#### - Uncomment the logout button
#### 6a. Write a `handleLogout` function that fetches `/logout` 
#### 6b. If `res.ok` update the user to be `{}`...
#### 6c. ... and navigate to the login page

---

### 7. Use user state to determine whether app is to be viewable
#### 7a. In `App.js` if the user is `null` return the following JSX:
```js
<div className="App light">
    <Navigation updateUser={updateUser} />
    <Auth updateUser={updateUser} />
</div>
```

---

### 8. Create a route for `/authorized-session` in `app.py` that will determine if there is a user stored in session
#### 8a. Create the route
#### 8b. Query for user by `user_id` stored in `session`
#### 8c. If user exists, send user info as response, otherwise `abort` with `401 Unauthorized`

---

### 9. Fetch `/authorized-session` in `App.js` to check if user is present in `session`
#### 9a. Create a function `getUser` that fetch GETs `/authorized-session`
#### 9b. If `res.ok` update `user` with the response 
#### 9c. Invoke `getUser`

---

### 10. Create a `/login` `Resource`
#### 10a. Create a `Resource` `/login` in `app.py` with only a `post` method
#### 10b. Get the username from the request's json
#### 10c. If user exists, save id in session and return user as response
#### 10d. Otherwise raise error
#### 10e. Add the resource to route `/login`
#### - Review `formik` submit method 

---

### 11. Show user greeting in `Navigation.js`
#### 11a. Pass down state `user` from `App.js` to `Navigation.js`
#### 11b. Conditionally render the logout button and a greeting

```js
<>
    <button onClick={} className="button">
        Log Out
    </button>
    <p style={{'margin-top': '8px'}}>Hello, {}</p>
</>
```