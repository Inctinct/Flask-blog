 # Flask-blog

Install requirements: 
  pip install Flask 
  pip install Flask_SQLAlchemy
  pip install flask_migrate 
  pip install psycopg2

Create database. I am using postgres. To work correctly, you need to manually create the database.
And specify the correct path to the database:
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://username:pass@localhost:port/name_database'
