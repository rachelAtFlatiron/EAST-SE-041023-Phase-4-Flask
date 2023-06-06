---

title: '04_exceptions_validations'

---

# Exceptions and Validations

--- 

## Validations

- validations will throw an error before they try to `db.session.commit()`
- these are Flask level validations
- if you have an @validates and make an entry directly in SQL, it will bypass @validates

```python
# in models.py
@validates('age') # uses the @validations decorator
    def validate_age(self, key, age):
        if(age < 0 or age > 200):
            raise ValueError('age must be greater than 0 and less than 200')
        else:
            return age
```

---

## Constraints 

- Constraints are handled at the SQL level
- It will be triggered both in Flask shell and directly in SQL

```python
name = db.Column(db.String, nullable=False, unique=True)
```

---

## `@app.errorhandler(e)`


```python
from werkzeug.exceptions import NotFound

@app.errorhandler(NotFound)
def some_error_handler(e):
    # additional logic
    return make_response({"message": ""}, <status code>)
```

---

## Werkzeug HTTPException

- automatically properly serialized, standardized exception

```python
# other exceptions include NotFound, Forbidden, MethodNotAllowed, RequestTimeout, UnprocessableEntity, InternalServerError and more
from werkzeug.exceptions import BadRequest

# description overrides default message
# you can raise a werkzeug exception directly in your classes
raise BadRequest(description=None)
```

---

## `abort()`

- a wrapper for Werkzeug Errors
- don't have to individually import Werkzeug exceptions
- must supply appropriate status code

```python
@app.route('/')
def hello():
    abort(404, "not found")
```

<aside class="notes">
`raiseException("Error")` - this is a python thing that can be used in any python code...not just flask stuff
</aside>

---