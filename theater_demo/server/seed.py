#!/usr/bin/env python3

# 4a. Imports
from app import app
from models import Production, db

# 🛑 already initialized SQLAlchemy instance with db.init_app(app)

# 4b. Create application context `with app.app_context():`
with app.app_context():

    # 4c. Create a query to delete all existing records from Production
Production.query.delete()

# 4d. Create some seeds for production and commit them to the database.
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

   # 5. Check seeds
   # `python seed.py`
   # `flask shell`
   # from app import app
   # from models import Production
   # Check the seeds by querying Production
