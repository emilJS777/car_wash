from src.services_db import device_service_db, car_wash_service_db
from src._response import response


# GET Device IDS
def get_device_ids():
    device_ids = device_service_db.get_device_ids()
    return response(True, device_ids, 200)


# GET DEVICE IDS BY CAR WASH IDS
def get_device_ids_by_car_wash_id(car_wash_id):
    device_ids = device_service_db.get_device_ids_by_car_wash_id(car_wash_id=car_wash_id)
    return response(True, device_ids, 200)


# GET DEVICE IDS BY CAR WASH ID OWNER ID
def get_device_ids_by_car_wash_id_owner_id(car_wash_id, owner_id):
    # GET CAR WASH BY ID BY OWNER ID AND VERIFY. IF NOT FOUND ReTURN NOT FOUND
    if not car_wash_service_db.get_car_wash_by_id_by_owner_id(car_wash_id=car_wash_id, owner_id=owner_id):
        return response(False, {'msg': f'car wash by id {car_wash_id} not found'}, 404)

    # ELSE RETURN GET AND RETURN DEVICE IDS BY CAR WASH ID
    device_ids = device_service_db.get_device_ids_by_car_wash_id(car_wash_id=car_wash_id)
    return response(True, device_ids, 200)


# CREATE DEVICE
def create_device(code, car_wash_id):
    # GET DEVICE BY CODE AND VERIFY. IF EXIST RETURN CONFLICT
    if device_service_db.get_device_by_code(code=code):
        return response(False, {'msg': 'device by this code exist'}, 409)

    # GET CAR WASH BY TITLE AND VERIFY. IF EXIST RETURN CONFLICT
    if car_wash_id and not car_wash_service_db.get_car_wash_by_id(car_wash_id=car_wash_id):
        return response(False, {'msg': 'car wash not found'}, 404)

    # ELSE CREATE DEVICE AND RETURN OK
    device_service_db.create_device(code=code, car_wash_id=car_wash_id)
    return response(True, {'msg': 'device successfully created!'}, 201)


# GET DEVICE BY ID
def get_device_by_id(device_id):
    # GET DEVICE BY ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    device = device_service_db.get_device_by_id(device_id=device_id)
    if not device:
        return response(False, {'msg': 'device not found'}, 404)

    # ELSE RETURN DEVICE FIELDS
    return response(True, {'id': device.id, 'code': device.code,
                           'car_wash_id': device.car_wash_id, 'last_update': device.last_update}, 200)


# UPDATE DEVICE
def update_device(device_id, code, car_wash_id):
    # GET DEVICE BY ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    if not device_service_db.get_device_by_id(device_id=device_id):
        return response(False, {'msg': 'device not found'}, 404)

    # GET CAR WASH BY ID AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    if car_wash_id and not car_wash_service_db.get_car_wash_by_id(car_wash_id=car_wash_id):
        return response(False, {'msg': 'car wash not found'}, 404)

    # ELSE UPDATE DEVICE AND RETURN OK
    device_service_db.update_device(device_id=device_id, code=code, car_wash_id=car_wash_id)
    return response(True, {'msg': 'device successfully updated!'}, 200)
