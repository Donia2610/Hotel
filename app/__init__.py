# __init__.py
import flask
from config import config
import os

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin

db  = SQLAlchemy()
migrate = Migrate()
login_mgr = LoginManager()
admin = Admin(template_mode='bootstrap4')


def create_app():
    from .models import User, Hotel, Reservation
    from app.users.views import users

    env=os.environ.get("FLASK_ENV", "development")
    print("Using config", env)

    app = flask.Flask(__name__) # __name__ is the name of the folder
    app.config.from_object(config[env])

    app.register_blueprint(users)
   



    db.init_app(app)
    migrate.init_app(app, db)
    login_mgr.init_app(app)
    admin.init_app(app)



    @app.shell_context_processor
    def shell_ctx():
        return {
            "User": User,
            "app": app,
            "db": db,
            "auth": auth,
            "main":main
        }

    @login_mgr.user_loader
    def user_loader(user_id):
        return User.query.get(user_id)


    return app


