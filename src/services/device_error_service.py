from src.services_db import device_error_service_db
from src._response import response


# GET DEVICE ERROR IDS
def get_device_error_ids():
    device_error_ids = device_error_service_db.get_device_error_ids()
    return response(True, device_error_ids, 200)


# GET DEVICE ERROR BY ID
def get_device_error_by_id(device_error_id):
    # GET DEVICE ERROR BY ID IND VERIFY. IF NOT FOUND RETURN NOT FOUND
    device_error = device_error_service_db.get_device_error_by_id(device_error_id=device_error_id)
    if not device_error:
        return response(False, {'msg': f'device error by id {device_error_id} not found'}, 404)

    # ELSE RETURN DEVICE ERROR AND OK
    return response(True, {'id': device_error.id, 'device_code': device_error.device_code,
                           'msg': device_error.msg, 'creation_date': device_error.creation_date}, 200)


