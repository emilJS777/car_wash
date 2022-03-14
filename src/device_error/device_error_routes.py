from src import app
from . import device_error_controller

# GET DEVICE ERROR IDS
app.add_url_rule("/api/device_error",
                 view_func=device_error_controller.get_device_error_ids,
                 methods=["GET"])

# GET DEVICE ERROR BY ID
app.add_url_rule("/api/device_error/<int:device_error_id>",
                 view_func=device_error_controller.get_device_error_by_id,
                 methods=["GET"])


# CREATE DEVICE ERROR
app.add_url_rule("/api/device_error/create",
                 view_func=device_error_controller.create_device_error,
                 methods=["GET"])
