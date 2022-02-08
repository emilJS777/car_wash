from functools import wraps
from src._response import response
from flask import g
from src.services_db import ticket_service_db
from datetime import datetime


# CHECK EXPIRATION DATE BY ROLE NAME
def check_expiration(role_names):
    def decoration(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # GET ARRAY OF ROLE FROM ARGUMENT AND FIND A MATCH WITH REQUESTER ROLE,
            if g.role_name in role_names:
                ticket = ticket_service_db.get_ticket_by_user_id(user_id=g.user_id)

                # IF MATCH GET USER TICKET AND CHECK DATE, IF DATE EXPIRED RETURN IS NOT ALLOWED
                if ticket.expiration_date < datetime.utcnow():
                    return response(False, {'msg': 'account expiration expired'}, 403)

            return f(*args, **kwargs)
        return decorated_function
    return decoration
