from src import app
from . import device_counter_controller


app.add_url_rule("/api/device_counter_daily/by_device_id/<int:device_id>",
                 view_func=device_counter_controller.get_device_counter_daily_by_device_id,
                 methods=["GET"])

app.add_url_rule("/api/device_counter_total/by_device_id/<int:device_id>",
                 view_func=device_counter_controller.get_device_counter_total_by_device_id,
                 methods=["GET"])
