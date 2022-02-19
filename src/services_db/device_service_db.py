from src.models.device_model import Device
from datetime import datetime
from sqlalchemy import desc


# GET Device IDS
def get_device_ids():
    ids = []
    devices = Device.query.order_by(desc(Device.last_update)).all()
    for device in devices:
        ids.append(device.id)
    return ids


# GET DEVICE IDS BY CAR WASH ID
def get_device_ids_by_owner(owner_id):
    ids = []
    devices = Device.query.filter_by(owner_id=owner_id).order_by(desc(Device.last_update)).all()
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
def create_device(code, owner_id):
    device = Device(code=code, owner_id=owner_id)
    device.save_db()
    return device


# UPDATE DEVICE
def update_device(device_id, code):
    device = Device.query.filter_by(id=device_id).first()
    device.code = code
    device.last_update = datetime.utcnow()
    device.update_db()
    return device


# ACTIVATE DEVICE
def activate_device(device_id):
    device = Device.query.filter_by(id=device_id).first()
    device.active = True
    device.update_db()
    return device


# DEACTIVATE DEVICE
def deactivate_device(device_id):
    device = Device.query.filter_by(id=device_id).first()
    device.active = False
    device.update_db()
    return device
