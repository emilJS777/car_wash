from . import role_service
from flask import request


# GET ROLE IDS
def get_role_ids():
    res = role_service.get_role_ids()
    return res


# GET ROLE BY ID
def get_role_by_id(role_id: int):
    res = role_service.get_role_by_id(role_id=role_id)
    return res


# CREATE ROLE
def create_role():
    req = request.get_json()
    res = role_service.create_role(name=req['name'])
    return res


# UPDATE ROLE
def update_role(role_id: int):
    req = request.get_json()
    res = role_service.update_role(role_id=role_id, name=req['name'])
    return res


# DELETE ROLE
def delete_role(role_id: int):
    res = role_service.delete_role(role_id=role_id)
    return res
