# REST APIs with Flask Part 1

## SWBATs

- [ ] Discuss MVC architecture
- [ ] Explain the concept of REST and RESTful naming conventions
- [ ] Build and execute a GET and POST request
- [ ] Use Postman to interact with Flask
- [ ] Use serializers

---

## Deliverables

#### 1. Set up the Flask app in the terminal
- `cd` into `server` and run
`export FLASK_APP=app.py` <br />
`export FLASK_RUN_PORT=5000` <br />
`flask db init` <br />
`flask db revision --autogenerate -m 'Create tables` <br />
`flask db upgrade` <br />
`python seed.py`

#### 2. Import `Api` and `Resource` from flask_restful
- What do these two classes do at a higher level?

#### 3. Initialize the Api

#### 4. Create a Productions class that inherits from Resource
- create a `/productions` resource using the `Productions` class

#### 5. Create a GET (all) route 

#### 6. Create a POST route for `Production` 
- Test the POST route in Postman

#### 7. Create a `ProductionById` class to GET one production
- Create a new resource for `ProductionById` at `/productions/<int:id>`


#### 8. Create a serializer rule for `Production` in `models.py`
- Import `SerializerMixin`
- Pass `SerializerMixin` to `Productions`
- Create a serializer rule to remove `created_at` and `updated_at` from the JSON response

#### 9. Create a `CrewMember` model with the additional following columns:
- name:string, role: string, production_id:integer

#### 10. Create a serializer rule for `CrewMember` that will add `Production` to our response.

