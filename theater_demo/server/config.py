from flask import Flask
# 2b. import bcrypt
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# 🛑 This is to avoid circular imports
# 1a. move app setup here
app = Flask(__name__)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# 1b. move db setup here
db = SQLAlchemy()
migrate = Migrate(app, db)
db.init_app(app)

# 2c. pass app to bcrypt
bcrypt = Bcrypt(app)

api = Api(app)