from src.models.device_model import Device
from datetime import datetime


# GET Device IDS
def get_device_ids():
    ids = []
    devices = Device.query.all()
    for device in devices:
        ids.append(device.id)
    return ids


# GET DEVICE IDS BY CAR WASH ID
def get_device_ids_by_car_wash_id(car_wash_id):
    ids = []
    devices = Device.query.filter_by(car_wash_id=car_wash_id).all()
    for device in devices:
        ids.append(device.id)
    return ids


# GET Device BY TITLE
def get_device_by_code(code):
    device = Device.query.filter_by(code=code).first()
    return device


# GET Device BY ID
def get_device_by_id(device_id):
    device = Device.query.filter_by(id=device_id).first()
    return device


# CREATE Device
def create_device(code, car_wash_id):
    device = Device(code=code, car_wash_id=car_wash_id)
    device.save_db()
    return device


# UPDATE CAR WASH
def update_device(device_id, code, car_wash_id):
    device = Device.query.filter_by(id=device_id).first()
    device.code = code
    device.car_wash_id = car_wash_id
    device.last_update = datetime.utcnow()
    device.update_db()
    return device
