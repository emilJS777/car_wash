from src.services import device_service
from flask import request
from src.middlewares import auth_middleware, role_middleware, ticket_middleware
from flask import g


# GET DEVICE IDS
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(["admin", "engineer", "owner"])
def get_device_ids():
    res = device_service.get_device_ids_by_owner_id(owner_id=g.user_id) \
        if g.role_name == "owner" \
        else device_service.get_device_ids()
    return res


# GET DEVICE IDS BY CAR WASH ID
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(["admin", "engineer", "owner"])
def get_device_ids_by_car_wash_id(car_wash_id):
    print(g.role_name)
    res = device_service.get_device_ids_by_car_wash_id_owner_id(car_wash_id=car_wash_id, owner_id=g.user_id) \
        if g.role_name == 'owner' \
        else device_service.get_device_ids_by_car_wash_id(car_wash_id=car_wash_id)
    return res


# GET DEVICE BY ID
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(["admin", "engineer", "owner"])
def get_device_by_id(device_id):
    res = device_service.get_device_by_id(device_id=device_id)
    return res


# CREATE DEVICE
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(["admin", "engineer"])
def create_device():
    req = request.get_json()
    res = device_service.create_device(code=req['code'], car_wash_id=req['car_wash_id'])
    return res


# UPDATE DEVICE
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(["admin", "engineer"])
def update_device(device_id):
    req = request.get_json()
    res = device_service.update_device(device_id=device_id, code=req['code'], car_wash_id=req['car_wash_id'])
    return res
