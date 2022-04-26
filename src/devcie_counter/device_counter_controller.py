from . import device_counter_service


# GET DAILY BY DEVICE ID
def get_device_counter_daily_by_device_id(device_id: int):
    res = device_counter_service.get_daily_by_device_id(device_id)
    return res


# GET TOTAL BY DEVICE ID
def get_device_counter_total_by_device_id(device_id: int):
    res = device_counter_service.get_total_by_device_id(device_id)
    return res
