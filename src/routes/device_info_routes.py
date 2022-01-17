from src import app
from src.controllers import device_info_controller


# GET DEVICE INFO IDS
app.add_url_rule("/api/device_info",
                 view_func=device_info_controller.get_device_info_ids,
                 methods=["GET"])

# GET DEVICE INFO BY ID
app.add_url_rule("/api/device_info/<int:device_info_id>",
                 view_func=device_info_controller.get_device_info_by_id,
                 methods=["GET"])

# CREATE DEVICE INFO
app.add_url_rule("/api/device_info",
                 view_func=device_info_controller.create_device_info,
                 methods=["POST"])

