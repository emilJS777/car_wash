from src.services import device_error_service


# GET DEVICE ERROR IDS
def get_device_error_ids():
    res = device_error_service.get_device_error_ids()
    return res


# GET DEVICE ERROR BY ID
def get_device_error_by_id(device_error_id):
    res = device_error_service.get_device_error_by_id(device_error_id=device_error_id)
    return res
