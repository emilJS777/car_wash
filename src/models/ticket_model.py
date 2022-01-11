from src import db
import random
import string
from datetime import datetime


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(40), nullable=False)
    user_id = db.Column(db.Integer, nullable=True)
    role_id = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, default=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())

    # CONSTRUCTOR
    def __init__(self, code):
        self.code = code

    # SAVE DB SELF
    def save_db(self):
        db.session.add(self)
        db.session.commit()

    # DELETE DB
    def delete_db(self):
        db.session.delete(self)
        db.session.commit()

    # UPDATE DATABASE
    @staticmethod
    def update_db():
        db.session.commit()

    # GENERATE RANDOM TICKET CODE
    @staticmethod
    def generate_ticket_code(length=32, uppercase=True, lowercase=True, numbers=True):
        ticket_code = ''

        if uppercase:
            ticket_code += string.ascii_uppercase
        if lowercase:
            ticket_code += string.ascii_lowercase
        if numbers:
            ticket_code += string.digits

        return ''.join(random.choice(ticket_code) for i in range(length))
