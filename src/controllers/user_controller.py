from src.services import user_service
from flask import request


# GET USER BY ID
def get_user_by_id(user_id):
    res = user_service.get_user_by_id(user_id=user_id)
    return res


# CREATE USER
def create_user():
    req = request.get_json()
    res = user_service.create_user(name=req['name'], first_name=req['first_name'],
                                   last_name=req['last_name'], password=req['password'],
                                   ticket_code=req['ticket_code'])
    return res


# UPDATE USER
def update_user(user_id):
    req = request.get_json()
    res = user_service.update_user(user_id=user_id, name=req['name'],
                                   first_name=req['first_name'], last_name=req['last_name'])
    return res


# DELETE USER
def delete_user(user_id):
    res = user_service.delete_user(user_id=user_id)
    return res
