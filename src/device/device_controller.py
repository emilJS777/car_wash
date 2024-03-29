from . import device_service, device_validator
from flask import request
from src.role import role_middleware
from src.ticket import ticket_middleware
from src.auth import auth_middleware
from flask import g
from flask_expects_json import expects_json


# GET DEVICE IDS
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(["admin", "engineer", "owner"])
def get_device_ids():
    res = device_service.get_device_ids_by_owner_id(owner_id=g.user_id) \
        if g.role_name == "owner" \
        else device_service.get_device_ids()
    return res


# GET DEVICE IDS BY OWNER ID
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(["admin", "engineer"])
def get_device_ids_by_owner_id(owner_id: int):
    res = device_service.get_device_ids_by_owner_id(owner_id=owner_id)
    return res


# GET DEVICE IDS BY CAR WASH ID
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(["admin", "engineer", "owner"])
def get_device_ids_by_car_wash_id(car_wash_id: int):
    res = device_service.get_device_ids_by_car_wash_id(car_wash_id=car_wash_id)
    return res


# GET DEVICE BY ID
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(["admin", "engineer", "owner"])
def get_device_by_id(device_id: int):
    res = device_service.get_device_by_id(device_id=device_id)
    return res


# CREATE DEVICE
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(["admin", "engineer"])
@expects_json(device_validator.device_schema)
def create_device():
    req = request.get_json()
    res = device_service.create_device(code=req['code'], owner_id=req['owner_id'], car_wash_id=req['car_wash_id'])
    return res


# UPDATE DEVICE
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(["admin", "engineer"])
def update_device(device_id: int):
    req = request.get_json()
    res = device_service.update_device(device_id=device_id, code=req['code'], car_wash_id=req['car_wash_id'])
    return res


# DELETE DEVICE
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(["admin", "engineer"])
def delete_device(device_id: int):
    res = device_service.delete_device(device_id)
    return res


# ****** DEVICE ACTIVE
def update_device_active():
    req = request.get_json()
    res = device_service.update_device_active(
        device_id=req['id'],
        device_active=req['active']
    )
    return res


# ***** DEVICE CONTENT

# UPDATE DEVICE CONTENT FROM DEVICE
def update_device_content():
    device_code: str = request.args['device_code']
    water: bool = request.args['water'] == 'true'
    lather: bool = request.args['lather'] == 'true'
    res = device_service.update_device_content(device_code=device_code, water=water, lather=lather)
    return res
