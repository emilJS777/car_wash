# from src.device_payment import device_payment_service_db
# from src.device_error import device_error_service_db
# from src.device import device_service_db
#
#
# # DEVICE ERROR LOG
# def device_error(data):
#     # CREATE DEVICE ERROR LOG
#     device_error_service_db.create_device_error(device_code=data['device_code'], msg=data['msg'])
#
#
# # DEVICE PAYMENT BY CASH
# def device_payment_cash(data):
#     # GET DEVICE BY CODE AND VERIFY. IF DEVICE EXIST CREATE DEVICE PAYMENT BY THIS DEVICE ID
#     device = device_service_db.get_device_by_code(code=data['device_code'])
#     if device:
#         device_payment_service_db.create_device_payment(device_id=device.id,
#                                                         price=data['price'],
#                                                         currency=data['currency'],
#                                                         type='cash')
