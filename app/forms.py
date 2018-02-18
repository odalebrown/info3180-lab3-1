from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class myForm(FlaskForm):
    name = StringField('Please enter your full name', validators=[DataRequired()])
    email = StringField('Please enter e-mail address', validators=[DataRequired()])
    subject = StringField('Please enter the subject for your message', validators=[DataRequired()])
    msg = StringField('Please enter the message you would like to send', validators=[DataRequired()])
    
    
  