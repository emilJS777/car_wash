from src import app
from . import bonus_card_controller


# CREATE
app.add_url_rule("/api/bonus_card",
                 view_func=bonus_card_controller.create,
                 methods=["POST"])

# UPDATE
app.add_url_rule("/api/bonus_card/<int:bonus_card_id>",
                 view_func=bonus_card_controller.update,
                 methods=["PUT"])

# DELETE
app.add_url_rule("/api/bonus_card/<int:bonus_card_id>",
                 view_func=bonus_card_controller.delete,
                 methods=["DELETE"])

# GET BY ID
app.add_url_rule("/api/bonus_card/<int:bonus_card_id>",
                 view_func=bonus_card_controller.create,
                 methods=["GET"])

# GET ALL IDS
app.add_url_rule("/api/bonus_card",
                 view_func=bonus_card_controller.get_all_ids,
                 methods=["GET"])
