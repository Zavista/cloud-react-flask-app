from flask import Flask
from .db import db
from .config import SQLALCHEMY_DATABASE_URI
from app.routes import register_routes

def create_app():
    app = Flask(__name__)

    # load config from config.py
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # initializes postgresql database
    db.init_app(app)


    # creates users table if not previosuly created
    with app.app_context():
        db.create_all()

    # registers Blueprints (routes) from the routes folder
    register_routes(app)

    return app