---

title: '01_intro_flask'

---

# Intro to Flask

<aside class="notes">
    Shhh, these are your private notes 📝
</aside>

---

✅ Objectives
- [ ] Understand how the Internet works
- [ ] Understand how the request-response cycle works
- [ ] Understand HTTP protocols
- [ ] Intialize a Flask application
- [ ] Understand how to use SQLAlchemy within Flask
- [ ] Use Flask routing and create views
- [ ] Use the Flask shell 

---

## What is The Internet?

---

<img src='https://media-cldnry.s-nbcnews.com/image/upload/newscms/2015_34/1182941/theinternet-egodeath-coverart.jpg' width='500px' />

---

## Also The Internet

<img src='https://www.gao.gov/assets/extracts/726c56e9ccd46e3aaf3e4b7b75c60895/rId15_image3.png' width="800px" />

---

## WWW

- websites (single domain pages on the web)
- web apps (software accessible through the web)

---

## Static vs Dynamic Website
- static website (doesn't change) is just HTML, CSS JS, almost acts as template for dynamic data coming into these pages
- dynamic software content is supplied

---

## Request Reponse Cycle

👀 What is the request-response cycle?

---

## Request Reponse Cycle

<img src="https://www.oreilly.com/api/v2/epubs/9780596802462/files/images/ugae_0104.png"/>

- client makes request to server which may contain additional data
- server responds with information which my contain data or an error
- client waits for response (as a promise)

---

## Client
- user interface
- responsible for styling, layout, event functionality
- lightweight and loads fast
- acts as a template for dynamic data
- makes request to a web server using HTTP protocols

---

## Web Server
- responsible for data storage and management
- changes in data may be triggered by the client but the actual change is handled by the server side
- sends a rewsponse back to the client
- uses HTTP proto cols to respond to requests

---

## API (Application Programming Interface)

- APIs
    - tools, including libraries, functions, methodsused for building server applications
    - not specific to web dev
- Web APIs
    - specific to interfacing with the web
    - used to build out functionality with web browsers and web servers

---

## URL Example

EX
- https://pokeapi.co/api/v2/pokemon/ditto
https - protocol
pokeapi.co - domain name
api/v2/pokemon/ditto - path

---

## HTTP Protocol

- Designed in the early 90s
- Stateless: one request doesn't know about the next
- Sessions: share info b/w requests by storing user info on the server
    - Sessions usually expire over a certain period of time
- Cookies: saved in the user's browser and saves users identity (usually anonymously)...this also expires over a certain period of time

<img src="https://www.oreilly.com/api/v2/epubs/9780596802462/files/images/ugae_0104.png" />

---

## HTTP Syntax

Fetch request syntax
<img src="#"/>
Response syntax
<img src="#"/>

---

## Status Codes

😎 <br />
200: `OK` - yay
<br />
201: `Created` - you probably did a POST request

---

## Status Codes 
😕
<br />
400: `Bad Request` - there's probably something wrong with your fetch in the client
<br />
401: `Unauthorized` - are you logged in?
<br />
404: `Not Found` - maybe that record doesn't exist 

--- 

## Status Codes

😰 <br />
500: `Internal Server Error` - hopefully it's just a typo

---

## More Status Codes

[🐶](https://httpstatusdogs.com/) <br />
(click me ^)

---

## CRUD vs HTTP verbs

<img src="https://www.atatus.com/blog/content/images/2022/12/crud-operations.png" width="500px" />

---

## JSON

- lightweight data storage for data exchange
- works with any language
- easy to read
- sometimes have to specify you will be sending JSON or expecting JSON

---

## Flask

- used to build web apps
- written in python
- easy to extend core (flask doesn't start with an ORM like SQLAlchemy)
    - flask SQLAlchemy
- WSGI
    - web server gateway interface
    - interface between web servers and apps
- Werkzeug
    - toolkit that implements requests, response objects and other utility functions
    - debugger, classes to build requests and process responses, routing, making dev server
- Flask provides a development WSGI through Werkzeug with `flask run`

---
## Why Flask
- built in debugger
- easily scalable
- secure cookies
- unit testing support
- easy to learn, straightforward
- lots of extensions
- small codebase - lots of control for developers

---
## Initializing a Flask App

```js
app = Flask('mynameiswhat')
```

That's it!

---

## Connecting Flask with SQLAlchemy

1. configure the database path you want a connection with
- database path is referred to as URI = Uniform Resource Identifier
```js
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///path/to/db.db'
```
2. configure whether SQLAlchemy should track modifications to objects (inserts, updates, etc.)
```js
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```
- this will use less memory
- we may get an error if we don't have this set

3. create an instance of the db 
```js
db = SQLALchemy(app)
```

---

## Flask-SQLAlchemy [Configuration Keys](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/)

- There are a few other configuration keys such as...

`SQLALCHEMY_RECORD_QUERIES`: setting to record queries
`SQLALCHEMY_POOL_TIMEOUT`: speicfies connection timeout in seconds
`SQLALCHEMY_ECHO`: SQLAlchemy will log all errors if set to True

---

## Creating a Route in Flask

Use a decorator!

```js
@app.route('/', methods=['GET', 'POST', ...])
def home():
    if request.method == 'GET':
        return {} 
```

---

## What do we send back?

### 🌈 JSON ✨
- We can add additional information to our response such as headers, status code, etc. with `make_response()`

---


## Request lifecycle
`@app.before_request`
`@app.after_request`
and more!...

```js
@app.before_request
def run_before():
    print('this is really useful when checking if a user is logged in')
```

---


## Context

- Application Context: Keeps track of config variables, logger, database connections so that we don't have to pass the entire application from function to function
- Request Context: Keeps track of request data such as URL, headers, method, request data, etc.

---

## Debugging

`import ipdb; ipdb.set_trace()`
<br />

`@app.before_request`