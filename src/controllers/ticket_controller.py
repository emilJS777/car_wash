from src.services import ticket_service
from flask import request
from src.middlewares import auth_middleware, role_middleware


# TICKET CREATE
@auth_middleware.check_authorize
@role_middleware.check_roles(["engineer"])
def create_ticket():
    req = request.get_json()
    res = ticket_service.create_ticket(role_id=req['role_id'])
    return res
