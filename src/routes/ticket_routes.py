from src import app
from src.controllers import ticket_controller

# CREATE TICKET
app.add_url_rule("/api/ticket", view_func=ticket_controller.create_ticket, methods=["POST"])


# DELETE TICKET
app.add_url_rule("/api/ticket/<int:ticket_id>", view_func=ticket_controller.delete_ticket, methods=["DELETE"])
