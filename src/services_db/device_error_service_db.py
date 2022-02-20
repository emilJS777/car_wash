from typing import List
from src.models.device_error_model import DeviceError


# GET DEVICE ERROR IDS
def get_device_error_ids() -> List[int]:
    ids: List[int] = []
    device_errors: List[DeviceError] = DeviceError.query.order_by(DeviceError.creation_date).all()
    for device_error in device_errors:
        ids.append(device_error.id)
    return ids


# GET DEVICE ERROR BY ID
def get_device_error_by_id(device_error_id: int) -> DeviceError:
    device_error: DeviceError = DeviceError.query.filter_by(id=device_error_id).first()
    return device_error


# CREATE DEVICE ERROR
def create_device_error(device_code: str, msg: str) -> DeviceError:
    device_error: DeviceError = DeviceError(device_code=device_code, msg=msg)
    device_error.save_db()
    return device_error

