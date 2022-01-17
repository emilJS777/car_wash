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
    return response(True, {'code': ticket.code}, 201)
