# Deliverables

### 1. Use gunicorn to start the client and server
#### 1a. Install `gunicorn`, `honcho`, and `flask-cors`
#### 1b. Create a `Procfile.dev` file and write:
```js
web: PORT=3000 npm start --prefix client
api: gunicorn -b 127.0.0.1:5555 --chdir ./server
```
#### 1c. In terminal run `honcho start -f Procfile.dev`
<br />

