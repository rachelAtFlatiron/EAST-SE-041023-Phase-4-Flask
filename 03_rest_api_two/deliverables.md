
# Flask APIs Part Two

---

✅ Objectives

- [ ] Build and execute a PATCH and DELETE request
- [ ] Discuss the importance of handling exceptions
- [ ] Handle exceptions
- [ ] Use Flask validations

--- 

#### 1. Import `NotFound` from `werkzeug.exceptions` for error handling

<br />

#### 2. Use `@app.errorhandler()` decorator to handle Not Found
##### 2a. Use `make_response` to create a response message with 404

<br />

#### 3. Update current routes with error handling

<br />

#### 4. In `ProductionById` create a `PATCH` request
##### 4a. If the production is not found raise the NotFound exception
##### - loop through the `request.form` object and update productions attributes

<br />

#### 5. In `ProductionById` create a `DELETE` request 
##### 5a. If the production isn't found raise a NotFound error