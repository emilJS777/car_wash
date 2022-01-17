from src import app
from src.controllers import user_controller

# GET USER BY ID
app.add_url_rule("/api/user/<int:user_id>", view_func=user_controller.get_user_by_id, methods=["GET"])

# CREATE USER
app.add_url_rule("/api/user", view_func=user_controller.create_user, methods=["POST"])

# UPDATE USER
app.add_url_rule("/api/user/<int:user_id>", view_func=user_controller.update_user, methods=["PUT"])

# DELETE USER
app.add_url_rule("/api/user/<int:user_id>", view_func=user_controller.delete_user, methods=["DELETE"])
