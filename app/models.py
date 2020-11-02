# models.py
import flask_login
from flask_login import UserMixin, current_user
import werkzeug
from sqlalchemy.ext.hybrid import hybrid_property
from flask_admin.contrib.sqla import ModelView

from . import db
from .utils import ModelMixin

class User(UserMixin, db.Model): # SQL Table

    # Create attributes (SQL columns)
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64))
    _password_hash    = db.Column(db.String(256))
    reservation = db.relationship('Reservation', backref='user', lazy=True)

    @classmethod
    def login_user(cls, name, pwd):
        user = cls.query.filter_by(username=name).first()
        if user and user.check_password(pwd):
            flask_login.login_user(user)
            return user
        return False

    @hybrid_property
    def password(self):
        return self._password_hash

    @password.setter
    def password(self, pwd):
        self._password_hash = werkzeug.security.generate_password_hash(pwd)

    def check_password(self, pwd):
        return werkzeug.security.check_password_hash(self._password_hash, pwd)

    def __repr__(self):
        return f"<User {self.id}-{self.username}>"


class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    rooms_number = db.Column(db.Integer)
    reservation = db.relationship('Reservation', backref='hotel', lazy=True)
    image1 = db.Column(db.String(256))
    image2 = db.Column(db.String(256))
    image3 = db.Column(db.String(256))
    image4 = db.Column(db.String(256))

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'), nullable=False)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)

class  MyModelView(ModelView):
    pass
