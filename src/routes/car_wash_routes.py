from src import app
from src.controllers import car_wash_controller


# GET CAR WASH IDS
app.add_url_rule("/api/car_wash",
                 view_func=car_wash_controller.get_car_wash_ids,
                 methods=["GET"])


# GET CAR WASH BY ID
app.add_url_rule("/api/car_wash/<int:car_wash_id>",
                 view_func=car_wash_controller.get_car_wash_by_id,
                 methods=["GET"])


# CREATE CAR WASH
app.add_url_rule("/api/car_wash",
                 view_func=car_wash_controller.create_car_wash,
                 methods=["POST"])


# UPDATE CAR WASH
app.add_url_rule("/api/car_wash/<int:car_wash_id>",
                 view_func=car_wash_controller.update_car_wash,
                 methods=["PUT"])
