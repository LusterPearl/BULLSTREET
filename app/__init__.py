from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig, ProductionConfig



"""initialize sqlalchemy"""
db = SQLAlchemy()


def create_app(config_name='development'):
    """create a flask app instance"""
    app = Flask(__name__)

    """ Load the configuration based on the environment"""
    if config_name == 'development':
        app.config.from_object(DevelopmentConfig)
    elif config_name == 'production' :
        app.config.from_object(ProductionConfig)
    else: 
       app.config.from_object(DevelopmentConfig) 

    """initialize sqlalchemy with the app"""
    db.init_app(app)
    
    print(f"SECRET_KEY: {app.config['SECRET_KEY']}")
    print(f"DATABASE_URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
    
    """return the app instance"""
    return app
