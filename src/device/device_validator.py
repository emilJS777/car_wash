# DEVICE SCHEMA
device_schema = {
    "type": "object",
    "properties": {
        "code": {"type": "string", "minLength": 1, "maxLength": 120},
        "owner_id": {"type": "number", "minLength": 1},
        "car_wash_id": {"type": "number", "minLength": 1}
      },
    "required": ["code", "owner_id", "car_wash_id"]
}
