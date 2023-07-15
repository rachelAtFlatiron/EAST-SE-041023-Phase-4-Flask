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
class Model:
    ...
    @validates('age', 'year') # uses the @validations decorator
        def validate_age(self, key, age):
            if(age < 0 or age > 200):
                raise ValueError('age must be greater than 0 and less than 200')
            else:
                return age
```

---

## Constraints 

- Constraints are handled at the table level
- It will be triggered both in Flask shell and directly in SQL

```python
name = db.Column(db.String, nullable=False, unique=True, db.CheckConstraint(...))
```

---

## `@app.errorhandler(e)`


```python

# use decorator to register custom error handler
@app.errorhandler(404)
def some_error_handler(e):
    # additional logic
    return make_response({"message": ""}, <status code>)

@app.route('/')
def index():
    try:
        #logic
    except Exception:
        abort(404)

```

---

## Werkzeug HTTPException

- automatically properly serialized, standardized exception

```python
# other exceptions include NotFound, Forbidden, MethodNotAllowed, RequestTimeout, UnprocessableEntity, InternalServerError and more
from werkzeug.exceptions import BadRequest

# description overrides default message
# you can raise a werkzeug exception directly in your classes
@app.route('/')
def index():
    try:
        #logic
    except Exception:
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
`raiseException("Error")` - this is a python thing that can be used in any python code...not just flask stuff <br />
abort raises HTTPException - same as raising an exception.  <br />
using make_response is not handled the same way <br />
error handling mechanism: looks for closest error handler that matches raised exception
</aside>

---