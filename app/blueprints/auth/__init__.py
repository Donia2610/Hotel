# __init__.py
import flask
from app import db  # .. is previous folder
from app.utils import ModelMixin


blueprint = flask.Blueprint("auth", __name__)

from . import views, models

