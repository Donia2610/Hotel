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


class QueryForm(flask_wtf.FlaskForm):

    query    = wtforms.StringField("")
    submit   = wtforms.SubmitField("Search")





