# BONUS CARD SCHEMA
bonus_card_schema = {
    "type": "object",
    "properties": {
        "code": {"type": "string", "minLength": 1, "maxLength": 120},
        "price": {"type": "number"},
        "full_name": {"type": "string", "minLength": 1, "maxLength": 60}
      },
    "required": ["code", "price", "full_name"]
}
