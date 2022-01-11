from src import app
from src.controllers import user_controller

# USER CREATE (REGISTRATION)
app.add_url_rule("/api/user", view_func=user_controller.create_user, methods=["POST"])
