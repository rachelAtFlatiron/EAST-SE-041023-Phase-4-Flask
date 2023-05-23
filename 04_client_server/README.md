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

### 2. Use a fetch request to get actors and productions on the page
#### 2a. Create a `useEffect` in `App.js` to fetch from `/productions` and `/actors`
#### 2b. Save the result in state
#### 2c. Pass it down to `<ActorContainer />` and `<ProductionContainer />`
<br />

### 3. In `ProductionDetail.js` and `ActorDetail.js`
#### 3a. Fetch the current `production` and `actor` based on the url params
#### 3b. Destructure the values and display them on the page
#### 3c. If the response throws and error, redirect to the `/not-found` client route
<br />

### 4. Use `formik` and `yup` to create a `ProductionForm`
#### 4a. Import `useFormik` and `yup`
#### 4b. Create a schema of constraints for the `ProductionForm` using `yup`
#### 4c. Create a `formik` instance containing:
#### - The initial values of the form
#### - The validation schema
#### - A `handleSubmit` callback
<br />

### 5. Attach the `formik` instance to the JSX
#### 5a. In the form's `onSubmit` event pass in the `formik.handleSubmit` callback
#### 5b. In the inputs' `onChange` event pass in the `formik.handleChange` callback
#### 5c. In the inputs' values pass in `formik.values.key` 
<br />

### 6. Make use of `formik`'s errors
#### 6a. Add an `onBlur` event to allow the ability to update `formik.touched`
#### 6b. Use `formik.touched` and `formik.errors` to conditionally render errors below appropriate forms.

### 7. [You Do] Use `formik` and `yup` to create a form in `ActorForm`