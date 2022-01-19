from src.models.ticket_model import Ticket
import random
import string


# GET TICKET BY ID
def get_ticket_by_id(ticket_id):
    ticket = Ticket.query.filter_by(id=ticket_id).first()
    return ticket


# GET TICKET BY USER ID
def get_ticket_by_user_id(user_id):
    ticket = Ticket.query.filter_by(user_id=user_id).first()
    return ticket


# GET TICKET BY CODE
def get_ticket_by_code(code):
    ticket = Ticket.query.filter_by(code=code).first()
    return ticket


# CREATE TICKET
def create_ticket(role_id, code=None):
    ticket = Ticket(role_id=role_id)
    ticket.code = code
    ticket.save_db()
    return ticket


# UPDATE TICKET ASSIGN FIELD USER ID
def update_ticket(ticket_id, user_id):
    ticket = Ticket.query.filter_by(id=ticket_id).first()
    ticket.user_id = user_id
    ticket.code = None
    ticket.update_db()
    return ticket


# DELETE TICKET BY ID
def delete_ticket(ticket_id):
    ticket = Ticket.query.filter_by(id=ticket_id).first()
    ticket.delete_db()
    return ticket


# GENERATE TICKET CODE
def generate_ticket_code(length=32, uppercase=True, lowercase=True, numbers=True):
    ticket_code = ''

    if uppercase:
        ticket_code += string.ascii_uppercase
    if lowercase:
        ticket_code += string.ascii_lowercase
    if numbers:
        ticket_code += string.digits

    return ''.join(random.choice(ticket_code) for i in range(length))
