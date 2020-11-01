#https://jamboard.google.com/d/1QkuB6jm7vekd6GwiLoENPpBq_kBgEfMF52uM8pK9Z4g/edit?usp=meet_whiteboard views.py
import flask, flask_login

from . import blueprint, db# The directory where the file is currently (here is blueprint/)
from . import forms

from . import User

@blueprint.route("/", methods=["GET", "POST"])
@blueprint.route("/home", methods=["GET", "POST"])
def index():
    query_form = forms.QueryForm()
    if query_form.validate_on_submit():
        url = flask.url_for('main.search_users', username=query_form.query.data)
        return flask.redirect(url)
    else:
        print(query_form.errors)

    return flask.render_template("index.html", title="My awesome blueprint", title2="Awesome blueprint", query_form=query_form)

@blueprint.route("/search-by/user/<username>")
def search_users(username):
    matching_users = list(User.query.filter_by(name=username))
    return flask.render_template("users_list.html", users=matching_users)

@blueprint.route("/profile/<user_name>")
def profile_page(user_name):
    user = User.query.filter_by(name=user_name).first_or_404()
    return flask.render_template("profile_page.html", user=user)

@blueprint.route("/users_list")
def users_list():
    users = User.query.all()
    return flask.render_template("users_list.html", users=users)

@blueprint.route("/secret-page")
@flask_login.login_required
def secret():
    return "You reached the secret page !"

