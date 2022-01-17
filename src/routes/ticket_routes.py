from src import app
from src.controllers import ticket_controller

# CREATE TICKET
app.add_url_rule("/api/ticket", view_func=ticket_controller.create_ticket, methods=["POST"])
