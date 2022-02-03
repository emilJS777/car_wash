from src import app
from src.controllers import email_controller


# GET EMAIL BY TICKET ID
app.add_url_rule("/api/email/get_by_ticket_id/<int:ticket_id>",
                 view_func=email_controller.get_email_by_ticket_id,
                 methods=["GET"])

# CREATE EMAIL
app.add_url_rule("/api/email",
                 view_func=email_controller.create_email,
                 methods=["POST"])

# SEND TICKET CODE BY EMAIL ID
app.add_url_rule("/api/email/send_ticket_code_by_email_id/<int:email_id>",
                 view_func=email_controller.send_ticket_code_by_email_id,
                 methods=["GET"])
