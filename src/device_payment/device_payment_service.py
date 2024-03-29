from . import device_payment_service_db
from src.device import device_service_db
from src._response import response
from typing import List


# GET DEVICE PAYMENT IDS BY DEVICE ID
def get_device_payment_ids(owner_id: int, car_wash_id: int or None, device_id: int or None):
    if device_id and car_wash_id:
        device_payment_ids: List[int] = device_payment_service_db.get_device_payment_ids_by_car_wash_id_device_id(
            owner_id=owner_id,
            car_wash_id=int(car_wash_id),
            device_id=int(device_id)
        )
    elif device_id:
        device_payment_ids: List[int] = device_payment_service_db.get_device_payment_ids_by_device_id(
            owner_id=owner_id,
            device_id=int(device_id)
        )
    elif car_wash_id:
        device_payment_ids: List[int] = device_payment_service_db.get_device_payment_ids_by_car_wash_id(
            owner_id=owner_id,
            car_wash_id=int(car_wash_id)
        )
    else:
        device_payment_ids: List[int] = device_payment_service_db.get_device_payment_ids(
            owner_id=owner_id
        )

    return response(True, device_payment_ids, 200)


# GET DEVICE PAYMENT BY ID
def get_device_payment_by_id(device_payment_id):
    # GET DEVICE PAYMENT BY ID AND VERIFY. OF NOT FOUND RETURN NOT FOUND
    device_payment = device_payment_service_db.get_device_payment_by_id(device_payment_id=device_payment_id)
    if not device_payment:
        return response(False, {'msg': 'device payment not found'}, 404)

    # ELSE RETURN DEVICE PAYMENT FIELDS AND OK
    return response(True, {'id': device_payment.id,
                           'device_id': device_payment.device_id,
                           'device_code': device_payment.device_code,
                           'price': device_payment.price,
                           'currency': device_payment.currency,
                           'creation_date': device_payment.creation_date,
                           'type': device_payment.type}, 200)


# # CREATE DEVICE PAYMENT
# def create_device_payment(device_code, price, currency, type):
#     # GET DEVICE BY CODE AND VERIFY. IF NOT FOUND RETURN NOT FOUND
#     device = device_service_db.get_device_by_code(code=device_code)
#     if not device:
#         return response(False, {'msg': 'device not found'}, 404)
#
#     # IF DEVICE IS NOT ACTIVE CHANGE TO ACTIVE
#     if not device.active:
#         device_service_db.activate_device(device_id=device.id)
#
#     # ELSE CREATE DEVICE PAYMENT END RETURN OK
#     device_payment = device_payment_service_db.create_device_payment(device_id=device.id,
#                                                                      car_wash_id=device.car_wash_id,
#                                                                      price=price,
#                                                                      currency=currency,
#                                                                      type=type,
#                                                                      owner_id=device.owner_id)
#     return response(True, {'id': device_payment.id, 'device_id': device.id, 'price': device_payment.price}, 200)


# CREATE DEVICE PAYMENT
def create_device_payment(device_code, price, currency, type):
    # GET DEVICE BY CODE AND VERIFY. IF NOT FOUND RETURN NOT FOUND
    device = device_service_db.get_device_by_code(code=device_code)
    if device:
        device_payment_service_db.create_device_payment(device_id=device.id,
                                                        device_code=device_code,
                                                        car_wash_id=device.car_wash_id,
                                                        price=price,
                                                        currency=currency,
                                                        type=type,
                                                        owner_id=device.owner_id)
