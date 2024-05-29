from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)  # Set the secret key to something unique and secret

    with app.app_context():
        from . import routes
        return app
