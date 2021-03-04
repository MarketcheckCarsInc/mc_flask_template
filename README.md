# app-engine-flex-python-rest-template
Prerequisite: 
- Python 3+
- install virtualenv  
virtualenv venv
source venv/bin/activate

##test
pip install -r requirements-test.txt 
python3 -m pytest tests -v

##local run 
pip install -r requirements-dev.txt
gunicorn app:application --reload

# Deploy to App Engine
gcloud app deploy
