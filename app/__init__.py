from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap()
db = SQLAlchemy(app)


def create_pitch(config_name):
    
    app.config.from_object(config_options[config_name])
    # ....

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    return app

