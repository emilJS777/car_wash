from src.models.device_error_model import DeviceError


# CREATE DEVICE ERROR
def create_device_error(device_code, msg):
    device_error = DeviceError(device_code=device_code, msg=msg)
    device_error.save_db()
    return device_error

