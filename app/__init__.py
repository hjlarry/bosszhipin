from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from common.config import config




def create_app():
    app = Flask(__name__)
    app.config.from_object(config['default'])
    # db.init_app(app)

    return app


db = SQLAlchemy(create_app())