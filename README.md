# Python flask template for Google App Engine

## Prerequisite: 
- Python 3+
- virtualenv  

## Features
- Flask Restful and Blueprint 
- Flask swagger UI
- Pytest

## First time, create virtual env, after cloning /checkout of code.
 - virtualenv venv
 - source venv/bin/activate

## test
 - pip install -r requirements-test.txt 
 - python -m pytest tests -v

## local run 
 - pip install -r requirements-dev.txt
 - gunicorn app:application --reload
 - http://localhost:8000/api/v1/demo/1
 - http://localhost:8000/api/v1/demo/2
   - Add below env vars in a .env file (same level as main.py)
     - GCP_PROJECT = ""
     - BT_INSTANCE = ""
     - BT_MAPPING  =  <>  ex: "{'price': 'p', 'miles': 'mi'}"
     - BT_TABLE_NAME = ""
     - BT_ROW_KEYS = ""
     - GOOGLE_APPLICATION_CREDENTIALS = "credentials/credential.json" (same level as main.py)
 - http://localhost:8000/api/v1/docs

# Deploy to App Engine
 - gcloud app deploy
   - update app.yaml with vars and network tag


Join the discussion @[Marketcheck forums](https://forums.marketcheck.com/) 
