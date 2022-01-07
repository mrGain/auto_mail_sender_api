from flask import Flask
from flask_mail import Message,Mail

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'name_of_db'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/name_of_db'

#=========================================
# configuring the mail

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "abcd@gmail.com" # Enter senders mail here.
app.config['MAIL_PASSWORD'] = "password"       # Enter your senders password here
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# Here we specify the subject, sender and recipient of the mail.

get_mail={
    "subject" :"Your subject",
    "sender":"abcd@gmail.com",  #Senders mail here 
    "recipient":"abcd@gmail.com" #REcepients mail here.
}