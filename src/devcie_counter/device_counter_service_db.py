from .device_counter_model import DeviceCounterDaily, DeviceCounterTotal
from datetime import datetime

# ***** DAILY


# UPDATE DAILY
def update_daily(device_id: int,
                 owner_id: int,
                 coin: float,
                 bill: float,
                 cashless: float,
                 bonus: float,
                 service: float):
    device_counter_daily: DeviceCounterDaily = DeviceCounterDaily.query.filter_by(device_id=device_id).first() \
                                               or \
                                               DeviceCounterDaily(device_id=device_id, owner_id=owner_id).save_db()
    device_counter_daily.coin = coin
    device_counter_daily.bill = bill
    device_counter_daily.cashless = cashless
    device_counter_daily.bonus = bonus
    device_counter_daily.service = service
    device_counter_daily.last_update = datetime.utcnow()

    device_counter_daily.update_db()
    return device_counter_daily


# GET BY DEVICE ID DAILY
def get_by_device_id_daily(device_id: int):
    device_counter_daily: DeviceCounterDaily = DeviceCounterDaily.query.filter_by(device_id=device_id).first()
    return device_counter_daily


# GET BY DEVICE CODE DAILY
def get_by_device_code_daily(device_code: str):
    device_counter_daily: DeviceCounterDaily = DeviceCounterDaily.query.filter_by(device_code=device_code).first()
    return device_counter_daily


# ***** TOTAL
def update_total(device_id: int,
                 owner_id: int,
                 coin: float,
                 bill: float,
                 cashless: float,
                 bonus: float,
                 service: float):
    device_counter_total: DeviceCounterTotal = DeviceCounterTotal.query.filter_by(device_id=device_id).first() \
                                               or \
                                               DeviceCounterTotal(device_id=device_id, owner_id=owner_id).save_db()
    device_counter_total.coin = coin
    device_counter_total.bill = bill
    device_counter_total.cashless = cashless
    device_counter_total.bonus = bonus
    device_counter_total.service = service
    device_counter_total.last_update = datetime.utcnow()

    device_counter_total.update_db()
    return device_counter_total


# GET BY DEVICE ID TOTAL
def get_by_device_id_total(device_id: int):
    device_counter_total: DeviceCounterTotal = DeviceCounterTotal.query.filter_by(device_id=device_id).first()
    return device_counter_total


# GET BY DEVICE CODE TOTAL
def get_by_device_code_total(device_code: str):
    device_counter_total: DeviceCounterTotal = DeviceCounterTotal.query.filter_by(device_code=device_code).first()
    return device_counter_total

