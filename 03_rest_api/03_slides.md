---

title: '03_rest_api'

---

# Flask REST 

---

## Flask-RESTful

- an extension for Flask that adds support for building APIs
- `json-server` was a fake RESTful server

| HTTP Verb 	|       Path       	| Description        	|
|-----------	|:----------------:	|--------------------	|
| GET       	|   /productions   	| READ all resources 	|
| GET       	| /productions/:id 	| READ one resource   	|
| POST      	|   /productions   	| CREATE one resource 	|
| PATCH/PUT 	| /productions/:id 	| UPDATE one resource	|
| DELETE    	| /productions/:id 	| DESTROY one resource 	|

- we use the RESTful methodology so that there is a standard 

---

## Configuring endpoints

The default flask way:
```python
@app.route('/endpoint', methods=["GET", "POST"])
def records():
    if request.method == 'GET':
        print('do stuff')
```

The `restful_flask` package way:
```python
api.add_resource(CLASSNAME, '/endpoint')
```

---

## Using Flask RESTful

- we don't need @app.route decorator
- instead we create a method that represents each route method (GET, POST, etc.)


```python
from flask_restful import Api, Resource

class MyModel(Resource):
    def get(self):
        print('get all records')
    
    def post(self):
        print('save a record')

//this is how we tell the class what path to use
api.add_resource(MyModel, '/my-model')

```

---

## Why flask-restful instead of the default way?

- You may write routes not included with RESTful routing such as login, alerts, checks and balances, etc.

- If so you will have to use the default way

---

## Getting JSON from the request

- It all depends on the content type passed into the request

---

- `request.form`: key/value pairs in the HTML POST form that isn't JSON encoded
- `request.form['key']` if key definitely exists
- `request.form.get('key')` if key may not exist

---

- `request.values`: multipurpose for args and form, especially if they overlap

---

- ➡️ `request.get_json()`: parse json data ⬅️

---

- `request.args`: key value pairs in the URL query string
<img src='https://static.semrush.com/blog/uploads/media/00/6e/006eebc38b54220916caecfc80fed202/Guide-to-URL-Parameters-2.png' width="500px">
