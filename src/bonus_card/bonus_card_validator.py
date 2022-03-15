# BONUS CARD SCHEMA
bonus_card_schema = {
    "type": "object",
    "properties": {
        "code": {"type": "string", "minLength": 1, "maxLength": 120},
        "price": {"type": "number"},
      },
    "required": ["code", "price"]
}
