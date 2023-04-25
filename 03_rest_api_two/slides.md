---

title: '03_rest_api_two'

---

# Flask APIs Part Two

---

✅ Objectives

- [ ] Build and execute a PATCH and DELETE request
- [ ] Discuss the importance of handling exceptions
- [ ] Handle exceptions
- [ ] Use Flask validations

---

## Werkzeug HTTPException

- automatically properly serialized

```python
from werkzeug.exceptions import BadRequest
raise BadRequest(<optional: custom message>)
```
- you can add other custom attributes

```python
e = BadRequest('blah')
e.data = {'custom': 'test'}
raise e
```
---

## abort()

- uses Werkzeug HTTPException and will be wrapped in it such that this exception will also be automatically serialized
- abort(): gives ability to give status code and message
- it also cancels our submission to the database?

```js
@app.route('/')
def hello():
    abort(404, "not found")
    return "hello"
```

--- 

## @api.errorhandler(SomeException)

- you can write a bunch of lines of code


## You can redirect

`Flask.redirect(location, statuscode, response)`

- location: URL to redirect to
- statuscode: sent to browser
- response: create response

```python
try:
    ...
except Exception, e:
    return redirect(url_for('index'))

@app.route('/foo')
def foo():
    ...
```

---

## You can add custom headers

```python
@api.errorhandler(SomeException)
@api.header('My-Header',  'Some description')
def handle_fake_exception_with_header(error):
    '''This is a custom error'''
    return {'message': error.message}, 400, {'My-Header': 'Value'}
```