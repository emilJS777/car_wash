from src.services_db import device_info_service_db, device_service_db
from src._response import response


# GET DEVICE INFO IDS
def get_device_info_ids():
    device_info_ids = device_info_service_db.get_device_info_ids()
    return response(True, device_info_ids, 200)


# GET DEVICE INFO BY ID
def get_device_info_by_id(device_info_id):
    # GET DEVICE INFO BY ID AND VERIFY. OF NOT FOUND RETURN NOT FOUND
    device_info = device_info_service_db.get_device_info_by_id(device_info_id=device_info_id)
    if not device_info:
        return response(False, {'msg': 'device info not found'}, 404)

    # ELSE RETURN DEVICE INFO FIELDS AND OK
    return response(True, {'id': device_info.id, 'device_id': device_info.device_id,
                           'payment': device_info.payment, 'topic': device_info.topic}, 200)


# CREATE DEVICE INFO
def create_device_info(device_id, payment, topic):
    # GET DEVICE BY ID AND VERIFY. OF NOT FOUND RETURN NOT FOUND
    if not device_service_db.get_device_by_id(device_id=device_id):
        return response(False, {'msg': 'device not found'}, 404)

    # ELSE CREATE NEW DEVICE INFO AND RETURN OK
    device_info = device_info_service_db.create_device_info(device_id=device_id, payment=payment, topic=topic)
    return response(True, {'msg': f'device info by id {device_info.payment} successfully created!'}, 201)
