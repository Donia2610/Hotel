#https://jamboard.google.com/d/1QkuB6jm7vekd6GwiLoENPpBq_kBgEfMF52uM8pK9Z4g/edit?usp=meet_whiteboard views.py
import flask, flask_login

from . import forms
from app import db, admin

from app.models import User, MyModelView, Hotel, Reservation
from app.users.forms import SigninForm, SignupForm

users = flask.Blueprint('users', __name__)

admin.add_view(MyModelView(User,db.session))
admin.add_view(MyModelView(Hotel,db.session))
admin.add_view(MyModelView(Reservation,db.session))


@users.route("/", methods=["GET", "POST"])
@users.route("/home", methods=["GET", "POST"])
def index():
    return flask.render_template("index.html", title="My awesome blueprint")

@users.route("/sign-up", methods=["GET", "POST"])
def signup():
    form = forms.SignupForm()

    if flask.request.method == "POST":
        if form.validate_on_submit():

            user = User()
            user.username = form.username.data
            user.password = form.password.data

            db.session.add(user)
            db.session.commit()
         

            flask.flash("User has been successfully registered", category="success")

            return flask.redirect('/')
        else:
            print("Form errors:", form.errors)

    return flask.render_template("signup.html", form=form)


@users.route("/sign-in", methods=["GET", "POST"])
def signin():
    form = forms.SigninForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.login_user(username, password)
        if user:
            return flask.redirect('/')
        else:
            flask.flash("Bad credentials", category="error")

    return flask.render_template("signin.html", form=form)

@users.route("/sign-out")
def signout():
    flask_login.logout_user()
    flask.flash("Goodbye !", category="message")
    return flask.redirect('/')

@users.route("/locations")
def countries():
    hotel_locations = Hotel.query.all()

    return flask.render_template("countries.html",title ='Hotel Locations',hotel_locations = hotel_locations)

