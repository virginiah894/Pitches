from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
# from main import views

# from flask_simplemde import SimpleMDE
app = Flask(__name__)
bootstrap = Bootstrap()
db = SQLAlchemy(app)
# simple = SimpleMDE
# defining what files are uploaded
photos = UploadSet('photos',IMAGES)
mail= Mail()
login_manager= LoginManager()
login_manager.session_protection = 'strong'
# prefix with the blueprint where it is located
login_manager .login_view = 'auth.login'

def create_app(config_name):
    
    app.config.from_object(config_options[config_name])
    # config_options[config_name].init_app(app)
    # ....
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # Initializing flask extensions
    bootstrap.init_app(app)
    # initializing database
    db.init_app(app)
    # initialize the login manager
    login_manager.init_app(app)
    # register and add prefix prefixes as arguments
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix ='/authenticate')
# settings for uploads
    configure_uploads(app,photos)
    mail.init_app(app)
    # simple.init_app(app)

    
    return app

