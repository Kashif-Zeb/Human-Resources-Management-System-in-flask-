from flask_mail import Message
from .email_initalize import mail

def send_login_email(user_email=None, username=None):
    msg = Message("Login Notification",
                  recipients=['kashifzk216@gmail.com'])
    msg.body = f"Hello {username},\n\nYou have logged in successfully to your account."
    mail.send(msg)