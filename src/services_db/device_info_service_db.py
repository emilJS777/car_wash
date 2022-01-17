from src.models.device_info import DeviceInfo


# GET DEVICE INFO IDS
def get_device_info_ids():
    ids = []
    devices_info = DeviceInfo.query.all()
    for device_info in devices_info:
        ids.append(device_info.id)
    return ids


# GET DEVICE BY ID
def get_device_info_by_id(device_info_id):
    device_info = DeviceInfo.query.filter_by(id=device_info_id).first()
    return device_info


# CREATE DEVICE INFO
def create_device_info(device_id, payment, topic):
    device_info = DeviceInfo(device_id=device_id, payment=payment, topic=topic)
    device_info.save_db()
    return device_info
