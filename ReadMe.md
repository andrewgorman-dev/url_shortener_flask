A simple url shortener with automatic and custom expiry dates 

To run locally:

activate virtual env: 
pipenv shell

Set environment variables:
export FLASK_APP=app
export FLASK_ENV=development

run app:
python run.py

Database:
SQLAlchemy with sqlite is used for flexibility and simplicity
For scalability this could be replaced with mysql 

dependencies are listed in url_shorten/Pipfile