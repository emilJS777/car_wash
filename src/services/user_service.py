from src.services_db import user_service_db, ticket_service_db, auth_service_db, email_service_db
from src._response import response


# CREATE USER AND UPDATE TICKET ASSIGN FIELDS (TICKET ACTIVE)
def create_user(name, password, email, ticket_code):
    ticket = ticket_service_db.get_ticket_by_code(code=ticket_code)
    user = user_service_db.get_user_by_name(name=name)

    if not ticket:
        return response(False, {'msg': 'ticket code not found'}, 404)

    elif user:
        return response(False, {'msg': 'user by this name exist'}, 409)

    else:
        user = user_service_db.create_user(name=name, password=password)
        email_service_db.create_email(address=email, user_id=user.id)
        ticket_service_db.activate_ticket(ticket_id=ticket.id, user_id=user.id)
        return response(True, {'msg': f'user by id {user.id} successfully created'}, 201)
