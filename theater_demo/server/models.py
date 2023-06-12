#SQLAlchemy import
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# 1. Create a Production Model
class Production(db.Model):
    __tablename__ = "productions" 

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    update_at = db.Column(db.DateTime, onupdate=db.func.now())

    title = db.Column(db.String)
    genre = db.Column(db.String)
    image = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String)
    year = db.Column(db.Integer)
    composer = db.Column(db.String)
    length = db.Column(db.Integer)


# 2. navigate to app.py