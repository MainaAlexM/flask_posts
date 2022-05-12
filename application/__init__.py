import imp
from flask import Blueprint
from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
# from flask_mail import Mail
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_login import LoginManager
from config import config_options


main_blueprint = Blueprint('main',__name__)


bootstrap = Bootstrap()
db = SQLAlchemy()
# mail = Mail()
photos = UploadSet('photos',IMAGES)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):

    app = Flask(__name__)

    # Application configuration
    app.config.from_object(config_options[config_name])

    # Initializing app extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    # mail.init_app(app)

    # Registering the blueprint
    app.register_blueprint(main_blueprint)

    # configuring UploadSet
    configure_uploads(app,photos)

    return app

