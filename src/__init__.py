from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from importlib import import_module
import os
from .active_modules import MODULES, API_MODULES
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()
jwt = JWTManager()

from src.modules.apps.models import *
from src.modules.logs.models import *


def register_extensions(app):
    db.init_app(app)
    jwt.init_app(app)
    admin = Admin(app, name="omc-admin", template_mode="bootstrap3")
    register_admin_models(admin)


def register_blueprints(app):
    for module_name in MODULES:
        module = import_module("src.modules.{}.routes".format(module_name))
        app.register_blueprint(module.blueprint)


def register_api(app):
    for module_name in API_MODULES:
        module = import_module("src.api.{}.routes".format(module_name))
        app.register_blueprint(module.blueprint)


def register_admin_models(admin):
    admin.add_view(ModelView(Apps, db.session))
    admin.add_view(ModelView(Logs, db.session))


def configure_database(app):
    with app.app_context():
        try:
            db.create_all()
        except Exception as e:
            print("> Error: DBMS Exception: " + str(e))

            # fallback to SQLite
            basedir = os.path.abspath(os.path.dirname(__file__))
            app.config[
                "SQLALCHEMY_DATABASE_URI"
            ] = SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
                basedir, "db.sqlite3"
            )

            print("> Fallback to SQLite ")
            db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def create_app(config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    register_api(app)
    configure_database(app)

    return app
