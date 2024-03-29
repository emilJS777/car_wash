from . import device_error_service
from src.role import role_middleware
from src.auth import auth_middleware
from flask import request


# GET DEVICE ERROR IDS
@auth_middleware.check_authorize
@role_middleware.check_role(["admin"])
def get_device_error_ids():
    res = device_error_service.get_device_error_ids()
    return res


# GET DEVICE ERROR BY ID
@auth_middleware.check_authorize
@role_middleware.check_role(["admin"])
def get_device_error_by_id(device_error_id: int):
    res = device_error_service.get_device_error_by_id(device_error_id=device_error_id)
    return res


# CREATE DEVICE ERROR
def create_device_error():
    res = device_error_service.create_device_error(device_code=request.args['device_code'], msg=request.args['msg'])
    return res
