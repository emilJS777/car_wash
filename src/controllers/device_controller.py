from src.services import device_service
from flask import request
from src.middlewares import auth_middleware, role_middleware


# GET DEVICE IDS
@auth_middleware.check_authorize
@role_middleware.check_role(["admin", "engineer"])
def get_device_ids():
    res = device_service.get_device_ids()
    return res


# GET DEVICE BY ID
@auth_middleware.check_authorize
@role_middleware.check_role(["admin", "engineer"])
def get_device_by_id(device_id):
    res = device_service.get_device_by_id(device_id=device_id)
    return res


# CREATE DEVICE
@auth_middleware.check_authorize
@role_middleware.check_role(["engineer"])
def create_device():
    req = request.get_json()
    res = device_service.create_device(code=req['code'], car_wash_id=req['car_wash_id'])
    return res


# UPDATE DEVICE
@auth_middleware.check_authorize
@role_middleware.check_role(["engineer"])
def update_device(device_id):
    req = request.get_json()
    res = device_service.update_device(device_id=device_id, code=req['code'], car_wash_id=req['car_wash_id'])
    return res
