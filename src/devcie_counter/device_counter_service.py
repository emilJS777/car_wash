from . import device_counter_service_db
from src.device import device_service_db
from src._response import response


def update_counters(counters):
    for data in counters:
        device = device_service_db.get_device_by_code(data['id'])
        if device:
            device_counter_service_db.update_daily(
                device_id=device.id,
                owner_id=device.owner_id,
                coin=data['coin']['d'],
                bill=data['bill']['d'],
                cashless=data['cashless']['d'],
                bonus=data['bonus']['d'],
                service=data['service']['d']
            )

            device_counter_service_db.update_total(
                device_id=device.id,
                owner_id=device.owner_id,
                coin=data['coin']['t'],
                bill=data['bill']['t'],
                cashless=data['cashless']['t'],
                bonus=data['bonus']['t'],
                service=data['service']['t']
            )


def get_daily_by_device_id(device_id: int):
    # GET DEVICE COUNTER DAILY BY DEVICE ID IF NOT FOUND RETURN 404
    device_counter_daily = device_counter_service_db.get_by_device_id_daily(device_id)
    if not device_counter_daily:
        return response(False, {'msg': 'device counter daily not found'}, 404)

    return response(True, {'device_id': device_counter_daily.device_id,
                           'coin': device_counter_daily.coin,
                           'bill': device_counter_daily.bill,
                           'cashless': device_counter_daily.cashless,
                           'service': device_counter_daily.service}, 200)


def get_total_by_device_id(device_id: int):
    # GET DEVICE COUNTER TOTAL BY DEVICE ID IF NOT FOUND RETURN 404
    device_counter_total = device_counter_service_db.get_by_device_id_total(device_id)
    if not device_counter_total:
        return response(False, {'msg': 'device counter total not found'}, 404)

    return response(True, {'device_id': device_counter_total.device_id,
                           'coin': device_counter_total.coin,
                           'bill': device_counter_total.bill,
                           'cashless': device_counter_total.cashless,
                           'service': device_counter_total.service}, 200)

