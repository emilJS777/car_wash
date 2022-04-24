from . import device_payment_service
from src.role import role_middleware
from src.ticket import ticket_middleware
from src.auth import auth_middleware
from flask import request, g


# GET DEVICE PAYMENT INFO IDS
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(['owner'])
# @expiration_middleware.check_expiration(["owner"])
def get_device_payment_ids():
    print("asdad----", request.args)
    res = device_payment_service.get_device_payment_ids(
        owner_id=g.user_id,
        car_wash_id=request.args.get('car_wash_id'),
        device_id=request.args.get('device_id'))
    return res


# GET DEVICE PAYMENT BY ID
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(['owner'])
# @expiration_middleware.check_expiration(["owner"])
def get_device_payment_by_id(device_payment_id: int):
    res = device_payment_service.get_device_payment_by_id(device_payment_id=device_payment_id)
    return res


# DEVICE PAYMENT
def create_device_payment():
    device_code: str = request.args['device_code']
    currency: str = request.args['currency']
    price: float = float(request.args['price'])
    res = device_payment_service.create_device_payment(device_code=device_code, currency=currency, price=price)
    return res
