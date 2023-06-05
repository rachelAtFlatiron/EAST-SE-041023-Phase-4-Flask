


## `Gunicorn` and `Honcho`

- run flask AND react at same time instead of opening up two different terminals:
- `honcho` and `gunicorn`
- `Procfile.dev` to create scripts making use of `honcho` and `gunicorn`

- `gunicorn` Python WGI HTTP server
- `honcho`: manages Procfile applications
- `Procfile`: a file that describes how to run your application even if the application is in multiple independent components 

```python

web: <Start React here>
api: <Start API here>
worker: <For job queues>

```


## Validations

- validations run when we try to create our object before we save to db

## Constraints


- constraint will run after we try to save to db
- best to use them in combo


## `try...except...`

- these exceptions will give you a 500 by default
- to specify what's going on....
- use a `try...except...`
- on `except` raise error

## `CORS`

## Formik and yup
- `Formik`: npm package that makes writing React forms easier
- `yup`: npm package for object schema validation

- NOTE: Flask-WTForm and WTForms are for Python view templates

## yup
You can...
- parse input values to correct types
- perform validations
- make nested schemas (blog)
## useFormik

## Formik errors
- validations run on handleChange, setFieldValue, setValues, handleSubmit and submitForm

## Displaying errors

```js
{touched.username && errors.username && <div>{errors.username}</div>}
           <Field name="email" />
```

## async/await