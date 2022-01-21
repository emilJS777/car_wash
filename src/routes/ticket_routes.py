from src import app
from src.controllers import ticket_controller

# GET ENGINEER TICKETS
app.add_url_rule("/api/ticket/engineer",
                 view_func=ticket_controller.get_engineer_tickets,
                 methods=["GET"])


# CREATE TICKET
app.add_url_rule("/api/ticket",
                 view_func=ticket_controller.create_ticket,
                 methods=["POST"])


# DELETE TICKET
app.add_url_rule("/api/ticket/<int:ticket_id>",
                 view_func=ticket_controller.delete_ticket,
                 methods=["DELETE"])


# ACTIVATE OR DEACTIVATE TICKET
app.add_url_rule("/api/ticket/<int:ticket_id>",
                 view_func=ticket_controller.activate_or_deactivate_ticket,
                 methods=["PUT"])
