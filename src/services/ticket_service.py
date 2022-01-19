from src.services_db import ticket_service_db, role_service_db
from src._response import response
from flask import g


# CREATE TICKET
def create_ticket():
    # IF G USER ROLE NAME IS ADMIN _ GET ROLE ID FOR ENGINEER
    if g.role_name == 'admin':
        role_id = role_service_db.get_role_by_name(name="engineer").id

    # ELSE IF G USER ROLE NAME IS ENGINEER _ GET ROLE ID FOR OWNER
    else:
        role_id = role_service_db.get_role_by_name(name="owner").id

    # CREATE TICKET FOR THIS ROLE AND RETURN RESPONSE OK
    ticket = ticket_service_db.create_ticket(role_id=role_id, code=ticket_service_db.generate_ticket_code())
    return response(True, {'id': ticket.id, 'code': ticket.code}, 201)


# DELETE TICKET BY ID
def delete_ticket(ticket_id):
    # GET TICKET BY ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    if not ticket_service_db.get_ticket_by_id(ticket_id=ticket_id):
        return response(False, {'msg': 'ticket not found'}, 404)

    # ELSE DELETE TICKET AND RETURN OK
    ticket = ticket_service_db.delete_ticket(ticket_id=ticket_id)
    return response(True, {'msg': f'ticket by id {ticket.id} successfully deleted!'}, 200)