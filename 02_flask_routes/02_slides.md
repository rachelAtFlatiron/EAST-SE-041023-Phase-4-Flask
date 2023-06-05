---

title: '02_rest_api_one'

---

# Flask APIs Part One

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

The native flask way:
```js
@app.route('/endpoint', methods=["GET", "POST"])
def records():
    if request.method == 'GET':
        print('do stuff')
```

The `restful_flask` package way:
```js
api.add_resource(CLASSNAME, '/endpoint')
```

---

## Using Flask RESTful

- we don't need @app.route decorator
- instead we create a method that represents each route method (GET, POST, etc.)


```js
from flask_restful import Api, Resource

class MyModel(Resource):
    def get(self):
        print('get all records')
    
    def post(self):
        print('save a record')

//this is how we tell the class what path to use
api.add_resource(MyModel, '/my-model')

```

- what is Resource?  Api?

---

## Why flask-restful instead of the native way?

- You may write routes not included with RESTful routing such as login, alerts, checks and balances, etc.

- If so you will have to use the native way

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

---

- `json.loads()` converts a JSON string in Python object/dictionary


---

## TypeError: Object of type <Model> is not JSON serializable

- If you try to use `jsonify()` or `json.dumps()` on some query you may get this error.

- To solve it you will have to create a `def serialize()` method in your model to express how to serialize the object.  Such that you will then call

`jsonify(result.serializer())`

- But you can skip all that by using...

---

## sqlalchemy-serialize

- Allows you to write rules on what fields to include in your response
- Especially helpful when you need to make use of relationships

```js
from sqlalchemy_serializer import SerializerMixin
from app import db

class SomeModel(db.Model, SerializerMixin)
```

- An easy way to serialize JSON for GET from db and for PUT/POST/PATCH/etc. from client.


---


## Creating JSON responses

`json.dumps()` vs `jsonify()` vs `to_dict()`
- `json.dumps()` does not automatically add an application/json header, and you need to provide how to serialize 
- `jsonify()` will add the header for you, and you need to provide how to serialize
- `to_dict()` is enabled by flask-serialize

---


## Serializer Rules

`serialize_only()` will include ONLY the exact specified fields
`serialize_rules()` is the negative to `serialize_only()` (so don't forget the `-`)

---

## Serializer Rules

```js
only_result = item.to_dict(only=('field_one', 'field_two'))
rules_result = item.to_dict(rules=('-field_one', '-field_two'))
```

OR

```js
serialize_only = ('field_one', 'field_two')
serialize_rules = ('-field_one', '-field_two')
```

---

## Max Recursion

- When creating a many-to-many relationship we may reach a max-recursion depth 
- For example with Actor -< Role >- Films if we try to serialize Actor we may get
```js
{
    id: 1,
    name: 'Richard',
    films: [
        {
            id: 1,
            title: 'Where\'s Richard?',
            actors: [
                {
                    id: 1,
                    name: 'Richard',
                    films: [
                        {
                            //more films...and actors...and films...
                        }
                    ]
                }
            ]
        }
    ]
}

```

---

## Max Recursion

- To avoid this we have to specify where to stop using `serialize_rules(-films.actors)`

```js
{
    id: 1,
    name: 'Richard',
    films: [
        {
            id: 1,
            title: 'Where\'s Richard?'
            //no more actors!
        }
    ]
}

```