from src import app
from src.controllers import device_controller


# GET DEVICE IDS
app.add_url_rule("/api/device",
                 view_func=device_controller.get_device_ids,
                 methods=["GET"])

# GET DEVICE BY ID
app.add_url_rule("/api/device/<int:device_id>",
                 view_func=device_controller.get_device_by_id,
                 methods=["GET"])

# CREATE DEVICE
app.add_url_rule("/api/device",
                 view_func=device_controller.create_device,
                 methods=["POST"])

# UPDATE DEVICE
app.add_url_rule("/api/device/<int:device_id>",
                 view_func=device_controller.update_device,
                 methods=["PUT"])
