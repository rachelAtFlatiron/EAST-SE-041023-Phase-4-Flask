---

title: '01_intro_flask'

---

# Intro to Flask

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

## What is The Internet

- Architecture 
- Connects networks across the Earth
- Ocean cables 
- Computers
- Data Centers
- Servers
- Sattelites
- Wifi towers

---

## What is The Internet

<img src='https://www.gao.gov/assets/extracts/726c56e9ccd46e3aaf3e4b7b75c60895/rId15_image3.png' width="800px" />

<aside class="notes">
Fun Fact: ARPANET was the initial backbone of the internet which was created by the Department of Defense
- packet switching: grouping data into packets that are transmitted over a digital network (with a header and payload)
- metaphor: header = envelope, payload = contents inside envelope
- response is a promise because it takes time for information to travel from wherever it originated, that's why I always say "we wait for the response to be fulfilled"
</aside>

---

## WWW: World Wide Web

- Web resources accessed via HTTP (HyperText Transfer Protocol)


---

## HTTP Protocol

- Hypertext Transfer Protocol
- Designed in the early 90s
- Stateless: one request doesn't know about the next
- Sessions: share info b/w requests by storing user info on the server
<aside class="notes"> sessions usually expire over a certain period of time </aside>
- Cookies: saved in the user's browser and saves users identity (usually anonymously)...this also expires over a certain period of time

<img src="https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview/fetching_a_page.png" width="900px"/>

<aside class="notes">
What is a protocol? A set of rules on how something should be done.
HTTP is the protocol describing the structure between client and server communication 
</aside>

---

## Other Protocols Include...

- SSH (secure shell) which we've been using in Github
- HTTPS: hypertext transfer protocol secure
- SSL (secure sockets layer)
- IMAP (internet message access protocol)
- DNS (domain name system) 
etc ... 

<aside class="notes">
- ssl: establishes encrypted link between server and client
- imap: stores emails on a mail server 
- dns: domain names database - this is why hosting a website and hosting the domain name happen in two different places
</aside>

---

## Static vs Dynamic Website

- static website (doesn't change) is just HTML, CSS JS, almost acts as template for dynamic data coming into these pages

<img src="https://rochester.kidsoutandabout.com/sites/default/files/html_css_javascript.jpeg" width="600px" />

- dynamic software content is supplied by server.  a user makes a request, and the server sends back a response

<aside class="notes">
- websites (single domain pages on the web)
- web apps (software accessible through the web)
</aside>

---

## Request Reponse Cycle

👀 What is the request-response cycle?

---

## Request Reponse Cycle

<img src="https://www.oreilly.com/api/v2/epubs/9780596802462/files/images/ugae_0104.png"/>

- client makes request to server which may contain additional data
- server responds with information which my contain data or an error
- client waits for response (as a promise)

<aside class="notes">
- this goes back to the transferring of data packets
- response is a promise because it takes time for information to travel from wherever it originated, that's why I always say "we wait for the response"
</aside>

---

## URL Example

- https://pokeapi.co/api/v2/pokemon/ditto <br /> <br />
https - protocol <br />
pokeapi.co - domain name <br />
api/v2/pokemon/ditto - path

<aside class="notes">
- use an example from github where you change the user who owns the repo, the branch name, etc.
- semantic ui github: https://github.com/Semantic-Org/Semantic-UI
- use an example by having a student's fork of repo and changing URL to navigate to my repo
- display wikipedia (they have search query)
</aside>

---

## Status Codes

😎 <br />
200: `OK` - yay
<br />
201: `Created` - you probably did a POST request

<aside class="notes">
100's - informational
200's - success
300's - redirect
400's - client error
500's - server error
</aside>

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

<aside class="notes">
- It’s a format to transfer data from client to server
- sometimes have to specify you will be sending JSON or expecting JSON
</aside>

---

## Flask

---

## Why Flask

- built in debugger
- easily scalable
- secure cookies
- unit testing support
- lots of extensions
- small codebase - lots of control for developers

<aside class="notes">
- easy to extend core: flask has a lot of packages to add on, flask itself is very lightweight
</aside>

---

## Why Flask 

- WSGI (WIZ-ghee): web server gateway interface
    - interface between web servers (Apache, Nginx, local development server) and web apps
    - specifically for Python frameworks
- Werkzeug: WSGI library
    - toolkit that implements requests, response objects and other utility functions
    - debugger, classes to build requests and process responses, routing, making dev server
- Flask provides a development WSGI through Werkzeug with `flask run` command

<aside class="notes">
- web apps are software accessed/ran via internet
</aside>

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
<br />

`SQLALCHEMY_RECORD_QUERIES`: setting to record queries
<br />

`SQLALCHEMY_POOL_TIMEOUT`: speicfies connection timeout in seconds
<br />

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

`flask run --debug`
