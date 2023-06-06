from sqlalchemy_serializer import SerializerMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy
# 9a. import validates from sqlalchemy.orm
from sqlalchemy.orm import validates 
db = SQLAlchemy()

class Production(db.Model, SerializerMixin):
    __tablename__ = "productions"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # 8a. add constraints 
    # 🛑 If you see 'Constraint: must have a name'
    # 🛑 Add render_as_batch=True in Migrate(app, db, ...) in app.py
    title = db.Column(db.String, nullable=False, unique=True) # 8a. not null, unique
    genre = db.Column(db.String) 
    length = db.Column(db.Integer) 
    year = db.Column(db.Integer) 
    image = db.Column(db.String, nullable=False) # 8a. required
    language = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String(50)) # 8a. at least 50 chars
    composer = db.Column(db.String)

    roles = db.relationship('Role', back_populates='production')
    actors = association_proxy('roles', 'actor')
    
    serialize_rules = ('-created_at', '-updated_at', '-roles.production', '-actors.productions')

    # 9b. validation: image must be 'png', 'jpg', or 'jpeg'
    @validates('image')
    def validate_image(self, key, image):
        if image == '':
            raise ValueError("image cannot be empty")
        elif('jpg' not in image and 'png' not in image and 'jpeg' not in image):
            raise ValueError('image must be png or jpg')
        else:
            return image 
    # 9b. validation: year must be > 1850
    @validates('year')
    def validates_year(self, key, year):
        if(year > 1850):
            return year 
        else:
            raise ValueError("year must be greater than 1850")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Actor(db.Model, SerializerMixin):
    __tablename__ = "actors"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    #8b. add constraints
    name = db.Column(db.String, nullable=False, unique=True) # 8b. required, unique
    image = db.Column(db.String, nullable=False) # 8b. required
    age = db.Column(db.Integer)
    country = db.Column(db.String)

    roles = db.relationship('Role', back_populates='actor')
    productions = association_proxy('roles', 'production')

    serialize_rules = ('-created_at', '-updated_at', '-roles.actor', '-productions.actors')

    # 9c. validation: age must be between 0 and 200
    @validates('age')
    def validate_age(self, key, age):
        if(age < 0 or age > 200):
            raise ValueError('age must be greater than 0 and less than 200')
        else:
            return age
    # 9d. test in sqlite3 and Postman
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Role(db.Model, SerializerMixin):
    __tablename__ = "roles"
    
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
   
    # 8c. add constraints
    role_name = db.Column(db.String, nullable=False) # 8c. required
    # 8d. test in sqlite3 and Postman
    
    production_id = db.Column(db.Integer, db.ForeignKey('productions.id'), nullable=False) # 8c. required
    production = db.relationship('Production', back_populates='roles')

    actor_id = db.Column(db.Integer, db.ForeignKey('actors.id'), nullable=False) # 8c. required
    actor = db.relationship('Actor', back_populates='roles')

    serialize_rules = ('-created_at', '-updated_at', '-production.roles', '-actors.roles')


