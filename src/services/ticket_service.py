from src.services_db import ticket_service_db, role_service_db
from src._response import response


# CREATE TICKET
def create_ticket(role_id):
    # GET ROLE ID AND VERIFY EXIST. IF NO RETURN NOT FOUND
    role = role_service_db.get_role_by_id(role_id=role_id)
    if not role:
        return response(False, {'msg': 'role not found'}, 404)

    # ELSE CREATE TICKET CODE BY THIS ROLE ID AND RETURN CREATE CODE
    ticket = ticket_service_db.create_ticket(role_id=role_id)
    return response(True, {'code': ticket.code}, 201)
