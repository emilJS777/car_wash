from .ticket_model import Ticket
import random
import string
from typing import List
from src.user import user_service_db


# GET TICKET IDS BY ROLE ID
def get_tickets_by_role_id(role_id: int) -> List[dict]:
    tickets_arr: List[dict] = []
    tickets: List[Ticket] = Ticket.query.order_by(Ticket.expiration_date).filter_by(role_id=role_id).all()
    for ticket in tickets:
        user_name = None

        if ticket.user_id:
            user_name = user_service_db.get_user_by_id(ticket.user_id).name

        tickets_arr.append({'id': ticket.id, 'role_id': ticket.role_id, 'expiration_date': ticket.expiration_date,
                            'code': ticket.code, 'active': ticket.active, 'user_id': ticket.user_id, 'user_name': user_name})
    return tickets_arr


# GET TICKET BY ID
def get_ticket_by_id(ticket_id: int) -> Ticket:
    ticket: Ticket = Ticket.query.filter_by(id=ticket_id).first()
    return ticket


# GET TICKET BY USER ID
def get_ticket_by_user_id(user_id: int) -> Ticket:
    ticket: Ticket = Ticket.query.filter_by(user_id=user_id).first()
    return ticket


# GET TICKET BY CODE
def get_ticket_by_code(code: str) -> Ticket:
    ticket: Ticket = Ticket.query.filter_by(code=code).first()
    return ticket


# CREATE TICKET
def create_ticket(role_id: int, code=None) -> Ticket:
    ticket: Ticket = Ticket(role_id=role_id)
    ticket.code = code
    ticket.save_db()
    return ticket


# UPDATE TICKET ASSIGN FIELD USER ID
def update_ticket(ticket_id, user_id) -> Ticket:
    ticket = Ticket.query.filter_by(id=ticket_id).first()
    ticket.user_id = user_id
    ticket.code = None
    ticket.update_db()
    return ticket


# DELETE TICKET BY ID
def delete_ticket(ticket_id) -> Ticket:
    ticket = Ticket.query.filter_by(id=ticket_id).first()
    ticket.delete_db()
    return ticket


# ACTIVATE OR DEACTIVATE TICKET BY ID
def activate_or_deactivate_ticket(ticket_id) -> Ticket:
    ticket = Ticket.query.filter_by(id=ticket_id).first()
    ticket.active = False if ticket.active else True
    ticket.update_db()
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
