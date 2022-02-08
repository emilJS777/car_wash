from src.services import device_payment_service
from src.middlewares import auth_middleware, role_middleware, ticket_middleware, expiration_middleware


# GET DEVICE INFO IDS
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(['owner'])
@expiration_middleware.check_expiration(["owner"])
def get_device_payment_ids():
    res = device_payment_service.get_device_payment_ids()
    return res


# GET DEVICE BY ID
@auth_middleware.check_authorize
@ticket_middleware.check_active_ticket
@role_middleware.check_role(['owner'])
@expiration_middleware.check_expiration(["owner"])
def get_device_payment_by_id(device_payment_id):
    res = device_payment_service.get_device_payment_by_id(device_payment_id=device_payment_id)
    return res
