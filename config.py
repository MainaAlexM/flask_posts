import os
from decouple import config

class Config:
    '''
    General configuration parent class
    '''

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = config('KEY')
    # SECRET_KEY = os.getenv['KEY']
    # SECRET_KEY = os.environ.get('KEY')

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL')

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL')

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
