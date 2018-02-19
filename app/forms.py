from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from flask import Flask, render_template, flash, session, redirect, url_for

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

class myForm(FlaskForm):
    name = StringField('Please enter your full name', validators=[DataRequired()])
    email = StringField('Please enter e-mail address', validators=[DataRequired(),  Email()])
    subject = StringField('Please enter the subject for your message', validators=[DataRequired()])
    message = TextAreaField('Please enter the message you would like to send', validators=[DataRequired()])
    button = StringField('Send')
    
    
  