from src import app
from . import device_payment_controller

# GET DEVICE PAYMENT INFO IDS
app.add_url_rule("/api/device_payment",
                 view_func=device_payment_controller.get_device_payment_ids,
                 methods=["GET"])

# GET DEVICE PAYMENT INFO BY ID
app.add_url_rule("/api/device_payment/<int:device_payment_id>",
                 view_func=device_payment_controller.get_device_payment_by_id,
                 methods=["GET"])

# GET DEVICE PAYMENT INFO BY ID
app.add_url_rule("/api/device_payment/create",
                 view_func=device_payment_controller.create_device_payment,
                 methods=["GET"])
