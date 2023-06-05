## Validations
- validations will throw an error when we try to `db.session.commit()`

- use `@validates` decorator

- these only happen in `models.py`

- they are analogous to SQL validations (I think)

- alembic won't handle `db.CheckConstraint` so may be easier to handle at application level with `@validates`


## Errors
werkzeug provides `HTTPException`:
```python @app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request():
    pass #generic exception handler
```
- these exceptions are not seen by user


---

## `abort()`
- gives generic werkzeug error
- `abort()` raises and error that an error handler will convert to a response , it is a wrapper that raises `HTTPException` classes...these can be used to raise specific errors in specific circumstances


---


## `raise BadRequest('message')`

- allows you to send custom message, always sends general 400 error or whatever other error you are raising

`raise NotFound(message)`
`raise Unauthorized(message)`
...

---

both `raise BadRequest(message)` and `abort` are handled the same way
- `abort` is a shortcut so you don't have to keep importing different exceptions
- `abort` comes from the werkzeug package which is wrapped by Flask (i.e. )

---

## `@app.errorhandler(e)`

- this is a more generalized error that will be falled back upon
```python
@app.errorhandler(e)
def some_error_handler(e):
    return make_response({"message": ""}, <status code>)
```


---


`raiseException("Error")` - this is a python thing that can be used in any python code...not just flask stuff

`make_response("message", 500)` will be sent as json and is not automatically created by raising HTTP exceptions


---