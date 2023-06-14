from sqlalchemy_serializer import SerializerMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy
db = SQLAlchemy()

class Production(db.Model, SerializerMixin):
    __tablename__ = "productions"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    title = db.Column(db.String)
    genre = db.Column(db.String) 
    length = db.Column(db.Integer) 
    year = db.Column(db.Integer) 
    image = db.Column(db.String)
    language = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String())
    composer = db.Column(db.String)

    #all of the roles for the current production
    production_roles = db.relationship('Role', back_populates='production')
    actors = association_proxy('production_roles', 'actor')
    
    # 1c. update the serializers for all three classes
    serialize_rules = ('-created_at', '-updated_at')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 1a. Review
# 1b. run flask db init, flask db migrate, flask db upgrade, python seed.py
class Actor(db.Model, SerializerMixin):
    __tablename__ = "actors"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    name = db.Column(db.String)
    image = db.Column(db.String)
    age = db.Column(db.Integer)
    country = db.Column(db.String)

    #all of the roles that belong to current actor
    actor_roles = db.relationship('Role', back_populates='actor')
    productions = association_proxy('actor_roles', 'production')

    # 1c. update the serializers for all three classes
    serialize_rules = ('-created_at', '-updated_at', '-actor_roles.actor', '-actor_roles.production')
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Role(db.Model, SerializerMixin):
    __tablename__ = "roles"
    
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    role_name = db.Column(db.String)
    
    #a role has one production
    production_id = db.Column(db.Integer, db.ForeignKey('productions.id'))
    production = db.relationship('Production', back_populates='production_roles')

    #a role has one actor
    actor_id = db.Column(db.Integer, db.ForeignKey('actors.id'))
    actor = db.relationship('Actor', back_populates='actor_roles')

    # 1c. update the serializers for all three classes
    serialize_rules = ('-created_at', '-updated_at', '-actor.actor_roles', '-production.production_roles')

