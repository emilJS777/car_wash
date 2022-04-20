from src import app
from . import loyal_card_payment_controller


# CREATE PAYMENT BONUS CARD
app.add_url_rule("/api/loyal_card_payment",
                 view_func=loyal_card_payment_controller.create_payment,
                 methods=["POST"])


# DELETE BONUS CARD PAYMENT
app.add_url_rule("/api/loyal_card_payment/<int:loyal_card_payment_id>",
                 view_func=loyal_card_payment_controller.delete_payment,
                 methods=["DELETE"])


# GET BY ID
app.add_url_rule("/api/loyal_card_payment/<int:loyal_card_payment_id>",
                 view_func=loyal_card_payment_controller.get_payment_by_id,
                 methods=["GET"])


# GET ALL IDS BY BONUS CARD ID
app.add_url_rule("/api/loyal_card_payment_ids_by_loyal_card_id/<int:loyal_card_id>",
                 view_func=loyal_card_payment_controller.get_all_ids_by_loyal_card_id,
                 methods=["GET"])
