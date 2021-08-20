from flask import Flask
from flask_sqlalchemy import SQLAlchemy


from config import config

db = SQLAlchemy()



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    #blueprints
    from app.login import login
    app.register_blueprint(login, url_prefix='/login/')
    print(app.url_map)

    return app
