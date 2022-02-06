from src.models.device_error_model import DeviceError


# GET DEVICE ERROR IDS
def get_device_error_ids():
    ids = []
    device_errors = DeviceError.query.order_by(DeviceError.creation_date).all()
    for device_error in device_errors:
        ids.append(device_error.id)
    return ids


# GET DEVICE ERROR BY ID
def get_device_error_by_id(device_error_id):
    device_error = DeviceError.query.filter_by(id=device_error_id).first()
    return device_error


# CREATE DEVICE ERROR
def create_device_error(device_code, msg):
    device_error = DeviceError(device_code=device_code, msg=msg)
    device_error.save_db()
    return device_error

