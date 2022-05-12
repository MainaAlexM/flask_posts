from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_login import LoginManager
from config import config_options
from main import main as main_blueprint


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
    Mail.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    # configuring UploadSet
    configure_uploads(app,photos)

    return app

