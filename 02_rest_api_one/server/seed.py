#!/usr/bin/env python3

from app import app
from models import Production, db

with app.app_context():

   Production.query.delete()

   amsterdam = Production(
       title="amsterdam",
       genre="mystery",
       image="https://m.media-amazon.com/images/M/MV5BNDQwNzE0ZTItYmZjMC00NjI3LWFlNzctNTExZDY2NWE0Zjc0XkEyXkFqcGdeQXVyMTA3MDk2NDg2._V1_FMjpg_UX1000_.jpg",
       length=134,
       director="david o russell",
       composer="daniel pemberton",
       description="let the love, murder, and conspiracy begin"
   )

   nope = Production(
       title='nope',
       genre='sci-fi',
       image='https://m.media-amazon.com/images/M/MV5BOGJhYzAwN2MtNjA1Ny00ZjJiLWFmNzYtMDgzNTUzYjc5NTIzXkEyXkFqcGdeQXVyMTUzOTcyODA5._V1_.jpg',
       length=130,
       director='jordan peele',
       composer='michael abels',
       description='nope'
   )

   db.session.add_all([amsterdam, nope])
   db.session.commit()
