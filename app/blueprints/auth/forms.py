#!/usr/bin/python3

##############################################
#
# app folder
# forms.py
#
##############################################

import flask_wtf
import wtforms
from wtforms import validators as vld

class SignupForm(flask_wtf.FlaskForm):

    username = wtforms.StringField("Name:", validators=[vld.DataRequired()])
    password = wtforms.PasswordField("Password:", validators=[vld.DataRequired()])

    submit   = wtforms.SubmitField("Sign up")

class SigninForm(flask_wtf.FlaskForm):

    username = wtforms.StringField("Name:", validators=[vld.DataRequired()])
    password = wtforms.PasswordField("Password:", validators=[vld.DataRequired()])

    submit   = wtforms.SubmitField("Sign in")


