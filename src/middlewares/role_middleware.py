from functools import wraps
from src._response import response
from flask import request, g
from src.services_db import ticket_service_db, role_service_db


# CHECK PERMISSION
def check_role(allowed_roles):
    def decoration(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            role_id = ticket_service_db.get_ticket_by_user_id(user_id=g.user_id).role_id
            role_name = role_service_db.get_role_by_id(role_id=role_id).name

            # IF ALLOWED ROLES FIND ROLE NAME RETURN NEXT
            if role_name in allowed_roles:
                g.role_name = role_name
                return f(*args, **kwargs)

            # ELSE RETURN FORBIDDEN
            return response(False, {'msg': 'forbidden'}, 403)
        return decorated_function
    return decoration
