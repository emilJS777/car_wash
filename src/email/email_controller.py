from . import email_service, email_validator
from flask import request
from flask_expects_json import expects_json
from src.role import role_middleware
from src.ticket import ticket_middleware
from src.auth import auth_middleware


# GET EMAIL BY TICKET ID
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(['admin', 'engineer'])
def get_email_by_ticket_id(ticket_id: int):
    res = email_service.get_email_by_ticket_id(ticket_id=ticket_id)
    return res


# CREATE EMAIL
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(['admin', 'engineer'])
@expects_json(email_validator.email_schema)
def create_email():
    req = request.get_json()
    res = email_service.create_email(ticket_id=req['ticket_id'], address=req['address'])
    return res


# SEND TICKET CODE BY EMAIL ID
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(['admin', 'engineer'])
def send_ticket_code_by_email_id(email_id: int):
    res = email_service.send_ticket_code_by_email_id(email_id=email_id)
    return res
