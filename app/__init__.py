"""
Primary Flask app

"""
import os
from flask import Flask
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint

from .api import api as api_blueprint
from .errors import add_error_handlers
from .api.routes import initialize_routes



def create_app():
    app = Flask(__name__)
    api = Api(app)
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    ###swagger start
    SWAGGER_URL = '/api/v1/docs'  # URL for exposing Swagger UI (without trailing '/')
    API_URL = '/static/swagger.json'

    # Call factory function to create our blueprint
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        API_URL,
        config={  # Swagger UI config overrides
            'app_name': "Demo application"
        },
        # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
        #    'clientId': "your-client-id",
        #    'clientSecret': "your-client-secret-if-required",
        #    'realm': "your-realms",
        #    'appName': "your-app-name",
        #    'scopeSeparator': " ",
        #    'additionalQueryStringParams': {'test': "hello"}
        # }
    )
    app.register_blueprint(swaggerui_blueprint)
    ###swagger end

    add_error_handlers(app)
    initialize_routes(api)
    return app


application = create_app()
