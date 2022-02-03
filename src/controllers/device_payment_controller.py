from src.services import device_payment_service
from flask import request
from src.middlewares import auth_middleware, role_middleware, ticket_middleware


# GET DEVICE INFO IDS
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(['engineer'])
def get_device_payment_ids():
    res = device_payment_service.get_device_payment_ids()
    return res


# GET DEVICE BY ID
@auth_middleware.check_authorize
@role_middleware.check_role(['engineer'])
def get_device_payment_by_id(device_payment_id):
    res = device_payment_service.get_device_payment_by_id(device_payment_id=device_payment_id)
    return res


# CREATE DEVICE INFO
def create_device_payment():
    req = request.get_json()
    res = device_payment_service.create_device_payment(device_id=req['device_id'], payment=req['payment'],
                                                       currency=req['currency'], topic=req['topic'])
    return res
