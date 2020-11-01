# __init__.py
import flask
from app import db
from app.utils import ModelMixin
from app.blueprints.auth.models import User

blueprint = flask.Blueprint("main", __name__)

from . import views, models
