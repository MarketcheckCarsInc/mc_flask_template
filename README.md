# Python flask templat for Google App Engine

## Prerequisite: 
- Python 3+
- virtualenv  

## Features
- Flask Restful and Blueprint 
- Flask swagger UI
- Pytest

## First time, create virtual env
 - virtualenv mft
 - source mft/bin/activate

## test
 - pip install -r requirements-test.txt 
 - python -m pytest tests -v

## local run 
 - pip install -r requirements-dev.txt
 - gunicorn app:application --reload
 - https://localhost:8080/api/v1/demo1/1
 - https://localhost:8080/api/v1/demo1/1
 - https://localhost:8080/api/v1/docs

# Deploy to App Engine
 - gcloud app deploy
