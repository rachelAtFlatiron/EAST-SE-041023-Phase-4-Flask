#wrapper for sqlalchemy to use all sqlalchemy methods within a single variable
# save those sqlalchemy methods to db 

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#db.Model will do the same thing as passing base
class Production(db.Model):
    __tablename__ = "productions" 

    #use db.Column instead of column
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genre = db.Column(db.String)
    budget = db.Column(db.Float)
    image = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String)
    ongoing = db.Column(db.Boolean)

    cast_members = db.relationship('CastMember', backref='production')
    #server_default and created_at is a SQL thing I think
    created_at = db.Column(db.DateTime, server_default=db.func.now()) 
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())   

    def __repr__(self):
        return f"<Production id={self.id}, title={self.title}, genre={self.genre}, budget={self.budget} />"

class CastMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)
    role = db.Column(db.String)
    production_id = db.Column(db.Integer, db.ForeignKey('productions.id'))

    created_at = db.Column(db.DateTime, server_default=db.func.now()) 
    updated_at = db.Column(db.DateTime, onupdate=db.func.now()) 