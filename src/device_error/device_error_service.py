from . import device_error_service_db
from .device_error_service_db import DeviceError
from src.device import device_service_db
from src._response import response
from typing import List


# GET DEVICE ERROR IDS
def get_device_error_ids():
    device_error_ids: List[int] = device_error_service_db.get_device_error_ids()
    return response(True, device_error_ids, 200)


# GET DEVICE ERROR BY ID
def get_device_error_by_id(device_error_id: int):
    # GET DEVICE ERROR BY ID IND VERIFY. IF NOT FOUND RETURN NOT FOUND
    device_error: DeviceError = device_error_service_db.get_device_error_by_id(device_error_id=device_error_id)
    if not device_error:
        return response(False, {'msg': f'device error by id {device_error_id} not found'}, 404)

    # ELSE RETURN DEVICE ERROR AND OK
    return response(True, {'id': device_error.id, 'device_code': device_error.device_code,
                           'msg': device_error.msg, 'creation_date': device_error.creation_date}, 200)


# CREATE DEVICE ERROR
def create_device_error(device_code: str, msg: str):
    # GET DEVICE BY CODE AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not device_service_db.get_device_by_code(code=device_code):
        return response(False, {'msg': f'device not found by code {device_code}'}, 404)

    # ELSE CREATE DEVICE ERROR AND RETURN OK
    device_error_service_db.create_device_error(device_code=device_code, msg=msg)
    return response(True, {'msg': "device error successfully created"}, 200)
