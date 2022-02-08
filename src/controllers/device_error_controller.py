from src.services import device_error_service
from src.middlewares import auth_middleware, role_middleware


# GET DEVICE ERROR IDS
@auth_middleware.check_authorize
@role_middleware.check_role(["admin"])
def get_device_error_ids():
    res = device_error_service.get_device_error_ids()
    return res


# GET DEVICE ERROR BY ID
@auth_middleware.check_authorize
@role_middleware.check_role(["admin"])
def get_device_error_by_id(device_error_id):
    res = device_error_service.get_device_error_by_id(device_error_id=device_error_id)
    return res
