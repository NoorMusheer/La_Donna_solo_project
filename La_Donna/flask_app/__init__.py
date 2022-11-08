from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = "this is the secret key for the La Donna app"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'noormusheer@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get('Gmail_Pword')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail =Mail(app)


