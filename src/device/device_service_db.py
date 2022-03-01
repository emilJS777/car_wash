from typing import List
from .device_model import Device
from datetime import datetime
from sqlalchemy import desc


# GET Device IDS
async def get_device_ids() -> List[int]:
    ids: List[int] = []
    devices: List[Device] = await Device.query.order_by(desc(Device.last_update)).all()
    for device in devices:
        ids.append(device.id)
    return ids


# GET DEVICE IDS BY CAR WASH ID
async def get_device_ids_by_owner(owner_id: int) -> List[int]:
    ids: List[int] = []
    devices: List[Device] = await Device.query.filter_by(owner_id=owner_id).order_by(desc(Device.last_update)).all()
    for device in devices:
        ids.append(device.id)
    return ids


# GET Device BY TITLE
async def get_device_by_code(code: str) -> Device:
    device: Device = await Device.query.filter_by(code=code).first()
    return device


# GET Device BY ID
async def get_device_by_id(device_id: int) -> Device:
    device: Device = await Device.query.filter_by(id=device_id).first()
    return device


# CREATE Device
async def create_device(code: str, owner_id: int) -> Device:
    device: Device = Device(code=code, owner_id=owner_id)
    await device.save_db()
    return device


# UPDATE DEVICE
async def update_device(device_id: int, code: str) -> Device:
    device: Device = await Device.query.filter_by(id=device_id).first()
    device.code = code
    device.last_update = datetime.utcnow()
    await device.update_db()
    return device


# ACTIVATE DEVICE
async def activate_device(device_id: int) -> Device:
    device: Device = await Device.query.filter_by(id=device_id).first()
    device.active = True
    await device.update_db()
    return device


# DEACTIVATE DEVICE
async def deactivate_device(device_id: int) -> Device:
    device: Device = await Device.query.filter_by(id=device_id).first()
    device.active = False
    await device.update_db()
    return device


# ******* DEVICE CONTENT


# UPDATE DEVICE CONTENT
async def update_device_content(device_id: int, water: bool, lather: bool) -> Device:
    device_content: Device = await Device.query.filter_by(id=device_id).first()
    device_content.water = water
    device_content.lather = lather
    device_content.last_update = datetime.utcnow()
    await device_content.update_db()
    return device_content
