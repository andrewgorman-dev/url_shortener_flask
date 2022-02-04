A simple url shortener with automatic and custom expiry dates
requires python_version 3.9 
Bootstrap 5.1 is required (cdn included in templates/base.html)

To run locally:

activate virtual env: 
pipenv shell

Set environment variables:
export FLASK_APP=app
export FLASK_ENV=development

run app:
python run.py

dependencies/libraries are listed in url_shorten/Pipfile

Database:
SQLAlchemy with sqlite is used for flexibility and simplicity
For scalability this could be replaced with mysql 

