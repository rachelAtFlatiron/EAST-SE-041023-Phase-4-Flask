# REST APIs with Flask Part 1

## SWBATs

- [ ] Discuss MVC architecture
- [ ] Explain the concept of REST and RESTful naming conventions
- [ ] Build and execute a GET and POST request
- [ ] Use Postman to interact with Flask
- [ ] Use serializers

---

## Deliverables

#### 1. Create a `CrewMember` model with the additional following columns:
- name:string, role: string, production_id:integer
##### 1a. Include some seed data

<br />

#### 2. Set up the Flask app in the terminal
- `cd` into `server` and run
`export FLASK_APP=app.py` <br />
`export FLASK_RUN_PORT=5000` <br />
`flask db init` <br />
`flask db revision --autogenerate -m 'Create tables` <br />
`flask db upgrade` <br />
`python seed.py`

<br />

#### 3. Import `Api` and `Resource` from flask_restful
- What do these two classes do at a higher level?
##### 3a. Initialize the Api

<br />

#### 4. Create a Productions class that inherits from Resource
##### - create a `/productions` resource using the `Productions` class
##### 4a. Create a GET (all) productions route 
##### - Do this by manually building out the dictionary

<br />

#### 5. Use SerializerMixin so we don't have to manually build the dictionary
##### - Import `SerializerMixin`
##### - Pass `SerializerMixin` to `Productions`

<br />

#### 6. Create a serializer rule for `Production` in `models.py` to remove `created_at` and `updated_at` from the JSON response

<br />

#### 7. Set up a one-to-many relationship between `CrewMember` and `Production`
##### 7a. Make sure you include your cascades 

<br />

#### 8. Create a serializer rule for `CrewMember` that will appropriately add `Production` to our response.
##### 8a. Update serializer rules in `Production` so that we don't error out

<br />

#### 9. Create a `ProductionById` class to GET one production
##### - Create a new resource for `ProductionById` at `/productions/<int:id>`

<br />

#### 10. Create a POST route for `Production`
##### 10a. import `request` and use it to get info from the request
##### 10b. use `ipdb` to check out `request` (try `.path`, `.get_json()`, and `.host`)

##### - Test the POST route in Postman (or Insomnia)

<br />

#### 11. Create a POST route for `CastMember`

