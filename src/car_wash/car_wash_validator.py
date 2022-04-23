# CAR WASH SCHEMA
car_wash_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 3, "maxLength": 60},
        "address": {"type": "string", "minLength": 4, "maxLength": 120},
        "owner_id": {"type": "number", "minLength": 1}
      },
    "required": ["title", "address", "owner_id"]
}
