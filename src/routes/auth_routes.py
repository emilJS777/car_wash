from src import app
from src.controllers import auth_controller

# LOGIN
app.add_url_rule("/api/auth", view_func=auth_controller.login, methods=["POST"])

# REFRESH TOKEN
app.add_url_rule("/api/auth", view_func=auth_controller.refresh, methods=["PUT"])

# GET PROFILE
app.add_url_rule("/api/auth", view_func=auth_controller.get_profile, methods=["GET"])
