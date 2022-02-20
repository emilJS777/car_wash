from src.services import device_payment_service
from src.middlewares import auth_middleware, role_middleware, ticket_middleware, expiration_middleware
from flask import request, g


# GET DEVICE PAYMENT INFO IDS
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(['owner'])
# @expiration_middleware.check_expiration(["owner"])
def get_device_payment_ids():
    res = device_payment_service.get_device_payment_ids(owner_id=g.user_id)
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
