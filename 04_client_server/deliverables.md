## Deliverables



#### 2. In `models.py` import validates

<br />

##### 2a. Create a constraint on `Production.role` for nullable
##### 2b. Use the validates decorator to check if `image` contains `.jpg`

<br />


#### 1. Install `honcho` and `gunicorn`
##### 1a. Create a `Procfile` file that contains scripts to use `honcho` and `gunicorn`

<br />

#### 3. In `app.py` import `CORS`

<br />


#### 4. Start up server / client 

<br />

#### 5. In `client/src/App.js` create a `GET` request to set `productions` state.
##### 5a. Use `async/await`

<br />

#### 6. `npm install formik yup`
##### 6a. Import them into `ProductionForm.js`

<br />

#### 7. Use `yup` to create validations schema...
##### - every form field is required
##### - title, genre, description should have character limits
##### - budget should be a positive number
##### - ongoing is set to `True` by default on our server

<br />

#### 8. Use the `useFormik` hook to check our `POST` against our `yup` schema 
##### 8a. Upon successful `POST` redirect to page of new production
##### 8b. Create the `onSubmit` and `onChange` events that uses `formik`

#### 9. Use `formik` to create errors on form when the user doesn't fill it out right