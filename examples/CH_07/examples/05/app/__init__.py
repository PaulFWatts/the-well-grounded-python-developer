import os
from flask import Flask
from dynaconf import FlaskDynaconf

def create_app():
    """Initialize the Flask app instance"""

    app = Flask(__name__)
    app.config["SECRET_KEY"] = "c86a3084b86da703506b310d41f47f42f199349b7f48f2ca"
    bytearray(app.config["SECRET_KEY"], "utf-8")
    
    dynaconf = FlaskDynaconf(extensions_list=True)

    with app.app_context():

        # initialize plugins
        os.environ["ROOT_PATH_FOR_DYNACONF"] = app.root_path
        dynaconf.init_app(app)

        # import the routes
        from . import intro

        # register the blueprints
        app.register_blueprint(intro.intro_bp)

        return app
