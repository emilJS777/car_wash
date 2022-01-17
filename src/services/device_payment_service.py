from src.services_db import device_payment_service_db, device_service_db
from src._response import response


# GET DEVICE PAYMENT IDS
def get_device_payment_ids():
    device_payment_info_ids = device_payment_service_db.get_device_payment_ids()
    return response(True, device_payment_info_ids, 200)


# GET DEVICE PAYMENT BY ID
def get_device_payment_by_id(device_payment_id):
    # GET DEVICE PAYMENT BY ID AND VERIFY. OF NOT FOUND RETURN NOT FOUND
    device_payment = device_payment_service_db.get_device_payment_by_id(device_payment_id=device_payment_id)
    if not device_payment:
        return response(False, {'msg': 'device payment not found'}, 404)

    # ELSE RETURN DEVICE PAYMENT FIELDS AND OK
    return response(True, {'id': device_payment.id, 'device_id': device_payment.device_id,
                           'payment': device_payment.payment, 'currency': device_payment.currency,
                           'topic': device_payment.topic}, 200)


# CREATE DEVICE PAYMENT
def create_device_payment(device_id, payment, currency, topic):
    # GET DEVICE BY ID AND VERIFY. OF NOT FOUND RETURN NOT FOUND
    if not device_service_db.get_device_by_id(device_id=device_id):
        return response(False, {'msg': 'device not found'}, 404)

    # ELSE CREATE NEW DEVICE PAYMENT AND RETURN OK
    device_payment = device_payment_service_db.create_device_payment(device_id=device_id, payment=payment,
                                                                     currency=currency, topic=topic)
    return response(True, {'msg': f'device info by id {device_payment.payment} successfully created!'}, 201)
