# Deliverables

### 1. Use gunicorn to start the client and server
#### 1a. Install `gunicorn`, `honcho`
#### 1b. Create a `Procfile.dev` file and write:
```js
web: PORT=3000 npm start --prefix client
api: gunicorn -b 127.0.0.1:5555 --chdir ./server
```
#### 1c. In terminal run `honcho start -f Procfile.dev`
<br />

### 2. In Home.js get the longest movies and display it on the page
#### - Review /longest-movies in app.py
#### 2a. Create a state for longest movies in Home.js
#### 2b. Use useEffect to fetch /longest-movies and update state

<br />

### 3. Use a fetch request to get actors and productions on the page
#### 3a. Create a `useEffect` in `App.js` to fetch from `/productions` and `/actors`
#### 3b. Save the result in state
#### 3c. Pass it down to `<ActorContainer />` and `<ProductionContainer />`
<br />

### 4. In `ProductionDetail.js` and `ActorDetail.js`
#### 4a. Fetch the current `production` and `actor` based on the url params
#### 4b. Destructure the values and display them on the page
#### 4c. If the response throws and error, redirect to the `/not-found` client route
<br />

### 5. Use `formik` and `yup` to create a `ProductionForm`
#### 5a. Import `useFormik` and `yup`
#### 5b. Create a schema of constraints for the `ProductionForm` using `yup`
#### 5c. Create a `formik` instance containing:
#### - The initial values of the form
#### - The validation schema
#### - A `handleSubmit` callback
<br />

### 6. Attach the `formik` instance to the JSX
#### 6a. In the form's `onSubmit` event pass in the `formik.handleSubmit` callback
#### 6b. In the inputs' `onChange` event pass in the `formik.handleChange` callback
#### 6c. In the inputs' values pass in `formik.values.key` 
<br />

### 7. Make use of `formik`'s errors
#### 7a. Add an `onBlur` event to allow the ability to update `formik.touched`
#### 7b. Use `formik.touched` and `formik.errors` to conditionally render errors below appropriate forms.
<br />

### 8. [You Do] Use `formik` and `yup` to create a form in `ActorForm`