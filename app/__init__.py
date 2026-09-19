from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#create database object globally
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # Tells SQLAlchemy to work with this Flask app and use its configuration.


    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp

    app.register_blueprint(auth_bp)  # register_blueprint() tells the Flask app to use/include the routes from that Blueprint. 👍
    app.register_blueprint(tasks_bp)

    return app
