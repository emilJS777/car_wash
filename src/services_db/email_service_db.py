from src.models.email_model import Email
from flask_mail import Message
from src import mail, app


# GET EMAIL BY ID
def get_email_by_id(email_id):
    email = Email.query.filter_by(id=email_id).first()
    return email


# GET EMAIL BY TICKET ID
def get_email_by_ticket_id(ticket_id):
    email = Email.query.filter_by(ticket_id=ticket_id).first()
    return email


# CREATE EMAIL
def create_email(ticket_id, address):
    email = Email(ticket_id=ticket_id, address=address)
    email.save_db()
    return email


# GET EMAIL BY ADDRESS
def get_email_by_address(address):
    email = Email.query.filter_by(address=address).first()
    return email


# SEND TICKET CODE
def send_ticket_code_by_email_id(email_id, ticket_code):
    email = Email.query.filter_by(id=email_id).first()
    msg = Message('Hello', sender=app.config['MAIL_USERNAME'], recipients=[email.address])
    msg.html = f"Your ticket code <b>{ticket_code}</b>"
    mail.send(msg)
    return email
