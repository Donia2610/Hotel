# __init__.py
import flask
from app import db  # .. is previous folder
from app.utils import ModelMixin



users = flask.Blueprint("users", __name__)

from . import views
from app import models
