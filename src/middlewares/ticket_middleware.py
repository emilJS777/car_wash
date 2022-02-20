from functools import wraps
from src._response import response
from src.services_db import ticket_service_db
from src.services_db.ticket_service_db import Ticket
from flask import g


# CHECk TICKET ACTIVE
def check_active_ticket(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # GET TICKET BY G USER ID AND VERIFY IS ACTIVE. IF ACTIVE ASSIGN G TICKET ID AND RETURN NEXT
        ticket: Ticket = ticket_service_db.get_ticket_by_user_id(user_id=g.user_id)
        if ticket.active:
            g.ticket_id = ticket.id
            return f(*args, **kwargs)
        # ELSE RETURN TICKET NOT ACTIVE FORBIDDEN
        return response(False, {'msg': 'ticket not active'}, 403)
    return decorated_function
