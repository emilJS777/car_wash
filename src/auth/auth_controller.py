from flask import request
from flask_jwt_extended import jwt_required
from . import auth_service, auth_validator, auth_middleware
from flask_expects_json import expects_json
from src.ticket import ticket_middleware


@expects_json(auth_validator.login_schema)
def login():
    req = request.get_json()
    res = auth_service.login(name=req['name'], password=req['password'])
    return res


@jwt_required(refresh=True)
def refresh():
    res = auth_service.refresh()
    return res


@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
def get_profile():
    res = auth_service.get_profile()
    return res
