#SQLAlchemy import
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# 1. ✅ Create a Production Model
	# tablename = 'Productions'
	# Columns:
        # title: string, genre: string, length:integer, year:integer, image:string, language:string, director: string, description:string, composer:string, created_at:date time, updated_at: date time 
# 2. ✅ navigate to app.py