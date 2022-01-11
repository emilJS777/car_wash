from src import app
from src.controllers import role_controller


# GET BY ID
app.add_url_rule("/api/role/<int:role_id>", view_func=role_controller.get_role_by_id, methods=["GET"])

# GET ROLE IDS
app.add_url_rule("/api/role", view_func=role_controller.get_role_ids, methods=["GET"])
