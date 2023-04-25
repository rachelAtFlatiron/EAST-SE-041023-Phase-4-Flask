# wrapper for sqlalchemy to use all sqlalchemy methods within a single variable
# save those sqlalchemy methods to db

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
db = SQLAlchemy()

# db.Model will do the same thing as passing base

########################TODO: not null constraint passes on empty strings
class Production(db.Model, SerializerMixin):
    __tablename__ = "productions"

    # use db.Column instead of column
    id = db.Column(db.Integer, primary_key=True)
    # server_default and created_at is a SQL thing I think
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    title = db.Column(db.String, nullable=False, unique=True) 
    genre = db.Column(db.String)
    length = db.Column(db.Integer) 
    year = db.Column(db.Integer) #must be int between 1850 - now
    image = db.Column(db.String, nullable=False) #must be image
    language = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String(50)) #must be less than 50 characters
    composer = db.Column(db.String)

    roles = db.relationship('Role', back_populates='production')
    actors = association_proxy('roles', 'actor')

    serialize_rules = ('-created_at', '-updated_at', '-roles.production')

    @validates('title')
    def not_empty_string(self, key, value):
        return not_empty_string(self, key,value)
        
    @validates('image')
    def validate_image(self, key, image):
        if image == '':
            raise ValueError("image cannot be empty")
        elif('jpg' not in image and 'png' not in image and 'jpeg' not in image):
            raise ValueError('image must be png or jpg')
        else:
            return image 
        
    @validates('year')
    def validates_year(self, key, year):
        if(year > 1850):
            return year 
        else:
            raise ValueError("year must be greater than 1850")
        
    @validates('length')
    def validates_length(self, key, length):
        if(length > 0):
            return length 
        else:
            raise ValueError('length must be greater than 0')
        
        
    def __repr__(self):
        return f"<Production id={self.id}, title={self.title}, genre={self.genre}, length={self.length}, image={self.image}, language={self.language}, director={self.director}, description={self.description} />"


class Actor(db.Model, SerializerMixin):
    __tablename__ = "actors"
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    name = db.Column(db.String, nullable=False, unique=True) #unique constraint
    image = db.Column(db.String, nullable=False) #must be image
    age = db.Column(db.Integer) #must be integer between 1 - 200
    country = db.Column(db.String)

    serialize_rules = ('-created_at', '-updated_at', '-roles.actor')

    roles = db.relationship('Role', back_populates='actor')
    #roles refers to Actor.roles, production is for Role.production
    productions = association_proxy('roles', 'production')

    @validates('age')
    def validate_age(self, key, age):
        if(age < 0 or age > 200):
            raise ValueError('age must be greater than 0 and less than 200')
        else:
            return age
        
    @validates('name', 'image')
    def validate_name_image(self, key, value):
        return not_empty_string(self, key, value)

    def __repr__(self):
        return f"<Actor id={self.id} name={self.name} image={self.image} age={self.age} country={self.country} />"


class Role(db.Model, SerializerMixin):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    actor_id = db.Column(db.Integer, db.ForeignKey('actors.id'), nullable=False) 
    #ForeignKeyConstraint("actor_id", "actor.id")
    production_id = db.Column(db.Integer, db.ForeignKey('productions.id'), nullable=False)
    #ForeignKeyConstraint("production_id", "production.id")
    role_name = db.Column(db.String, nullable=False)

    actor = db.relationship('Actor', back_populates='roles')
    production = db.relationship('Production', back_populates='roles')

    serialize_rules = ('-created_at', '-updated_at',
                       '-actor.roles', '-production.roles')
    
    @validates('role_name')
    def validate_role_name(self, key, value):
        return not_empty_string(self, key, value)

    def __repr__(self):
        return f"<Role id={self.id}, role_name={self.role_name}, actor_id={self.actor_id}, production_id={self.production_id}/>"


def not_empty_string(self, key, value):
    if(value == ''):
        raise ValueError(f'{key} cannot be empty')
    else:
        return value
