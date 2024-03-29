from sqlalchemy import desc
from .device_payment_model import DevicePayment
from typing import List


# GET DEVICE INFO IDS BY DEVICE ID
def get_device_payment_ids_by_device_id(owner_id: int, device_id: int) -> List[int]:
    ids: List[int] = []

    devices_payment: List[DevicePayment] = DevicePayment.query.filter_by(
        owner_id=owner_id,
        device_id=device_id
    ).order_by(desc('creation_date')).all()

    for device_payment in devices_payment:
        ids.append(device_payment.id)

    return ids


# GET DEVICE INFO IDS BY CAR WASH ID
def get_device_payment_ids_by_car_wash_id(owner_id: int, car_wash_id: int) -> List[int]:
    ids: List[int] = []

    devices_payment: List[DevicePayment] = DevicePayment.query.filter_by(
        owner_id=owner_id,
        car_wash_id=car_wash_id
    ).order_by(desc('creation_date')).all()

    for device_payment in devices_payment:
        ids.append(device_payment.id)

    return ids


# GET DEVICE INFO IDS BY CAR WASH ID
def get_device_payment_ids_by_car_wash_id_device_id(owner_id: int, car_wash_id: int, device_id: int) -> List[int]:
    ids: List[int] = []

    devices_payment: List[DevicePayment] = DevicePayment.query.filter_by(
        owner_id=owner_id,
        car_wash_id=car_wash_id,
        device_id=device_id
    ).order_by(desc('creation_date')).all()

    for device_payment in devices_payment:
        ids.append(device_payment.id)

    return ids


# GET DEVICE INFO IDS
def get_device_payment_ids(owner_id: int) -> List[int]:
    ids: List[int] = []

    devices_payment: List[DevicePayment] = DevicePayment.query.filter_by(
        owner_id=owner_id
    ).order_by(desc('creation_date')).all()

    for device_payment in devices_payment:
        ids.append(device_payment.id)

    return ids


# GET DEVICE PAYMENT BY ID
def get_device_payment_by_id(device_payment_id: int) -> DevicePayment:
    device_payment: DevicePayment = DevicePayment.query.filter_by(id=device_payment_id).first()
    return device_payment


# CREATE DEVICE PAYMENT
def create_device_payment(device_id: int, device_code: int, car_wash_id: int, price: float, currency: str, type: str, owner_id: int) -> DevicePayment:
    device_payment: DevicePayment = DevicePayment(device_id=device_id,
                                                  device_code=device_code,
                                                  car_wash_id=car_wash_id,
                                                  price=price,
                                                  currency=currency,
                                                  type=type,
                                                  owner_id=owner_id)
    device_payment.save_db()
    return device_payment
