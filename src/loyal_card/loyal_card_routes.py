from src import app
from . import loyal_card_controller


# CREATE
app.add_url_rule("/api/loyal_card",
                 view_func=loyal_card_controller.create,
                 methods=["POST"])

# UPDATE
app.add_url_rule("/api/loyal_card/<int:loyal_card_id>",
                 view_func=loyal_card_controller.update,
                 methods=["PUT"])

# DELETE
app.add_url_rule("/api/loyal_card/<int:loyal_card_id>",
                 view_func=loyal_card_controller.delete,
                 methods=["DELETE"])

# GET BY ID
app.add_url_rule("/api/loyal_card/<int:loyal_card_id>",
                 view_func=loyal_card_controller.get_by_id,
                 methods=["GET"])

# GET ALL IDS
app.add_url_rule("/api/loyal_card",
                 view_func=loyal_card_controller.get_all_ids,
                 methods=["GET"])
