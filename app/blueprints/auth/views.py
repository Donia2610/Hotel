#https://jamboard.google.com/d/1QkuB6jm7vekd6GwiLoENPpBq_kBgEfMF52uM8pK9Z4g/edit?usp=meet_whiteboard views.py
import flask, flask_login

from . import db, forms, blueprint

from .models import User



@blueprint.route("/sign-up", methods=["GET", "POST"])
def signup():
    form = forms.SignupForm()

    if flask.request.method == "POST":
        if form.validate_on_submit():

            user = User()
            user.name = form.username.data
            user.password = form.password.data

            #db.session.add(user)
            #db.session.commit()
            user.save()

            flask.flash("User has been successfully registered", category="success")

            return flask.redirect('/')
        else:
            print("Form errors:", form.errors)

    return flask.render_template("signup.html", form=form)


@blueprint.route("/sign-in", methods=["GET", "POST"])
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

@blueprint.route("/sign-out")
def signout():
    flask_login.logout_user()
    flask.flash("Goodbye !", category="message")
    return flask.redirect('/')


