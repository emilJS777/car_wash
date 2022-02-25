from . import qr_controller
from src import app


# CREATE Qr
app.add_url_rule("/api/qr",
                 view_func=qr_controller.create_qr,
                 methods=["POST"])

# GET QR
app.add_url_rule("/api/qr",
                 view_func=qr_controller.get_current_qr,
                 methods=["GET"])


# DELETE QR BY ID
app.add_url_rule("/api/qr/<int:qr_id>",
                 view_func=qr_controller.delete_qr,
                 methods=["DELETE"])
