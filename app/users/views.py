#https://jamboard.google.com/d/1QkuB6jm7vekd6GwiLoENPpBq_kBgEfMF52uM8pK9Z4g/edit?usp=meet_whiteboard views.py
import flask, flask_login
from flask_login import current_user
from flask import session
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
    return flask.render_template("index.html", title="Dhotels")

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

@users.route("/reservations/<user_id>")
def reservations(user_id):
    

    reservations_list = Reservation.query\
        .join(Hotel, Reservation.hotel_id == Hotel.id)\
        .filter(Reservation.user_id == user_id).all()
    print([ r.hotel.name for r in reservations_list])
    if not reservations_list:
        flask.flash("No reservations found", category="error")
        return flask.redirect('/')
    


    return flask.render_template("reservations.html",title ='Your Reservations',user_reservations = reservations_list)

@users.route("/reserve/<hotel_id>",methods=["GET", "POST"])
def reserve(hotel_id):
    form = forms.ReserveForm()
    print(current_user)
    if flask.request.method == "POST":
        if form.validate_on_submit():

            reservation = Reservation()
            reservation.start_date = form.start.data
            reservation.end_date = form.end.data
            reservation.hotel_id = hotel_id
            reservation.user_id = current_user.id
            

            db.session.add(reservation)
            db.session.commit()
         

            flask.flash("Your reservation has been successfully registered", category="success")

            return flask.redirect('/')
        else:
            print("Form errors:", form.errors)

    hotel = Hotel.query.filter_by(id=hotel_id).first()
    return flask.render_template("reserve.html", title='Reserve',hotel=hotel,form=form)