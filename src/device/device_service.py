from . import device_service_db
from .device_service_db import Device
from src._response import response
from typing import List


# GET Device IDS
def get_device_ids():
    device_ids: List[int] = device_service_db.get_device_ids()
    return response(True, device_ids, 200)


# GET DEVICE IDS BY OWNER ID
def get_device_ids_by_owner_id(owner_id: int):
    device_ids: List[int] = device_service_db.get_device_ids_by_owner(owner_id=owner_id)
    return response(True, device_ids, 200)


# GET DEVICE IDS BY CAR WASH ID
def get_device_ids_by_car_wash_id(car_wash_id: int):
    device_ids: List[int] = device_service_db.get_device_ids_by_car_wash(car_wash_id=car_wash_id)
    return response(True, device_ids, 200)


# CREATE DEVICE
def create_device(code: str, owner_id: int, car_wash_id: int):
    # GET DEVICE BY CODE AND VERIFY. IF EXIST RETURN CONFLICT
    if device_service_db.get_device_by_code(code=code):
        return response(False, {'msg': 'device by this code exist'}, 409)

    # ELSE CREATE DEVICE AND RETURN OK
    device_service_db.create_device(code=code, owner_id=owner_id, car_wash_id=car_wash_id)
    return response(True, {'msg': 'device successfully created!'}, 201)


# GET DEVICE BY ID
def get_device_by_id(device_id: int):
    # GET DEVICE BY ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    device: Device = device_service_db.get_device_by_id(device_id=device_id)
    if not device:
        return response(False, {'msg': 'device not found'}, 404)

    # ELSE RETURN DEVICE FIELDS
    return response(True, {'id': device.id, 'code': device.code, 'active': device.active,
                           'owner_id': device.owner_id, 'last_update': device.last_update,
                           'water': device.water, "lather": device.lather}, 200)


# UPDATE DEVICE
def update_device(device_id: int, code: str, car_wash_id: int):
    # GET DEVICE BY ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    if not device_service_db.get_device_by_id(device_id=device_id):
        return response(False, {'msg': 'device not found'}, 404)

    # GET DEVICE BY CODE AND VERIFY. IF EXIST RETURN CONFLICT
    if device_service_db.get_device_by_code(code=code):
        return response(False, {'msg': 'device by this code exist'}, 409)

    # ELSE UPDATE DEVICE AND RETURN OK
    device_service_db.update_device(device_id=device_id, code=code, car_wash_id=car_wash_id)
    return response(True, {'msg': 'device successfully updated!'}, 200)


# DELETE DEVICE
def delete_device(device_id: int):
    # GET DEVICE BY ID AND VERIFY IF NOT FOUND RETURN NOT FOUND
    if not device_service_db.get_device_by_id(device_id):
        return response(False, {'msg': 'device not found'}, 404)

    # ELSE REMOVE DEVICE AND RETURN OK
    device_service_db.delete_device(device_id)
    return response(True, {'msg': 'device successfully deleted'}, 200)


# ***** DEVICE CONTEnT

# UPDATE DEVICE CONTENT
def update_device_content(device_code: str, water: bool, lather: bool):
    device = device_service_db.get_device_by_code(code=device_code)
    if not device:
        return response(False, {'msg': 'device not found'}, 404)

    device_content_updated = device_service_db.update_device_content(device_id=device.id, water=water, lather=lather)
    # RESPONSE OK AND DEVICE CONTENT FIELDS
    return response(True, {'device_id': device_content_updated.id,
                           'water': device_content_updated.water,
                           'lather': device_content_updated.lather}, 200)
