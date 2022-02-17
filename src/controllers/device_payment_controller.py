from src.services import device_payment_service
from src.middlewares import auth_middleware, role_middleware, ticket_middleware, expiration_middleware
from flask import request


# GET DEVICE PAYMENT INFO IDS
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(['owner'])
@expiration_middleware.check_expiration(["owner"])
def get_device_payment_ids():
    res = device_payment_service.get_device_payment_ids()
    return res


# GET DEVICE PAYMENT BY ID
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(['owner'])
@expiration_middleware.check_expiration(["owner"])
def get_device_payment_by_id(device_payment_id):
    res = device_payment_service.get_device_payment_by_id(device_payment_id=device_payment_id)
    return res


# DEVICE PAYMENT
def create_device_payment():
    device_code = request.args['device_code']
    currency = request.args['currency']
    price = request.args['price']
    res = device_payment_service.create_device_payment(device_code=device_code, currency=currency, price=price)
    return res
