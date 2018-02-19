<<<<<<< HEAD
from flask import Flask
from flask_mail import Mail
app = Flask(__name__)

app.config['SECRET_KEY'] = 'Hello World'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
=======
from Flask import Flask
from Flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = 'enter some random passphrase'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = 'enter your mailtrap username'
app.config['MAIL_PASSWORD'] = 'enter your mailtrap password'
>>>>>>> 2d5544afecf55e3ba64dfccf3619355def35881a
mail = Mail(app)

from app import views
