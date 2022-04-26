from src import app
from . import device_controller

# GET DEVICE IDS
app.add_url_rule("/api/device",
                 view_func=device_controller.get_device_ids,
                 methods=["GET"])

# GET DEVICE IDS BY OWNER ID
app.add_url_rule("/api/device/by_owner_id/<int:owner_id>",
                 view_func=device_controller.get_device_ids_by_owner_id,
                 methods=["GET"])

# GET DEVICE IDS BY CAR WASH ID
app.add_url_rule("/api/device/by_car_wash_id/<int:car_wash_id>",
                 view_func=device_controller.get_device_ids_by_car_wash_id,
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

# DELETE DEVICE
app.add_url_rule("/api/device/<int:device_id>",
                 view_func=device_controller.delete_device,
                 methods=["DELETE"])

# ******** DEVICE ACTIVE UPDATE
app.add_url_rule("/api/device/active",
                 view_func=device_controller.update_device_active,
                 methods=["PUT"])

# ******** DEVICE CENTENT UDPDATE
# UPDATE DEVICE CONTENT
app.add_url_rule("/api/device_content",
                 view_func=device_controller.update_device_content,
                 methods=["GET"])

