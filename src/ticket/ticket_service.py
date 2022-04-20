from . import ticket_service_db
from src.role import role_service_db
from .ticket_service_db import Ticket
from src._response import response
from typing import List


# GET TICKETS BY ROLE
def get_tickets_by_role_name(role_name: str):
    # GET ALL TICKETS BY ENGINEER ROLE ID AND RETURN OK
    role_id: int = role_service_db.get_role_by_name(name=role_name).id
    ticket_arr: List[dict] = ticket_service_db.get_tickets_by_role_id(role_id=role_id)
    return response(True, ticket_arr, 200)


# CREATE TICKET
def create_ticket():
    # IF G USER ROLE NAME IS ADMIN _ GET ROLE ID FOR ENGINEER
    role_id: int = role_service_db.get_role_by_name(name="owner").id

    # CREATE TICKET FOR THIS ROLE AND RETURN RESPONSE OK
    ticket: Ticket = ticket_service_db.create_ticket(role_id=role_id, code=ticket_service_db.generate_ticket_code())
    return response(True, {'id': ticket.id, 'code': ticket.code}, 201)


# DELETE TICKET BY ID
def delete_ticket(ticket_id: int):
    # GET TICKET BY ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    if not ticket_service_db.get_ticket_by_id(ticket_id=ticket_id):
        return response(False, {'msg': 'ticket not found'}, 404)

    # ELSE DELETE TICKET AND RETURN OK
    ticket: Ticket = ticket_service_db.delete_ticket(ticket_id=ticket_id)
    return response(True, {'msg': f'ticket by id {ticket.id} successfully deleted!'}, 200)


# ACTIVATE OR DEACTIVATE TICKET BY ID
def activate_or_deactivate_ticket(ticket_id: int):
    # GET TICKET BY ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    if not ticket_service_db.get_ticket_by_id(ticket_id=ticket_id):
        return response(False, {'msg': 'ticket not found'}, 404)

    # ELSE ACTIVATE IF NOT ACTIVE ELSE DEACTIVATE IF ACTIVE
    ticket: Ticket = ticket_service_db.activate_or_deactivate_ticket(ticket_id=ticket_id)
    return response(True, {'id': ticket.id, 'active': ticket.active}, 200)
