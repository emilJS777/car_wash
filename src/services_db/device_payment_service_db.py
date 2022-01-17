from src.models.device_payment_model import DevicePayment


# GET DEVICE INFO IDS
def get_device_payment_ids():
    ids = []
    devices_payment = DevicePayment.query.all()
    for device_payment in devices_payment:
        ids.append(device_payment.id)
    return ids


# GET DEVICE PAYMENT BY ID
def get_device_payment_by_id(device_payment_id):
    device_payment = DevicePayment.query.filter_by(id=device_payment_id).first()
    return device_payment


# CREATE DEVICE PAYMENT
def create_device_payment(device_id, payment, currency, topic):
    device_payment = DevicePayment(device_id=device_id, payment=payment, currency=currency, topic=topic)
    device_payment.save_db()
    return device_payment
