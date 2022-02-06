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
                           'price': device_payment.price, 'currency': device_payment.currency,
                           'creation_date': device_payment.creation_date, 'type': device_payment.type}, 200)
