from . import user_service, user_validator
from flask import request
from flask_expects_json import expects_json
from src.role import role_middleware
from src.ticket import ticket_middleware
from src.auth import auth_middleware


# GET USER BY ID
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
def get_user_by_id(user_id: int):
    res = user_service.get_user_by_id(user_id=user_id)
    return res


# CREATE USER
@expects_json(user_validator.create_user_schema)
def create_user():
    req = request.get_json()
    res = user_service.create_user(name=req['name'], first_name=req['first_name'].title(),
                                   last_name=req['last_name'].title(), password=req['password'],
                                   ticket_code=req['ticket_code'])
    return res


# UPDATE USER
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
def update_user(user_id: int):
    req = request.get_json()
    res = user_service.update_user(user_id=user_id, name=req['name'],
                                   first_name=req['first_name'], last_name=req['last_name'])
    return res


# DELETE USER
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(["admin"])
def delete_user(user_id: int):
    res = user_service.delete_user(user_id=user_id)
    return res
