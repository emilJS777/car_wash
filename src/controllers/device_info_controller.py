from src.services import device_info_service
from flask import request
from src.middlewares import auth_middleware, role_middleware


# GET DEVICE INFO IDS
@auth_middleware.check_authorize
@role_middleware.check_role(['engineer'])
def get_device_info_ids():
    res = device_info_service.get_device_info_ids()
    return res


# GET DEVICE BY ID
@auth_middleware.check_authorize
@role_middleware.check_role(['engineer'])
def get_device_info_by_id(device_info_id):
    res = device_info_service.get_device_info_by_id(device_info_id=device_info_id)
    return res


# CREATE DEVICE INFO
def create_device_info():
    req = request.get_json()
    res = device_info_service.create_device_info(device_id=req['device_id'], payment=req['payment'], topic=req['topic'])
    return res
