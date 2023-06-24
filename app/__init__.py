from flask import Flask
from flask_session import Session

from .views import main

from config import Config


def Create_App():

    app = Flask(__name__)
    app.config.from_object(Config)
    Session(app)

    app.register_blueprint(main)

    return app