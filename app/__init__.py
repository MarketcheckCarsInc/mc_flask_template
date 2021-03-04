"""
Primary Flask app

"""
from flask import Flask
from flask_restful import Api

from .api import api as api_blueprint
from .errors import add_error_handlers
from .api.routes import initialize_routes



def create_app():
    app = Flask(__name__)
    api = Api(app)
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')
    add_error_handlers(app)
    initialize_routes(api)
    return app


application = create_app()
