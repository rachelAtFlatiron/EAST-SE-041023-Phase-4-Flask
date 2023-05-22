#!/usr/bin/env python3

# 5. ✅ Imports
    # app from app
    # db and Production from models

# 6. ✅ Initialize the SQLAlchemy instance with `db.init_app(app)`


# 7. ✅ Create application context `with app.app_context():`
    # Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/

# 8.✅ Create a query to delete all existing records from Production    
   
# 9.✅ Create some seeds for production and commit them to the database. 

#   amsterdam = Production(
#         title="amsterdam",
#         genre="mystery",
#         image="https://m.media-amazon.com/images/M/MV5BNDQwNzE0ZTItYmZjMC00NjI3LWFlNzctNTExZDY2NWE0Zjc0XkEyXkFqcGdeQXVyMTA3MDk2NDg2._V1_FMjpg_UX1000_.jpg",
#         length=134,
#         director="david o russell",
#         composer="daniel pemberton",
#         description="let the love, murder, and conspiracy begin"
#     )

#     nope = Production(
#         title='nope',
#         genre='sci-fi',
#         image='https://m.media-amazon.com/images/M/MV5BOGJhYzAwN2MtNjA1Ny00ZjJiLWFmNzYtMDgzNTUzYjc5NTIzXkEyXkFqcGdeQXVyMTUzOTcyODA5._V1_.jpg',
#         length=130,
#         director='jordan peele',
#         composer='michael abels',
#         description='nope'
#     )

# 10.✅ Run in terminal:
    # `python seed.py`

# 11.✅ run `flask shell` in the terminal 
    # from app import app
    # from models import Production
    # Check the seeds by querying Production

# 12.✅ Navigate back to app.py  
    