#!/usr/bin/python3

##############################################
#
# app folder
# forms.py
#
##############################################
import flask_wtf
import wtforms
from flask_wtf import Form
from wtforms import validators as vld
from wtforms.fields.html5 import DateField

class SignupForm(flask_wtf.FlaskForm):

    username = wtforms.StringField("Name:", validators=[vld.DataRequired()])
    password = wtforms.PasswordField("Password:", validators=[vld.DataRequired()])

    submit   = wtforms.SubmitField("Sign up")

class SigninForm(flask_wtf.FlaskForm):

    username = wtforms.StringField("Name:", validators=[vld.DataRequired()])
    password = wtforms.PasswordField("Password:", validators=[vld.DataRequired()])

    submit   = wtforms.SubmitField("Sign in")

class ReserveForm(Form):
    start = DateField("Start Date: ", format = '%Y-%m-%d', validators=[vld.DataRequired()])
    end = DateField("End Date:  ", format = '%Y-%m-%d',validators=[vld.DataRequired()])

    submit = wtforms.SubmitField("Reserve")


