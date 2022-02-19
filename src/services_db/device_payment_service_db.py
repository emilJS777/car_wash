from sqlalchemy import desc
from src.models.device_payment_model import DevicePayment


# GET DEVICE INFO IDS
def get_device_payment_ids(owner_id) -> list:
    ids = list([])
    devices_payment = list(DevicePayment.query.filter_by(owner_id=owner_id).order_by(desc('creation_date')).all())
    for device_payment in devices_payment:
        ids.append(device_payment.id)
    return ids


# GET DEVICE PAYMENT BY ID
def get_device_payment_by_id(device_payment_id) -> DevicePayment:
    device_payment = DevicePayment.query.filter_by(id=device_payment_id).first()
    return device_payment


# CREATE DEVICE PAYMENT
def create_device_payment(device_id, price, currency, type, owner_id, device_code) -> DevicePayment:
    device_payment = DevicePayment(device_id=device_id, price=price,
                                   currency=currency, type=type,
                                   owner_id=owner_id, device_code=device_code)
    device_payment.save_db()
    return device_payment
