from functools import wraps
from src.services_db import ticket_service_db, role_service_db
from src._response import response
from flask import g


# CHECK ROLE WITH TICKET
def check_roles(allowed_roles):
    def decoration(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            ticket = ticket_service_db.get_ticket_by_user_id(user_id=g.user_id)
            print(ticket)

            role = role_service_db.get_role_by_id(role_id=ticket.role_id)
            for role_title in allowed_roles:
                if role.title == role_title:
                    return f(*args, **kwargs)

                return response(False, {'msg': 'you have no rights'}, 403)
        return decorated_function
    return decoration
